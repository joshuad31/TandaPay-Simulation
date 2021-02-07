import os
import sys
from functools import partial

import qdarkstyle
from PySide2.QtWidgets import QMainWindow, QApplication, QFileDialog

from ui.ui_tps import Ui_TandaPaySimulationWindow
from utils.common import get_config, update_config_file
from utils.logger import logger


class TandaPaySimulationApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_TandaPaySimulationWindow()
        self.ui.setupUi(self)
        self.conf = get_config()
        for k in {"system", "user", "matrix"}:
            getattr(self.ui, f"{k}_database").setText(self.conf['database'][k])
            getattr(self.ui, f"btn_{k}_database").released.connect(partial(self._on_btn_database, k))
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

    def btn_start(self):
        pass

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
