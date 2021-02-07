import os
import sys
from functools import partial

import qdarkstyle
from PySide2.QtWidgets import QMainWindow, QApplication, QFileDialog
from openpyxl import load_workbook

from ui.ui_tps import Ui_TandaPaySimulationWindow
from utils.common import get_config, update_config_file
from utils.logger import logger


class TandaPaySimulationApp(QMainWindow):

    def __init__(self, matrix=None, edge=False):
        super().__init__()
        self.ui = Ui_TandaPaySimulationWindow()
        self.ui.setupUi(self)
        self._matrix = matrix
        self.edge = edge
        self.conf = get_config()
        self.wb = {}
        self.sh = {}
        for k in {"system", "user", "matrix"}:
            getattr(self.ui, f"{k}_database").setText(self.conf['database'][k])
            getattr(self.ui, f"btn_{k}_database").released.connect(partial(self._on_btn_database, k))
            self._init_sheet(k)
        self.ev = [0] * 10
        self.pv = [0] * 6
        for i in range(9):
            getattr(self.ui, f"ev_{i}").textChanged.connect(partial(self._on_value_changed, 'ev', i))
            self.ev[i] = int(getattr(self, f"ev_{i}").value())
        for i in range(6):
            getattr(self.ui, f"pv_{i}").textChanged.connect(partial(self._on_value_changed, 'pv', i))
            self.pv[i] = int(getattr(self, f"pv_{i}").value())
        self.ui.btn_exit.released.connect(self.close)
        self.ui.btn_start.released.connect(self.btn_start)
        self.ui.btn_clear.released.connect(self.btn_clear)

    def _on_btn_database(self, db_type: str):
        db_file, _ = QFileDialog.getOpenFileName(
            self, f"Select {db_type.capitalize()} Database File",
            os.path.dirname(self.conf['database'][db_type]), "Excel files (*.xlsx)")
        if db_file:
            self.conf['database'][db_type] = db_file
            update_config_file(self.conf)
            getattr(self.ui, f"{db_type}_database").setText(db_file)
            self._init_sheet(db_type)

    def _init_sheet(self, db_type):
        db_file = self.conf['database'][db_type]
        self.wb[db_type] = load_workbook(db_file)
        if db_type != 'matrix':
            self.sh[db_type] = self.wb[db_type].active
        else:
            self.sh['matrix_var_sh'] = self.wb[db_type]['Variable Map']
            self.sh['matrix_sys_log'] = self.wb[db_type]['System Log']
        if db_type == 'user':
            for row in self.sh['user']['A2:N200']:
                for cell in row:
                    cell.value = None
            self.wb['user'].save(db_file)
        elif db_type == 'system':
            for row in self.sh['system']['C2:U37']:
                for cell in row:
                    cell.value = None
            self.wb['system'].save(db_file)

    def _on_value_changed(self, v_type, index, value):
        getattr(self, v_type)[index] = int(value)

    def _checksum(self, syfunc: int, period: int, line: int):
        c_count = 0
        c_value = 0
        last_checked = 0
        for i in range(self.ev[0]):
            c_us_rec3_val = self.sh['user'].cell(i + 2, 4)
            c_us_rec8_val = self.sh['user'].cell(i + 2, 9)
            if c_us_rec3_val.value == 0 or c_us_rec8_val.value == 'defected':
                continue
            c_us_rec4_val = self.sh['user'].cell(i + 2, 5)
            if c_us_rec3_val.value != last_checked:
                for _i in range(self.ev[0]):
                    c_ur3_sub = self.sh['user'].cell(_i + 2, 4)
                    c_ur8_sub = self.sh['user'].cell(_i + 2, 9)
                    if c_ur3_sub.value == 0 or c_ur8_sub.value == 'defected':
                        continue
                    c_ur4_sub = self.sh['user'].cell(_i + 2, 5)
                    if c_ur3_sub.value == c_us_rec3_val.value:
                        c_count += 1
                        c_value += c_ur4_sub.value
                if c_value % c_count != 0 or c_count != c_us_rec4_val.value:
                    logger.debug(f'______________ Period {period} -> Line {line}')
                    if self._matrix:
                        run_log_index = self.run - 1
                        msg = f'Run {run_log_index}: SyFunc {syfunc} _checksum failed: c_value % c_count = ' \
                              f'{c_value % c_count} - supposed to be 0.\nc_UsRec3_val:{c_us_rec3_val.value}'
                    else:
                        msg = f'SyFunc {syfunc} _checksum failed: c_value % c_count = {c_value % c_count} - ' \
                              f'supposed to be 0.\nc_UsRec3_val:{c_us_rec3_val.value}'
                    logger.error(msg)
                last_checked = c_us_rec3_val.value
                c_count = 0
                c_value = 0

    def _checksum_sr1(self, _sy_rec1_val: int, syfunc: int, period: int, line: int):
        counter = 0
        for i in range(self.ev[0]):
            c_us_rec_3 = self.sh['user'].cell(i + 2, 4)
            if c_us_rec_3.value == 0:
                counter += 1
        if self.ev[0] - _sy_rec1_val != counter:
            logger.debug(f'______________ Period {period} -> Line {line}')
            if self._matrix:
                run_log_index = self.run - 1
                msg = f'Run {run_log_index}: SyFunc {syfunc} _checksum_sr1 failed: counter = {counter} - ' \
                      f'supposed to be {self.ev[0] - _sy_rec1_val}'
            else:
                msg = f'SyFunc {syfunc} _checksum_sr1 failed: counter = {counter} - ' \
                      f'supposed to be {self.ev[0] - _sy_rec1_val}'
            logger.error(msg)

    def get_valid_users(self) -> list:
        """
        Returns list of user indexes (for Excel) where User Record 5 is equal to 'valid'
        """
        return [i + 2 for i in range(self.ev[0]) if self.sh['user'].cell(i + 2, 6).value == 'valid']

    def get_select_users(self, _filter: str, u_rec: int) -> list:
        """
        Returns list of user indexes (for Excel) where User Record 'u_rec' is equal to '_filter' argument
        """
        return [i + 2 for i in range(self.ev[0]) if self.sh['user'].cell(i + 2, u_rec + 1).value == _filter]

    def btn_start(self):
        start_iter = 0
        counter = 0
        current_period_list = []

    def btn_clear(self):
        pass


if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
    ex = TandaPaySimulationApp()

    sys._excepthook = sys.excepthook

    def exception_hook(exctype, value, tb):
        logger.error("=========== Crashed!", exc_info=(exctype, value, tb))
        getattr(sys, "_excepthook")(exctype, value, tb)
        ex.on_crashed()
        sys.exit(1)

    sys.excepthook = exception_hook

    logger.info('========== Starting TandaPay Simulation Application ==========')

    ex.show()
    sys.exit(app.exec_())
