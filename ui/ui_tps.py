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
        TandaPaySimulationWindow.resize(946, 528)
        font = QFont()
        font.setPointSize(12)
        TandaPaySimulationWindow.setFont(font)
        self.centralwidget = QWidget(TandaPaySimulationWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(200, 0))

        self.horizontalLayout.addWidget(self.label)

        self.system_database = QLineEdit(self.centralwidget)
        self.system_database.setObjectName(u"system_database")
        self.system_database.setReadOnly(True)

        self.horizontalLayout.addWidget(self.system_database)

        self.btn_system_database = QToolButton(self.centralwidget)
        self.btn_system_database.setObjectName(u"btn_system_database")
        icon = QIcon()
        icon.addFile(u":/img/img/Open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_system_database.setIcon(icon)
        self.btn_system_database.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_system_database)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.user_database = QLineEdit(self.centralwidget)
        self.user_database.setObjectName(u"user_database")
        self.user_database.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.user_database)

        self.btn_user_database = QToolButton(self.centralwidget)
        self.btn_user_database.setObjectName(u"btn_user_database")
        self.btn_user_database.setIcon(icon)
        self.btn_user_database.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.btn_user_database)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.matrix_database = QLineEdit(self.centralwidget)
        self.matrix_database.setObjectName(u"matrix_database")
        self.matrix_database.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.matrix_database)

        self.btn_matrix_database = QToolButton(self.centralwidget)
        self.btn_matrix_database.setObjectName(u"btn_matrix_database")
        self.btn_matrix_database.setIcon(icon)
        self.btn_matrix_database.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.btn_matrix_database)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setSpacing(30)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(30)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.ev_0 = QSpinBox(self.groupBox)
        self.ev_0.setObjectName(u"ev_0")
        self.ev_0.setMinimumSize(QSize(70, 0))
        self.ev_0.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ev_0.setMinimum(4)
        self.ev_0.setMaximum(9999)

        self.horizontalLayout_5.addWidget(self.ev_0)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.ev_1 = QSpinBox(self.groupBox)
        self.ev_1.setObjectName(u"ev_1")
        self.ev_1.setMinimumSize(QSize(70, 0))
        self.ev_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ev_1.setMinimum(4)
        self.ev_1.setMaximum(9999)

        self.horizontalLayout_6.addWidget(self.ev_1)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.ev_2 = QSpinBox(self.groupBox)
        self.ev_2.setObjectName(u"ev_2")
        self.ev_2.setMinimumSize(QSize(70, 0))
        self.ev_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ev_2.setMinimum(25)
        self.ev_2.setMaximum(75)

        self.horizontalLayout_7.addWidget(self.ev_2)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(30)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_8.addWidget(self.label_7)

        self.ev_3 = QSpinBox(self.groupBox)
        self.ev_3.setObjectName(u"ev_3")
        self.ev_3.setMinimumSize(QSize(70, 0))
        self.ev_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ev_3.setMinimum(10)
        self.ev_3.setMaximum(30)

        self.horizontalLayout_8.addWidget(self.ev_3)


        self.horizontalLayout_15.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_9.addWidget(self.label_8)

        self.ev_4 = QSpinBox(self.groupBox)
        self.ev_4.setObjectName(u"ev_4")
        self.ev_4.setMinimumSize(QSize(70, 0))
        self.ev_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ev_4.setMinimum(10)
        self.ev_4.setMaximum(30)

        self.horizontalLayout_9.addWidget(self.ev_4)


        self.horizontalLayout_15.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_10.addWidget(self.label_9)

        self.ev_5 = QSpinBox(self.groupBox)
        self.ev_5.setObjectName(u"ev_5")
        self.ev_5.setMinimumSize(QSize(70, 0))
        self.ev_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ev_5.setMinimum(20)
        self.ev_5.setMaximum(80)

        self.horizontalLayout_10.addWidget(self.ev_5)


        self.horizontalLayout_15.addLayout(self.horizontalLayout_10)


        self.verticalLayout_2.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(30)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_11.addWidget(self.label_10)

        self.ev_6 = QSpinBox(self.groupBox)
        self.ev_6.setObjectName(u"ev_6")
        self.ev_6.setMinimumSize(QSize(70, 0))
        self.ev_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ev_6.setMinimum(2)
        self.ev_6.setMaximum(4)

        self.horizontalLayout_11.addWidget(self.ev_6)


        self.horizontalLayout_16.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_12.addWidget(self.label_11)

        self.ev_7 = QSpinBox(self.groupBox)
        self.ev_7.setObjectName(u"ev_7")
        self.ev_7.setMinimumSize(QSize(70, 0))
        self.ev_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ev_7.setMinimum(0)
        self.ev_7.setMaximum(3)

        self.horizontalLayout_12.addWidget(self.ev_7)


        self.horizontalLayout_16.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_13.addWidget(self.label_12)

        self.ev_8 = QSpinBox(self.groupBox)
        self.ev_8.setObjectName(u"ev_8")
        self.ev_8.setMinimumSize(QSize(70, 0))
        self.ev_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ev_8.setMinimum(4)
        self.ev_8.setMaximum(9999)

        self.horizontalLayout_13.addWidget(self.ev_8)


        self.horizontalLayout_16.addLayout(self.horizontalLayout_13)


        self.verticalLayout_2.addLayout(self.horizontalLayout_16)


        self.horizontalLayout_4.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setSpacing(30)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(30)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_18.addWidget(self.label_13)

        self.pv_0 = QSpinBox(self.groupBox_2)
        self.pv_0.setObjectName(u"pv_0")
        self.pv_0.setMinimumSize(QSize(70, 0))
        self.pv_0.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pv_0.setMinimum(1)
        self.pv_0.setMaximum(100)

        self.horizontalLayout_18.addWidget(self.pv_0)


        self.horizontalLayout_17.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_14 = QLabel(self.groupBox_2)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_19.addWidget(self.label_14)

        self.pv_1 = QSpinBox(self.groupBox_2)
        self.pv_1.setObjectName(u"pv_1")
        self.pv_1.setMinimumSize(QSize(70, 0))
        self.pv_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pv_1.setMinimum(1)
        self.pv_1.setMaximum(100)

        self.horizontalLayout_19.addWidget(self.pv_1)


        self.horizontalLayout_17.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_20.addWidget(self.label_15)

        self.pv_2 = QSpinBox(self.groupBox_2)
        self.pv_2.setObjectName(u"pv_2")
        self.pv_2.setMinimumSize(QSize(70, 0))
        self.pv_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pv_2.setMinimum(0)
        self.pv_2.setMaximum(9999)

        self.horizontalLayout_20.addWidget(self.pv_2)


        self.horizontalLayout_17.addLayout(self.horizontalLayout_20)


        self.verticalLayout_3.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setSpacing(30)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_16 = QLabel(self.groupBox_2)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_22.addWidget(self.label_16)

        self.pv_3 = QSpinBox(self.groupBox_2)
        self.pv_3.setObjectName(u"pv_3")
        self.pv_3.setMinimumSize(QSize(70, 0))
        self.pv_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pv_3.setMinimum(0)
        self.pv_3.setMaximum(9999)

        self.horizontalLayout_22.addWidget(self.pv_3)


        self.horizontalLayout_21.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_17 = QLabel(self.groupBox_2)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_23.addWidget(self.label_17)

        self.pv_4 = QSpinBox(self.groupBox_2)
        self.pv_4.setObjectName(u"pv_4")
        self.pv_4.setMinimumSize(QSize(70, 0))
        self.pv_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pv_4.setMinimum(0)
        self.pv_4.setMaximum(9999)

        self.horizontalLayout_23.addWidget(self.pv_4)


        self.horizontalLayout_21.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_18 = QLabel(self.groupBox_2)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_24.addWidget(self.label_18)

        self.pv_5 = QSpinBox(self.groupBox_2)
        self.pv_5.setObjectName(u"pv_5")
        self.pv_5.setMinimumSize(QSize(70, 0))
        self.pv_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pv_5.setMinimum(0)
        self.pv_5.setMaximum(9999)

        self.horizontalLayout_24.addWidget(self.pv_5)


        self.horizontalLayout_21.addLayout(self.horizontalLayout_24)


        self.verticalLayout_3.addLayout(self.horizontalLayout_21)

        self.verticalSpacer = QSpacerItem(20, 29, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_4.addWidget(self.groupBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_25 = QHBoxLayout(self.widget)
        self.horizontalLayout_25.setSpacing(30)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(323, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer)

        self.btn_start = QPushButton(self.widget)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_25.addWidget(self.btn_start)

        self.btn_clear = QPushButton(self.widget)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_25.addWidget(self.btn_clear)

        self.btn_exit = QPushButton(self.widget)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_25.addWidget(self.btn_exit)

        self.horizontalSpacer_2 = QSpacerItem(323, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.widget)

        TandaPaySimulationWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(TandaPaySimulationWindow)
        self.statusbar.setObjectName(u"statusbar")
        TandaPaySimulationWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TandaPaySimulationWindow)

        QMetaObject.connectSlotsByName(TandaPaySimulationWindow)
    # setupUi

    def retranslateUi(self, TandaPaySimulationWindow):
        TandaPaySimulationWindow.setWindowTitle(QCoreApplication.translate("TandaPaySimulationWindow", u"TandaPay Simulation", None))
        self.label.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"System Database File:", None))
        self.btn_system_database.setText("")
        self.label_2.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"User Database File:", None))
        self.btn_user_database.setText("")
        self.label_3.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"Matrix Database File:", None))
        self.btn_matrix_database.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("TandaPaySimulationWindow", u"EV", None))
        self.label_4.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"EV 1", None))
        self.label_5.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"EV 2", None))
        self.label_6.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"EV 3", None))
        self.label_7.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"EV 4", None))
        self.label_8.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"EV 5", None))
        self.label_9.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"EV 6", None))
        self.label_10.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"EV 7", None))
        self.label_11.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"EV 8", None))
        self.label_12.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"EV 9", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("TandaPaySimulationWindow", u"PV", None))
        self.label_13.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"PV 1", None))
        self.label_14.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"PV 2", None))
        self.label_15.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"PV 3", None))
        self.label_16.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"PV 4", None))
        self.label_17.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"PV 5", None))
        self.label_18.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"PV 6", None))
        self.btn_start.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"Start", None))
        self.btn_clear.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"Clear", None))
        self.btn_exit.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"Exit", None))
    # retranslateUi

