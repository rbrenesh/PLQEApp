# PLQEApp.py
# Roberto Brenes
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from mainwindow import Ui_MainWindow
from model import Model, NoSpectraToProcess
from seabreeze.cseabreeze.wrapper import SeaBreezeError
import sys

class MainWindowUIClass( Ui_MainWindow ):
    def __init__( self ):
        '''Initialize the super class
        '''
        super().__init__()
        self.dir_ = None
        self.fileName = None
        self.model = Model()
        self._toggle = False
        
    def setupUi( self, MW ):
        ''' Setup the UI of the super class, and add here code
        that relates to the way we want our UI to operate.
        '''
        super().setupUi( MW )
        self.connectBox.clicked.connect(self.toggle)

        # close the lower part of the splitter to hide the 
        # debug window under normal operations
        # self.splitter.setSizes([300, 0])

    def debugPrint( self, msg ):
        '''Print the message in the text edit at the bottom of the
        horizontal splitter.
        '''
        self.debugTextBrowser.append( msg )


    #a toggle function to keep track if the spectrometer has been connected
    @pyqtSlot()
    def toggle(self):
        self._toggle = not self._toggle
        self.connectBox.setChecked(self._toggle)

        if self._toggle:
            self.connectSpecSlot()
        else:
            self.disconnectSpecSlot()


    # @pyqtSlot( )
    # def checkBoxState(self):
        # if self.connectBox.isChecked()==True:
            # self.connectSpecSlot()
        # else:
            # self.disconnectSpecSlot()

    # slot
    def calcPLQESlot( self ):
        ''' Called when the user enters a string in the line edit and
        presses the ENTER key.
        '''
        try:
            if self.model.connected:

                self.res = self.model.calcPLQE(self.get_lbbounds(),self.get_rbbounds())
                # self.PLQEdisplay.setvalue(self.res[0])
                if self.res[1]:
                    self.PLQEdisplay.setText(str(self.res[0]))
                else:
                    self.PLQEerrorDialog()
            else:
                self.noSpecDialog()
        except (SeaBreezeError,AttributeError):
            self.noSpecDialog()
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
            self.plotlaser(self.model.wav,self.model.LaserSpec)
        # self.debugPrint( "Acquire Laser button pressed" )
    # slot
    def browseSlot( self ):
        ''' Called when the user presses the Browse button
        '''
        if 'win' in sys.platform:
            self.dir_ = QtGui.QFileDialog.getExistingDirectory(None, 'Select a folder:', 'C:\\', QtGui.QFileDialog.ShowDirsOnly)
        else:
            self.dir_ = QtGui.QFileDialog.getExistingDirectory(None, 'Select a folder:', '/', QtGui.QFileDialog.ShowDirsOnly)

        self.folderDisplay.setText(self.dir_)
        # self.debugPrint(self.dir_)

    def acquireOUTSlot( self ):
        success = self.model.acqOUTSpec(self.intSpinBox.value(), self.avgsSpinBox.value())
        if success == False:
            self.noSpecDialog()
        else:
            self.plotOUTPL(self.model.wav,self.model.OUTSpec)
        # self.debugPrint("Acquire Out button pressed")

    def acquireINSlot( self ):
        success = self.model.acqINSpec(self.intSpinBox.value(), self.avgsSpinBox.value())
        if success == False:
            self.noSpecDialog()
        else:
            self.plotINPL(self.model.wav,self.model.INSpec)
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