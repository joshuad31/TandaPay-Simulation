import threading
import sys
from functools import partial

import qdarkstyle
from PySide2.QtCore import Signal, QSize
from PySide2.QtGui import Qt
from PySide2.QtWidgets import QMainWindow, QApplication, QFileDialog, QDoubleSpinBox, QWidget

from settings import RESULT_DIR
from ui.ui_tps import Ui_TandaPaySimulationWindow
from utils.graph import MplCanvas
from utils.logger import logger
from utils.message import show_message
from utils.tandapay import TandaPaySimulator


class TandaPaySimulationApp(QMainWindow):

    finished = Signal()
    matrix_status = Signal(int)

    def __init__(self):
        super().__init__()
        self.ui = Ui_TandaPaySimulationWindow()
        self.ui.setupUi(self)
        self.result_path = RESULT_DIR
        self.ui.result_path.setText(self.result_path)

        # Variables for single run
        self.ev = [0, 0, 0, 0, 0, 0, 0, 0, .3333, 0.]
        self.pv = [0, 0, 0, 0, 0, 0]
        # Bind events for the single run
        for i in range(9):
            name = f"ev_{i}"
            if hasattr(self.ui, name):
                getattr(self.ui, name).textChanged.connect(partial(self._on_value_changed, 'ev', i))
                self._on_value_changed('ev', i, float(getattr(self.ui, name).value()))
        for i in range(6):
            name = f"pv_{i}"
            getattr(self.ui, name).textChanged.connect(partial(self._on_value_changed, 'pv', i))
            self._on_value_changed('pv', i, float(getattr(self.ui, name).value()))

        # Bind events for the matrix group selectors
        for combo, v_type, index in self._get_comboboxes():
            combo.currentTextChanged.connect(partial(self._on_group_changed, combo, v_type, index))

        self.ui.btn_exit.released.connect(self.close)
        self.ui.btn_exit_matrix.released.connect(self.close)
        self.ui.btn_start_single.released.connect(self.btn_start_single)
        self.ui.btn_start_matrix.released.connect(self.btn_start_matrix)
        self.ui.btn_result_path.released.connect(self._on_btn_result_path)

        self.canvas = MplCanvas(width=5, height=4, dpi=100)
        self.ui.layout_graph.addWidget(self.canvas)
        getattr(self, 'finished').connect(self._on_single_process_finished)

    def _on_btn_result_path(self):
        result_path = QFileDialog.getExistingDirectory(self, "Select a Folder to Save Result", self.result_path)
        if result_path:
            self.result_path = result_path
            self.ui.result_path.setText(self.result_path)

    def _on_value_changed(self, v_type, index, value):
        # All PV values and EV3 ~ EV6 are percentage values.
        ratio = .01 if (v_type == 'pv' or 2 <= index <= 5) else 1
        getattr(self, v_type)[index] = float(value) * ratio
        if v_type == 'ev' and index in {0, 1}:
            self.ev[9] = self.ev[1] * 0.025 * self.ev[0]
        if v_type == 'ev' and index == 0:
            self.ev[0] = int(self.ev[0])

    def _draw_chart(self):
        self.canvas.axes.cla()  # Clear the canvas.
        self.canvas.axes.set_xlim([0, 100])
        self.canvas.axes.set_ylim([0, 25])
        self.canvas.axes.plot([self.pv[0] * 100, self.pv[2] * 100], [self.pv[1] * 100, self.pv[3] * 100], 'b')
        self.canvas.axes.annotate("(PV1, PV2)", xy=(self.pv[0] * 100, self.pv[1] * 100 - 1), color='b')
        self.canvas.axes.annotate("(PV3, PV4)", xy=(self.pv[2] * 100, self.pv[3] * 100 - 1), color='b')
        self.canvas.axes.scatter(self.pv[4] * 100, self.pv[5] * 100, color='r')
        self.canvas.axes.annotate("(PV5, PV6)", xy=(self.pv[4] * 100, self.pv[5] * 100 - 2), color='r')
        self.canvas.draw()

    def btn_start_single(self, count=10):
        if self.pv[2] < self.pv[0]:
            show_message(msg="PV3 should be larger than PV1!", msg_type="Critical")
            return
        if self.pv[3] < self.pv[1]:
            show_message(msg="PV4 should be larger than PV2!", msg_type="Critical")
            return
        self._draw_chart()
        self.ui.centralwidget.setEnabled(False)
        self.ui.statusbar.showMessage("Processing...")
        threading.Thread(target=self._start_single_process, args=(self.result_path, count,)).start()

    def _start_single_process(self, target_dir=RESULT_DIR, count=10):
        tp = TandaPaySimulator(ev=self.ev, pv=self.pv)
        tp.start_simulation(target_dir=target_dir, count=count)
        getattr(self, 'finished').emit()

    def _on_single_process_finished(self):
        self.ui.statusbar.showMessage("Finished, please check result folder!", 5000)
        self.ui.centralwidget.setEnabled(True)

    def _get_comboboxes(self):
        for i in range(8):
            if hasattr(self.ui, f"g_ev{i}"):
                yield getattr(self.ui, f"g_ev{i}"), 'ev', i
            if hasattr(self.ui, f"g_pv{i}"):
                yield getattr(self.ui, f"g_pv{i}"), 'pv', i

    def _on_group_changed(self, combo, v_type='ev', index=0, new_val='N/A'):
        self._rearrange_groups()
        layout = getattr(self.ui, f"layout_{v_type}{index}")
        for i in reversed(range(layout.count())):
            item = layout.itemAt(i)
            if item.widget() is not None:
                item.widget().setParent(None)
        for _ in range(5 - combo.currentIndex()):
            layout.addWidget(QWidget())
        for _ in range(combo.currentIndex()):
            spin = QDoubleSpinBox(parent=self)
            spin.setMaximumSize(QSize(70, 100))
            spin.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
            layout.addWidget(spin)

    def _rearrange_groups(self):
        for num in range(1, 6):
            max_count = {1: 5, 2: 3, 3: 1, 4: 3, 5: 1}[num]
            if len([c for c, _, _ in self._get_comboboxes() if c.currentText() == str(num)]) < max_count:
                for c, _, _ in self._get_comboboxes():
                    if c.model().item(num) is not None:
                        c.model().item(num).setEnabled(True)
            else:
                for c, _, _ in self._get_comboboxes():
                    if c.currentText() != str(num) and c.model().item(num) is not None:
                        c.model().item(num).setEnabled(False)

    def btn_start_matrix(self):
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
