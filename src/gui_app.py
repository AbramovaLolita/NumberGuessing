# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_app.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGroupBox, QHeaderView,
    QLCDNumber, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolBar,
    QVBoxLayout, QWidget,QButtonGroup)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(463, 599)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.Game = QWidget()
        self.Game.setObjectName(u"Game")
        self.lbl_feedback = QLabel(self.Game)
        self.lbl_feedback.setObjectName(u"lbl_feedback")
        self.lbl_feedback.setGeometry(QRect(50, 235, 331, 71))
        self.level = QGroupBox(self.Game)
        self.level.setObjectName(u"level")
        self.level.setGeometry(QRect(9, 9, 241, 71))
        self.radioButton_10 = QRadioButton(self.level)
        self.radioButton_10.setObjectName(u"radioButton_10")
        self.radioButton_10.setGeometry(QRect(11, 27, 68, 24))
        self.radioButton_11 = QRadioButton(self.level)
        self.radioButton_11.setObjectName(u"radioButton_11")
        self.radioButton_11.setGeometry(QRect(82, 27, 81, 24))
        self.radioButton_12 = QRadioButton(self.level)
        self.radioButton_12.setObjectName(u"radioButton_12")
        self.radioButton_12.setGeometry(QRect(166, 27, 61, 24))
        self.attempts = QLCDNumber(self.Game)
        self.attempts.setObjectName(u"attempts")
        self.attempts.setGeometry(QRect(280, 20, 121, 51))
        self.attempts.setProperty(u"intValue", 10)
        self.lbl_instruction_2 = QLabel(self.Game)
        self.lbl_instruction_2.setObjectName(u"lbl_instruction_2")
        self.lbl_instruction_2.setGeometry(QRect(130, 110, 131, 31))
        self.lbl_instruction_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.list_history = QListWidget(self.Game)
        self.list_history.setObjectName(u"list_history")
        self.list_history.setGeometry(QRect(40, 320, 361, 91))
        self.input_number_2 = QLineEdit(self.Game)
        self.input_number_2.setObjectName(u"input_number_2")
        self.input_number_2.setGeometry(QRect(130, 145, 141, 31))
        self.pushButton_2 = QPushButton(self.Game)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(150, 190, 81, 26))
        self.tabWidget.addTab(self.Game, "")
        self.Rating = QWidget()
        self.Rating.setObjectName(u"Rating")
        self.verticalLayout_3 = QVBoxLayout(self.Rating)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tableWidget = QTableWidget(self.Rating)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.tableWidget.setSortingEnabled(True)

        self.verticalLayout_3.addWidget(self.tableWidget)

        self.tabWidget.addTab(self.Rating, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 463, 33))
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuRecords = QMenu(self.menubar)
        self.menuRecords.setObjectName(u"menuRecords")
        self.menuExit = QMenu(self.menubar)
        self.menuExit.setObjectName(u"menuExit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QToolBar(MainWindow)
        self.toolBar_2.setObjectName(u"toolBar_2")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar_2)

        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuRecords.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_feedback.setText("")
        self.level.setTitle(QCoreApplication.translate("MainWindow", u"Level", None))
        self.radioButton_10.setText(QCoreApplication.translate("MainWindow", u"Easy", None))
        self.radioButton_11.setText(QCoreApplication.translate("MainWindow", u"Medium", None))
        self.radioButton_12.setText(QCoreApplication.translate("MainWindow", u"Hard", None))
        self.lbl_instruction_2.setText(QCoreApplication.translate("MainWindow", u"Enter a number", None))
        self.input_number_2.setPlaceholderText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Game), QCoreApplication.translate("MainWindow", u"Game", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Record", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Rating), QCoreApplication.translate("MainWindow", u"Rating", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Log in", None))
        self.menuRecords.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuExit.setTitle(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.toolBar_2.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_2", None))
    # retranslateUi

