# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg

class Ui_MainWindow(QObject):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.folderDisplay = QtWidgets.QLineEdit(self.centralwidget)
        self.folderDisplay.setEnabled(False)
        self.folderDisplay.setAutoFillBackground(False)
        self.folderDisplay.setReadOnly(True)
        self.folderDisplay.setObjectName("folderDisplay")
        self.gridLayout.addWidget(self.folderDisplay, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.browseButton = QtWidgets.QPushButton(self.centralwidget)
        self.browseButton.setObjectName("browseButton")
        self.gridLayout.addWidget(self.browseButton, 0, 2, 1, 1)
        self.filenameDisplay = QtWidgets.QLineEdit(self.centralwidget)
        self.filenameDisplay.setObjectName("filenameDisplay")
        self.gridLayout.addWidget(self.filenameDisplay, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 4, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.acqINButton = QtWidgets.QPushButton(self.centralwidget)
        self.acqINButton.setObjectName("acqINButton")
        self.horizontalLayout.addWidget(self.acqINButton)
        self.acqOUTButton = QtWidgets.QPushButton(self.centralwidget)
        self.acqOUTButton.setObjectName("acqOUTButton")
        self.horizontalLayout.addWidget(self.acqOUTButton)
        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 4, 1, 1)
        self.debugTextBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.debugTextBrowser.sizePolicy().hasHeightForWidth())
        self.debugTextBrowser.setSizePolicy(sizePolicy)
        self.debugTextBrowser.setObjectName("debugTextBrowser")
        self.gridLayout_3.addWidget(self.debugTextBrowser, 4, 1, 1, 4)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_3.addWidget(self.progressBar, 1, 2, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.avgsSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.avgsSpinBox.setObjectName("avgsSpinBox")
        self.gridLayout_2.addWidget(self.avgsSpinBox, 2, 1, 1, 1)
        self.intSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.intSpinBox.sizePolicy().hasHeightForWidth())
        self.intSpinBox.setSizePolicy(sizePolicy)
        self.intSpinBox.setObjectName("intSpinBox")
        self.gridLayout_2.addWidget(self.intSpinBox, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.connectBox = QtWidgets.QCheckBox(self.centralwidget)
        self.connectBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectBox.sizePolicy().hasHeightForWidth())
        self.connectBox.setSizePolicy(sizePolicy)
        self.connectBox.setCheckable(False)
        self.connectBox.setTristate(False)
        self.connectBox.setObjectName("connectBox")
        self.gridLayout_2.addWidget(self.connectBox, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.acqBckgButton = QtWidgets.QPushButton(self.centralwidget)
        self.acqBckgButton.setObjectName("acqBckgButton")
        self.horizontalLayout_2.addWidget(self.acqBckgButton)
        self.acqLaserButton = QtWidgets.QPushButton(self.centralwidget)
        self.acqLaserButton.setObjectName("acqLaserButton")
        self.horizontalLayout_2.addWidget(self.acqLaserButton)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.calcPLQEButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calcPLQEButton.sizePolicy().hasHeightForWidth())
        self.calcPLQEButton.setSizePolicy(sizePolicy)
        self.calcPLQEButton.setObjectName("calcPLQEButton")
        self.verticalLayout.addWidget(self.calcPLQEButton)
        self.PLQEdisplay = QtWidgets.QLineEdit(self.centralwidget)
        self.PLQEdisplay.setEnabled(True)
        self.PLQEdisplay.setReadOnly(True)
        self.PLQEdisplay.setObjectName("PLQEdisplay")
        self.verticalLayout.addWidget(self.PLQEdisplay)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 2, 1, 2)
        self.groupBox_LaserPlot = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_LaserPlot.sizePolicy().hasHeightForWidth())
        self.groupBox_LaserPlot.setSizePolicy(sizePolicy)
        self.groupBox_LaserPlot.setObjectName("groupBox_LaserPlot")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_LaserPlot)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.gridLayout_3.addWidget(self.groupBox_LaserPlot, 3, 1, 1, 4)
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


        self.plt1 = pg.PlotWidget()
        self.plt2 = pg.PlotWidget()

        self.groupBox_LaserPlot.layout().addWidget(self.plt1,stretch=1)
        self.groupBox_LaserPlot.layout().addWidget(self.plt2,stretch=1)

        self.lb = pg.LinearRegionItem([500, 600], movable=True)
        self.rb = pg.LinearRegionItem([500, 600], movable=True)

        self.plt1.addItem(self.lb)
        self.plt2.addItem(self.rb)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.label_2.setText(_translate("MainWindow", "Filename"))
        self.label.setText(_translate("MainWindow", "Folder"))
        self.browseButton.setText(_translate("MainWindow", "Browse"))
        self.acqINButton.setText(_translate("MainWindow", "Sample in beam"))
        self.acqOUTButton.setText(_translate("MainWindow", "Sample out of beam"))
        self.label_3.setText(_translate("MainWindow", "Integration (ms)"))
        self.label_4.setText(_translate("MainWindow", "Avgs"))
        self.label_5.setText(_translate("MainWindow", "USB4000"))
        self.connectBox.setText(_translate("MainWindow", "Connect"))
        self.acqBckgButton.setText(_translate("MainWindow", "Acquire bckg"))
        self.acqLaserButton.setText(_translate("MainWindow", "Laser in"))
        self.calcPLQEButton.setText(_translate("MainWindow", "Calculate PLQE"))
        self.groupBox_LaserPlot.setTitle(_translate("MainWindow", "Laser"))

        
    def get_lbbounds(self):
        return lb.getRegion() #min_X, max_X

    def get_rbbounds(self):
        return rb.getRegion() #min_X, max_X
    
    def plotlaser(self,x,y):
        self.plt1.plot(x,y)

    def plotPL(self,x,y):
        self.plt2.plot(x,y)

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

