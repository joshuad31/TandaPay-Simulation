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
        TandaPaySimulationWindow.resize(1121, 935)
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

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(50)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.ev_0 = QSpinBox(self.groupBox)
        self.ev_0.setObjectName(u"ev_0")
        self.ev_0.setMinimumSize(QSize(70, 0))
        self.ev_0.setMaximumSize(QSize(70, 16777215))
        self.ev_0.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ev_0.setMinimum(1)
        self.ev_0.setMaximum(9999)
        self.ev_0.setValue(60)

        self.horizontalLayout_5.addWidget(self.ev_0)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.ev_1 = QSpinBox(self.groupBox)
        self.ev_1.setObjectName(u"ev_1")
        self.ev_1.setMinimumSize(QSize(70, 0))
        self.ev_1.setMaximumSize(QSize(70, 16777215))
        self.ev_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ev_1.setMinimum(4)
        self.ev_1.setMaximum(9999)
        self.ev_1.setValue(1000)

        self.horizontalLayout_6.addWidget(self.ev_1)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.ev_2 = QSpinBox(self.groupBox)
        self.ev_2.setObjectName(u"ev_2")
        self.ev_2.setMinimumSize(QSize(70, 0))
        self.ev_2.setMaximumSize(QSize(70, 16777215))
        self.ev_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ev_2.setMinimum(0)
        self.ev_2.setMaximum(100)
        self.ev_2.setValue(40)

        self.horizontalLayout_7.addWidget(self.ev_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_8.addWidget(self.label_7)

        self.ev_3 = QSpinBox(self.groupBox)
        self.ev_3.setObjectName(u"ev_3")
        self.ev_3.setMinimumSize(QSize(70, 0))
        self.ev_3.setMaximumSize(QSize(70, 16777215))
        self.ev_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ev_3.setMinimum(0)
        self.ev_3.setMaximum(100)
        self.ev_3.setValue(27)

        self.horizontalLayout_8.addWidget(self.ev_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_9.addWidget(self.label_8)

        self.ev_4 = QSpinBox(self.groupBox)
        self.ev_4.setObjectName(u"ev_4")
        self.ev_4.setMinimumSize(QSize(70, 0))
        self.ev_4.setMaximumSize(QSize(70, 16777215))
        self.ev_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ev_4.setMinimum(0)
        self.ev_4.setMaximum(100)
        self.ev_4.setValue(10)

        self.horizontalLayout_9.addWidget(self.ev_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_10.addWidget(self.label_9)

        self.ev_5 = QSpinBox(self.groupBox)
        self.ev_5.setObjectName(u"ev_5")
        self.ev_5.setMinimumSize(QSize(70, 0))
        self.ev_5.setMaximumSize(QSize(70, 16777215))
        self.ev_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ev_5.setMinimum(0)
        self.ev_5.setMaximum(100)
        self.ev_5.setValue(70)

        self.horizontalLayout_10.addWidget(self.ev_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_11.addWidget(self.label_10)

        self.ev_6 = QSpinBox(self.groupBox)
        self.ev_6.setObjectName(u"ev_6")
        self.ev_6.setMinimumSize(QSize(70, 0))
        self.ev_6.setMaximumSize(QSize(70, 16777215))
        self.ev_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ev_6.setMinimum(2)
        self.ev_6.setMaximum(4)
        self.ev_6.setValue(2)

        self.horizontalLayout_11.addWidget(self.ev_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_12.addWidget(self.label_11)

        self.ev_7 = QSpinBox(self.groupBox)
        self.ev_7.setObjectName(u"ev_7")
        self.ev_7.setMinimumSize(QSize(70, 0))
        self.ev_7.setMaximumSize(QSize(70, 16777215))
        self.ev_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ev_7.setMinimum(0)
        self.ev_7.setMaximum(3)
        self.ev_7.setValue(3)

        self.horizontalLayout_12.addWidget(self.ev_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_12)


        self.horizontalLayout_4.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_18.addWidget(self.label_13)

        self.pv_0 = QSpinBox(self.groupBox_2)
        self.pv_0.setObjectName(u"pv_0")
        self.pv_0.setMinimumSize(QSize(70, 0))
        self.pv_0.setMaximumSize(QSize(70, 16777215))
        self.pv_0.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pv_0.setMinimum(1)
        self.pv_0.setMaximum(100)
        self.pv_0.setValue(10)

        self.horizontalLayout_18.addWidget(self.pv_0)


        self.verticalLayout_3.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_14 = QLabel(self.groupBox_2)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_19.addWidget(self.label_14)

        self.pv_1 = QSpinBox(self.groupBox_2)
        self.pv_1.setObjectName(u"pv_1")
        self.pv_1.setMinimumSize(QSize(70, 0))
        self.pv_1.setMaximumSize(QSize(70, 16777215))
        self.pv_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pv_1.setMinimum(1)
        self.pv_1.setMaximum(100)
        self.pv_1.setValue(2)

        self.horizontalLayout_19.addWidget(self.pv_1)


        self.verticalLayout_3.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_20.addWidget(self.label_15)

        self.pv_2 = QSpinBox(self.groupBox_2)
        self.pv_2.setObjectName(u"pv_2")
        self.pv_2.setMinimumSize(QSize(70, 0))
        self.pv_2.setMaximumSize(QSize(70, 16777215))
        self.pv_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pv_2.setMinimum(0)
        self.pv_2.setMaximum(9999)
        self.pv_2.setValue(70)

        self.horizontalLayout_20.addWidget(self.pv_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_16 = QLabel(self.groupBox_2)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_22.addWidget(self.label_16)

        self.pv_3 = QSpinBox(self.groupBox_2)
        self.pv_3.setObjectName(u"pv_3")
        self.pv_3.setMinimumSize(QSize(70, 0))
        self.pv_3.setMaximumSize(QSize(70, 16777215))
        self.pv_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pv_3.setMinimum(0)
        self.pv_3.setMaximum(100)
        self.pv_3.setValue(8)

        self.horizontalLayout_22.addWidget(self.pv_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_17 = QLabel(self.groupBox_2)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_23.addWidget(self.label_17)

        self.pv_4 = QSpinBox(self.groupBox_2)
        self.pv_4.setObjectName(u"pv_4")
        self.pv_4.setMinimumSize(QSize(70, 0))
        self.pv_4.setMaximumSize(QSize(70, 16777215))
        self.pv_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pv_4.setMinimum(0)
        self.pv_4.setMaximum(100)
        self.pv_4.setValue(77)

        self.horizontalLayout_23.addWidget(self.pv_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_18 = QLabel(self.groupBox_2)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_24.addWidget(self.label_18)

        self.pv_5 = QSpinBox(self.groupBox_2)
        self.pv_5.setObjectName(u"pv_5")
        self.pv_5.setMinimumSize(QSize(70, 0))
        self.pv_5.setMaximumSize(QSize(70, 16777215))
        self.pv_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pv_5.setMinimum(0)
        self.pv_5.setMaximum(100)
        self.pv_5.setValue(5)

        self.horizontalLayout_24.addWidget(self.pv_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_24)

        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy1)
        self.layout_graph = QVBoxLayout(self.groupBox_3)
        self.layout_graph.setObjectName(u"layout_graph")

        self.verticalLayout_3.addWidget(self.groupBox_3)


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
        self.groupBox.setTitle(QCoreApplication.translate("TandaPaySimulationWindow", u"ENVIRONMENTAL VARIABLES", None))
        self.label_4.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"Members in group", None))
#if QT_CONFIG(tooltip)
        self.ev_0.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"How many members are in the group?", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"Average take-home pay for group members", None))
#if QT_CONFIG(tooltip)
        self.ev_1.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Average take-home pay for group members?", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"Chance of a claim each month(%)", None))
#if QT_CONFIG(tooltip)
        self.ev_2.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"What is the chance of a claim each month?", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"Honest defectors(%)", None))
#if QT_CONFIG(tooltip)
        self.ev_3.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"What is the percentage of honest defectors?", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"Low-morale members(%)", None))
