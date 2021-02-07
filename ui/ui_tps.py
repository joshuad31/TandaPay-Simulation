# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tps.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import ui.tps_rc

class Ui_TandaPaySimulationWindow(object):
    def setupUi(self, TandaPaySimulationWindow):
        if not TandaPaySimulationWindow.objectName():
            TandaPaySimulationWindow.setObjectName(u"TandaPaySimulationWindow")
        TandaPaySimulationWindow.resize(800, 600)
        self.centralwidget = QWidget(TandaPaySimulationWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        TandaPaySimulationWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(TandaPaySimulationWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        TandaPaySimulationWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(TandaPaySimulationWindow)
        self.statusbar.setObjectName(u"statusbar")
        TandaPaySimulationWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TandaPaySimulationWindow)

        QMetaObject.connectSlotsByName(TandaPaySimulationWindow)
    # setupUi

    def retranslateUi(self, TandaPaySimulationWindow):
        TandaPaySimulationWindow.setWindowTitle(QCoreApplication.translate("TandaPaySimulationWindow", u"TandaPay Simulation", None))
    # retranslateUi

