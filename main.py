import sys
import qdarkstyle
from PySide2.QtWidgets import QMainWindow, QApplication

from ui.ui_tps import Ui_TandaPaySimulationWindow
from utils.logger import logger


class TandaPaySimulationApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_TandaPaySimulationWindow()
        self.ui.setupUi(self)


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
