# model.py
# Roberto Brenes
# This is the model part of the Model-View-Controller
# The class connects to a USB4000 spectrometer, acquires spectra and calculates PLQE
#
import os 
import numpy as np
import seabreeze.spectrometers as sb
from seabreeze.cseabreeze.wrapper import SeaBreezeError

class Model:
    def __init__( self ):

        self.fileName = None
        self.directory = None
        self.spec = None
        self.bckg = None
        self.LaserSpec = None
        self.INSpec = None
        self.OUTSpec = None
        self.wav = None

    def fileExists(self,directory,fileName):
        return os.path.isfile(directory+fileName)

    
    def writeFile( self, directory,fileName):
        #save a csv file with the spectra to the specified directory
        if self.LaserSpec!=None and self.INSpec!=None and OUTSpec!=None:
            pass
        else:
            pass


    def connectSpec(self):
        try:
            devices = sb.list_devices()
            self.spec = sb.Spectrometer(devices[0])
            self.wav = self.spec.wavelengths()
            return True
        except (SeaBreezeError,IndexError):
            return False

    def disconnectSpec(self):
        try:
            self.spec.close()
            return True
        except:
            return False

    def acqBckg(self,int_time, avgs):
        try:
        #Set integration time and initialize array to zero in order to average
            self.spec.integration_time_micros(int_time)
            self.bckg = np.zeros(self.spec.pixels())
            #Acquire avgs number of arrays
            for i in range(avgs):
                self.bckg += self.spec.intensities()

            self.bckg = self.bckg/avgs
            return True
        except (SeaBreezeError,AttributeError):
            return False

    def acqLaserSpec(self,int_time, avgs):
        try:
        #Set integration time and initialize array to zero in order to average
            self.spec.integration_time_micros(int_time)
            self.LaserSpec = np.zeros(self.spec.pixels())

            for i in range(avgs):
                self.LaserSpec += self.spec.intensities()

            if self.bckg != None:
                self.LaserSpec = self.LaserSpec/avgs - self.bckg
            else:
                self.LaserSpec = self.LaserSpec/avgs
            return True
        except (SeaBreezeError,AttributeError):
            return False

    def acqINSpec(self,int_time, avgs):
        try:
        #Set integration time and initialize array to zero in order to average
            self.spec.integration_time_micros(int_time)
            self.INSpec = np.zeros(self.spec.pixels())

            for i in range(avgs):
                self.INSpec += self.spec.intensities()
            if self.bckg != None:
                self.INSpec = self.INSpec/avgs - self.bckg
            else:
                self.INSpec = self.INSpec/avgs
            return True
        except (SeaBreezeError,AttributeError):
            return False

    def acqOUTSpec(self,int_time, avgs):
        try:
        #Set integration time and initialize array to zero in order to average
            self.spec.integration_time_micros(int_time)
            self.OUTSpec = np.zeros(self.spec.pixels())

            for i in range(avgs):
                self.OUTSpec += self.spec.intensities()

            if self.bckg != None:
                self.OUTSpec = self.OUTSpec/avgs - self.bckg
            else:
                self.OUTSpec =  self.OUTSpec/avgs


            return True
        except (SeaBreezeError,AttributeError):
            return False

    def calcPLQE(self,minX_Laser,maxX_Laser,minX_PL,maxX_PL):
        pass