#if QT_CONFIG(tooltip)
        self.ev_4.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"What is the percentage of low-morale members?", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_9.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"What is the percentage of members who are unwilling to act alone? ", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"Members who are unwilling to act alone(%)", None))
#if QT_CONFIG(tooltip)
        self.ev_5.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"What is the percentage of members who are unwilling to act alone?", None))
#endif // QT_CONFIG(tooltip)
        self.label_10.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"Member threshold for dependent members to defect", None))
#if QT_CONFIG(tooltip)
        self.ev_6.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"What is the member threshold needed for dependent members to defect?", None))
#endif // QT_CONFIG(tooltip)
        self.label_11.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"Additional periods once the group stabilizes", None))
#if QT_CONFIG(tooltip)
        self.ev_7.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Once the group stabilizes how many additional periods will there be?", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_2.setTitle(QCoreApplication.translate("TandaPaySimulationWindow", u"PRICING VARIABLES", None))
        self.label_13.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"Lower threshold of premium price", None))
#if QT_CONFIG(tooltip)
        self.pv_0.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"The premium price must exceed this minimum threshold", None))
#endif // QT_CONFIG(tooltip)
        self.label_14.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"Policyholders decide to leave before:", None))
#if QT_CONFIG(tooltip)
        self.pv_1.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Before this many policyholders decide to leave", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_15.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"The maximum premium price increase threshold", None))
#endif // QT_CONFIG(tooltip)
        self.label_15.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"Upper threshold of premium price", None))
        self.label_16.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"Policyholders deciding to leave result in(%)", None))
#if QT_CONFIG(tooltip)
        self.pv_3.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Resulting in this percentage of policyholders deciding to leave", None))
#endif // QT_CONFIG(tooltip)
        self.label_17.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"Lower threshold of premium price sensitivity(%)", None))
#if QT_CONFIG(tooltip)
        self.pv_4.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u" If the premium increases beyond this percentage", None))
#endif // QT_CONFIG(tooltip)
        self.label_18.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"Policyholders leaving every period(%)", None))
#if QT_CONFIG(tooltip)
        self.pv_5.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Then this percentage of policyholders will leave every period", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_3.setTitle(QCoreApplication.translate("TandaPaySimulationWindow", u"Pricing Graph", None))
        self.btn_start.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"Start", None))
        self.btn_exit.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"Exit", None))
    # retranslateUi

