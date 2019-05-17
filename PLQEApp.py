# PLQEApp.py
# Roberto Brenes
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
import pyqtgraph as pg
from mainwindow import Ui_MainWindow
from model import Model, NoSpectraToProcess, NoSignal
from seabreeze.cseabreeze.wrapper import SeaBreezeError
import os, sys

class MainWindowUIClass(QtWidgets.QMainWindow,Ui_MainWindow ):
    def __init__( self ):
        '''Initialize the super class
        '''
        super().__init__()
        # super(MainWindowUIClass, self).__init__(parent)
        self.dir_ = None
        self.calibdir = None
        self.fileName = None
        self.model = Model()
        self._toggle = False
        self.setupUi(self)

    def setupUi( self, MW ):
        ''' Setup the UI of the super class, and add here code
        that relates to the way we want our UI to operate.
        '''
        super().setupUi( MW )
        self.connectBox.clicked.connect(self.toggle)
        self.avgsSpinBox.setRange(0,100000)
        self.avgsSpinBox.setMinimum(1)
        self.intSpinBox.setValue(100)
        self.intSpinBox.setRange(3.8,10000)
        self.intSpinBox.setDecimals(1)
        self.laserthresh.setValue(4.5)
        self.INPLthresh.setValue(4.0)
        self.OUTPLthresh.setValue(4.0)
        self.pushButton.clicked.connect(self.sigDetectSlot)

        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')

        self.plt1 = pg.PlotWidget()
        self.plt2 = pg.PlotWidget()

        self.legend1 = self.plt1.addLegend()
        self.legend1.anchor((0,0), (0,0))
        self.legend2 = self.plt2.addLegend()
        self.legend2.anchor((0,0), (0,0))

        self.groupBox_LaserPlot.layout().addWidget(self.plt1,stretch=1)
        self.groupBox_LaserPlot.layout().addWidget(self.plt2,stretch=1)

        self.lb = pg.LinearRegionItem([500, 600], movable=True)
        self.rb = pg.LinearRegionItem([500, 600], movable=True)

        self.plt1.addItem(self.lb)
        self.plt2.addItem(self.rb)

        #check if system is running Windows to see which filepath format we need
        if 'nt' == os.name:
            self.calibdir = 'C:\\Users\\TCSPC\\Documents\\Calibration Files\\Intensity_Calibration_1000umFiber.txt'
            self.dir_ = 'C:\\'
            self.calibFileDisp.setText(self.calibdir)
        else:
            self.calibdir = '/Users/robertobrenes/Dropbox (MIT)/Roberto/Integrating Sphere Calibration/Intensity_Calibration_1umFiber.txt'
            self.dir_ = '/'
            self.calibFileDisp.setText(self.calibdir)
        # self.calibBrowseButton.clicked.connect(self.calibBrowseSlot)
        # self.connectBox.clicked.connect(self.toggle)

        # close the lower part of the splitter to hide the
        # debug window under normal operations
        # self.splitter.setSizes([300, 0])

    # def debugPrint( self, msg ):
    #     '''Print the message in the text edit at the bottom of the
    #     horizontal splitter.
    #     '''
    #     self.debugTextBrowser.append( msg )


    #a toggle function to keep track if the spectrometer has been connected
    @pyqtSlot()
    def toggle(self):
        self._toggle = not self._toggle
        self.connectBox.setChecked(self._toggle)

        if self._toggle:
            self.connectSpecSlot()
        else:
            self.disconnectSpecSlot()


    @pyqtSlot()
    def sigDetectSlot(self):
        try:
            laserx,lasery,plx,ply,_,_ = self.model.detect_signal(self.get_lbbounds(),self.get_rbbounds(),self.calibdir,self.INPLthresh.value(),self.OUTPLthresh.value(),self.laserthresh.value())
            self.plotlaserdetect(laserx,lasery)
            self.plotPLdetect(plx,ply)
        except NoSpectraToProcess:
            self.PLQEerrorDialog()


    # @pyqtSlot( )
    # def checkBoxState(self):
        # if self.connectBox.isChecked()==True:
            # self.connectSpecSlot()
        # else:
            # self.disconnectSpecSlot()

    # slot
    @pyqtSlot()
    def calcPLQESlot( self ):
        ''' Called when the user enters a string in the line edit and
        presses the ENTER key.
        '''
        try:
            if self.model.connected:

                self.res = self.model.calcPLQE(self.get_lbbounds(),self.get_rbbounds(),self.calibdir)
                # self.PLQEdisplay.setvalue(self.res[0])
                if self.res[1]:
                    self.PLQEdisplay.setText(str(self.res[0]))
                else:
                    self.PLQEerrorDialog()
            else:
                self.noSpecDialog()
        except (SeaBreezeError,AttributeError):
            self.noSpecDialog()

        except (TypeError, NoSignal):
            self.DetecterrorDialog()

            # self.debugPrint(str(self.res[0]))

        # self.debugPrint( "Calc PLQE key pressed" )

    # slot
    def savefileSlot( self ):
        ''' Called when the user presses the save button.
        '''
        self.fileName = self.filenameDisplay.text()

        #Check to see if file exists and prompt the user to overwrite or not
        # try:
        if self.fileName=='':

            self.NameFileDialog()
        else:

            if self.model.fileExists(self.dir_,self.fileName):

                reply = self.OverWriteDialog()

                if reply == QtGui.QMessageBox.Yes:
                    try:
                        self.model.writeFile(self.dir_,self.fileName)
                    except NoSpectraToProcess:
                        self.PLQEerrorDialog()

            else:
                try:
                    self.model.writeFile(self.dir_,self.fileName)
                except NoSpectraToProcess:
                    self.PLQEerrorDialog()
        # except TypeError:
            # self.PLQEerrorDialog()


        # self.debugPrint( "Save button pressed" )

    def acquireLaserSlot( self ):
        success = self.model.acqLaserSpec(self.intSpinBox.value(), self.avgsSpinBox.value())
        if success == False:
            self.noSpecDialog()
        else:
            self.plotlaser(self.model.wav,self.model.LaserSpec-self.model.bckg)
        # self.debugPrint( "Acquire Laser button pressed" )
    # slot
    def browseSlot( self ):
        ''' Called when the user presses the Browse button
        '''
        if 'nt' == os.name:
            tmp = QtGui.QFileDialog.getExistingDirectory(None, 'Select a folder:', self.dir_, QtGui.QFileDialog.ShowDirsOnly)
            if tmp:
                self.dir_ = tmp
        else:
            tmp = QtGui.QFileDialog.getExistingDirectory(None, 'Select a folder:', self.dir_, QtGui.QFileDialog.ShowDirsOnly)
            if tmp:
                self.dir_ = tmp

        self.folderDisplay.setText(self.dir_)


    def calibBrowseSlot( self ):
        ''' Called when the user presses the Browse button
        '''
        if 'nt' == os.name:
            #returns a tuple, where the first is the filepath string and the second the file format options string, so we just select the first
            tmp = QtGui.QFileDialog.getOpenFileName(None, 'Select a calibration file:', self.calibdir, "Calibration Files (*.txt)")[0]
            if tmp:
                self.calibdir =  tmp
            # print(self.calibdir)
        else:
            # print(self.calibdir)
            tmp = QtGui.QFileDialog.getOpenFileName(None, 'Select a calibration file:', self.calibdir, "Calibration Files (*.txt)")[0]
            if tmp:
                self.calibdir = tmp
            # print(self.calibdir)

        self.calibFileDisp.setText(self.calibdir)
        # self.debugPrint(self.dir_)

    def acquireOUTSlot( self ):
        success = self.model.acqOUTSpec(self.intSpinBox.value(), self.avgsSpinBox.value())
        if success == False:
            self.noSpecDialog()
        else:
            self.plotOUTPL(self.model.wav,self.model.OUTSpec-self.model.bckg)
        # self.debugPrint("Acquire Out button pressed")

    def acquireINSlot( self ):
        success = self.model.acqINSpec(self.intSpinBox.value(), self.avgsSpinBox.value())
        if success == False:
            self.noSpecDialog()
        else:
            self.plotINPL(self.model.wav,self.model.INSpec-self.model.bckg)
        # self.debugPrint("Acquire In button pressed")

    def acquireBckgSlot( self ):
        success = self.model.acqBckg(self.intSpinBox.value(), self.avgsSpinBox.value())
        if success == False:
            self.noSpecDialog()
        # self.debugPrint("Acquire background button pressed")

    def connectSpecSlot( self ):
        success = self.model.connectSpec()
        # self.debugPrint(str(success))
        if success == False:
            self.connectBox.setChecked(False)
            self._toggle= False
            self.connectionErrorDialog()
        # self.debugPrint("connectSpecSlot Checked")

    def disconnectSpecSlot( self ):
        success = self.model.disconnectSpec()

        # self.debugPrint("connectSpecSlot Unchecked")

    def connectionErrorDialog(self):

        error_dialog = QtGui.QMessageBox()
        error_dialog.setIcon(QtGui.QMessageBox.Critical)
        error_dialog.setText('USB4000 Connection Failed')
        error_dialog.setWindowTitle('Error')
        error_dialog.exec_()

    def noSpecDialog(self):
        error_dialog = QtGui.QMessageBox()
        error_dialog.setIcon(QtGui.QMessageBox.Critical)
        error_dialog.setText('No spectrometer connected')
        error_dialog.setWindowTitle('Error')
        error_dialog.exec_()

    def PLQEerrorDialog(self):
        error_dialog = QtGui.QMessageBox()
        error_dialog.setIcon(QtGui.QMessageBox.Critical)
        error_dialog.setText('Please acquire all spectra first')
        error_dialog.setWindowTitle('Error')
        error_dialog.exec_()

    def DetecterrorDialog(self):
        error_dialog = QtGui.QMessageBox()
        error_dialog.setIcon(QtGui.QMessageBox.Critical)
        error_dialog.setText('No signal detected')
        error_dialog.setWindowTitle('Error')
        error_dialog.exec_()

    def NameFileDialog(self):
        error_dialog = QtGui.QMessageBox()
        error_dialog.setIcon(QtGui.QMessageBox.Critical)
        error_dialog.setText('Please name your file')
        error_dialog.setWindowTitle('Error')
        error_dialog.exec_()

    def OverWriteDialog(self):
        ovrwrite_msg = "File already exists. Overwrite?"
        error = QtGui.QMessageBox()
        reply = error.question(error,'Message', ovrwrite_msg, error.No, error.Yes)

        return reply

    def get_lbbounds(self):
        return self.lb.getRegion() #min_X, max_X

    def get_rbbounds(self):
        return self.rb.getRegion() #min_X, max_X

    def plotlaser(self,x,y):
        try:
            self.laser.clear()
            self.legend1.removeItem(self.laser.name())
        except AttributeError:
            pass
        self.laser = self.plt1.plot(x,y,name="Laser",pen='k')



    def plotlaserdetect(self,x,y):
        try:
            self.laserdetect.clear()
            self.legend1.removeItem(self.laserdetect.name())
        except AttributeError:
            pass
        self.laserdetect = self.plt1.plot(x,y,name="LaserDetect",pen='r')

    def plotPLdetect(self,x,y):
        try:
            self.PLdetect.clear()
            self.legend2.removeItem(self.PLdetect.name())
        except AttributeError:
            pass
        self.PLdetect = self.plt2.plot(x,y,name="PLDetect",pen='k')

    def plotINPL(self,x,y):
        try:
            self.IN.clear()
            self.legend2.removeItem(self.IN.name())
        except AttributeError:
            pass
        self.IN = self.plt2.plot(x,y,name='IN',pen='r')

    def plotOUTPL(self,x,y):
        try:
            self.OUT.clear()
            self.legend2.removeItem(self.OUT.name())
        except AttributeError:
            pass
        self.OUT = self.plt2.plot(x,y,name='OUT',pen='b')

def AppExec(app,ui):
    app.exec_()

    #handle the spectrometer disconnect here
    ui.model.disconnectSpec()

    # print("you just closed the pyqt window!!! you are awesome!!!")

def main():
    """
    This is the MAIN ENTRY POINT of our application.  The code at the end
    of the mainwindow.py script will not be executed, since this script is now
    our main program.   We have simply copied the code from mainwindow.py here
    since it was automatically generated by '''pyuic5'''.

    """
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowUIClass()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(AppExec(app,ui))
    # sys.exit(app.exec_())

main()
