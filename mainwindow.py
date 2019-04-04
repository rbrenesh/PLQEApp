# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot


class Ui_MainWindow(QObject):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.debugTextBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.debugTextBrowser.setGeometry(QtCore.QRect(105, 501, 561, 51))
        self.debugTextBrowser.setObjectName("debugTextBrowser")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(500, 10, 301, 71))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.folderDisplay = QtWidgets.QLineEdit(self.layoutWidget)
        self.folderDisplay.setEnabled(False)
        self.folderDisplay.setAutoFillBackground(False)
        self.folderDisplay.setReadOnly(True)
        self.folderDisplay.setObjectName("folderDisplay")
        self.gridLayout.addWidget(self.folderDisplay, 0, 1, 1, 1)
        self.browseButton = QtWidgets.QPushButton(self.layoutWidget)
        self.browseButton.setObjectName("browseButton")
        self.gridLayout.addWidget(self.browseButton, 0, 2, 1, 1)
        self.saveButton = QtWidgets.QPushButton(self.layoutWidget)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.filenameDisplay = QtWidgets.QLineEdit(self.layoutWidget)
        self.filenameDisplay.setObjectName("filenameDisplay")
        self.gridLayout.addWidget(self.filenameDisplay, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(40, 470, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.groupBox_LaserPlot = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_LaserPlot.setGeometry(QtCore.QRect(20, 140, 371, 331))
        self.groupBox_LaserPlot.setObjectName("groupBox_LaserPlot")
        self.groupBox_PLPlot = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_PLPlot.setGeometry(QtCore.QRect(410, 140, 371, 331))
        self.groupBox_PLPlot.setObjectName("groupBox_PLPlot")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(460, 110, 298, 32))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.acqINButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.acqINButton.setObjectName("acqINButton")
        self.horizontalLayout.addWidget(self.acqINButton)
        self.acqOUTButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.acqOUTButton.setObjectName("acqOUTButton")
        self.horizontalLayout.addWidget(self.acqOUTButton)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(100, 110, 209, 32))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.acqBckgButton = QtWidgets.QPushButton(self.layoutWidget2)
        self.acqBckgButton.setObjectName("acqBckgButton")
        self.horizontalLayout_2.addWidget(self.acqBckgButton)
        self.acqLaserButton = QtWidgets.QPushButton(self.layoutWidget2)
        self.acqLaserButton.setObjectName("acqLaserButton")
        self.horizontalLayout_2.addWidget(self.acqLaserButton)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(320, 10, 132, 81))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.calcPLQEButton = QtWidgets.QPushButton(self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calcPLQEButton.sizePolicy().hasHeightForWidth())
        self.calcPLQEButton.setSizePolicy(sizePolicy)
        self.calcPLQEButton.setObjectName("calcPLQEButton")
        self.verticalLayout.addWidget(self.calcPLQEButton)
        self.PLQEdisplay = QtWidgets.QLineEdit(self.layoutWidget3)
        self.PLQEdisplay.setEnabled(True)
        self.PLQEdisplay.setReadOnly(True)
        self.PLQEdisplay.setObjectName("PLQEdisplay")
        self.verticalLayout.addWidget(self.PLQEdisplay)
        self.layoutWidget4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget4.setGeometry(QtCore.QRect(50, 10, 201, 81))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget4)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.avgsSpinBox = QtWidgets.QSpinBox(self.layoutWidget4)
        self.avgsSpinBox.setObjectName("avgsSpinBox")
        self.gridLayout_2.addWidget(self.avgsSpinBox, 2, 1, 1, 1)
        self.intSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget4)
        self.intSpinBox.setObjectName("intSpinBox")
        self.gridLayout_2.addWidget(self.intSpinBox, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.connectBox = QtWidgets.QCheckBox(self.layoutWidget4)
        self.connectBox.setEnabled(True)
        self.connectBox.setCheckable(False)
        self.connectBox.setTristate(False)
        self.connectBox.setObjectName("connectBox")
        self.gridLayout_2.addWidget(self.connectBox, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.browseButton.clicked.connect(self.browseSlot)
        self.acqBckgButton.clicked.connect(self.acquireBckgSlot)
        self.acqLaserButton.clicked.connect(self.acquireLaserSlot)
        self.calcPLQEButton.clicked.connect(self.calcPLQESlot)
        self.saveButton.clicked.connect(self.savefileSlot)
        self.acqINButton.clicked.connect(self.acquireINSlot)
        self.acqOUTButton.clicked.connect(self.acquireOUTSlot)
        self.connectBox.toggled['bool'].connect(self.connectSpecSlot)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.browseButton.setText(_translate("MainWindow", "Browse"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.label.setText(_translate("MainWindow", "Folder"))
        self.label_2.setText(_translate("MainWindow", "Filename"))
        self.groupBox_LaserPlot.setTitle(_translate("MainWindow", "Laser"))
        self.groupBox_PLPlot.setTitle(_translate("MainWindow", "PL"))
        self.acqINButton.setText(_translate("MainWindow", "Sample in beam"))
        self.acqOUTButton.setText(_translate("MainWindow", "Sample out of beam"))
        self.acqBckgButton.setText(_translate("MainWindow", "Acquire bckg"))
        self.acqLaserButton.setText(_translate("MainWindow", "Laser in"))
        self.calcPLQEButton.setText(_translate("MainWindow", "Calculate PLQE"))
        self.label_3.setText(_translate("MainWindow", "Integration (ms)"))
        self.label_4.setText(_translate("MainWindow", "Avgs"))
        self.label_5.setText(_translate("MainWindow", "USB4000"))
        self.connectBox.setText(_translate("MainWindow", "Connect"))

    @pyqtSlot( )
    def browseSlot( self ):
        pass

    @pyqtSlot( )
    def acquireBckgSlot( self ):
        pass

    @pyqtSlot( )
    def acquireINSlot( self ):
        pass

    @pyqtSlot( )
    def acquireOUTSlot( self ):
        pass

    @pyqtSlot( )
    def acquireLaserSlot( self ):
        pass

    @pyqtSlot( )
    def calcPLQESlot( self ):
        pass

    @pyqtSlot( )
    def savefileSlot( self ):
        pass

    @pyqtSlot( )
    def connectSpecSlot( self ,bool):
        pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

