# model.py
# Roberto Brenes
# This is the model part of the Model-View-Controller
# The class connects to a USB4000 spectrometer, acquires spectra and calculates PLQE
#
import os 
import numpy as np
import seabreeze.spectrometers as sb
from seabreeze.cseabreeze.wrapper import SeaBreezeError
from scipy.interpolate import interp1d

class NoSpectraToProcess(Exception):
    pass

class Model():
    def __init__( self ):
        self.fileName = None
        self.directory = None
        self.spec = None
        self.bckg = None
        self.LaserSpec = None
        self.INSpec = None
        self.OUTSpec = None
        self.wav = None
        self.progress= 0
        self.connected = False
        self.n = 0

    def fileExists(self,directory,fileName):
        if ".txt" not in fileName:
            savepath = directory + '/' + fileName + '.txt'
        else:
            savepath = directory + '/' + fileName
        return os.path.isfile(savepath)

    
    def writeFile( self, directory,fileName):
        #save a csv file with the spectra to the specified directory
        if type(self.LaserSpec)!=type(None) and type(self.INSpec)!=type(None) and type(self.OUTSpec)!=type(None):
            try:
                M = np.vstack((self.wav,self.LaserSpec-self.bckg,self.INSpec-self.bckg,self.OUTSpec-self.bckg)).T
            except TypeError:
                M = np.vstack((self.wav,self.LaserSpec,self.INSpec,self.OUTSpec)).T

            if ".txt" not in fileName:
                savepath = directory + '/' + fileName + '.txt'
            else:
                savepath = directory + '/' + fileName

            np.savetxt(savepath,M,header= 'PLQE = {0:.1f} \n Wavelength(nm) Laser(counts) InBeam(counts) OutofBeam(counts)'.format(self.n))
        else:
            raise NoSpectraToProcess('Please acquire all spectra')


    def connectSpec(self):
        try:
            devices = sb.list_devices()
            self.spec = sb.Spectrometer(devices[0])
            self.wav = self.spec.wavelengths()
            self.connected = True
            return True
        except (SeaBreezeError,IndexError):
            self.connected = False
            return False

    def disconnectSpec(self):
        try:
            self.spec.close()
            self.connected = False
            return True
        except:
            self.connected = True
            return False

    def acqBckg(self,int_time, avgs):
        try:
        #Set integration time and initialize array to zero in order to average
            self.spec.integration_time_micros(int_time)
            self.bckg = np.zeros(self.spec.pixels)
            #Acquire avgs number of arrays
            for i in range(avgs):
                self.bckg += self.spec.intensities()

            self.bckg = self.bckg/avgs
            return True
        except (SeaBreezeError,AttributeError):
            return False

    def acqLaserSpec(self,int_time, avgs):

        dirname = os.path.dirname(__file__)
        file_path = os.path.join(dirname, 'Intensity_Calibration.txt')
        calibration = np.genfromtxt(file_path,skip_header=1)
        wav_calib = calibration[:,0]
        int_calib = calibration[:,1]
        calib_factor = interp1d(wav_calib,int_calib)
        try:
        #Set integration time and initialize array to zero in order to average
            self.spec.integration_time_micros(int_time)
            self.LaserSpec = np.zeros(self.spec.pixels)
            for i in range(avgs):
                self.LaserSpec += self.spec.intensities()
                self.progress = int(i/avgs)

            if type(self.bckg) != type(None):
                self.LaserSpec = self.LaserSpec/avgs - self.bckg
                # self.wav = self.spec.wavelengths()
                # wav = self.wav[(self.wav>=350)&(self.wav<=1039.5)]

                # self.LaserSpec = self.LaserSpec[(self.wav>=350)&(self.wav<=1039.5)]*calib_factor(wav)
                # self.wav = self.wav[(self.wav>=350)&(self.wav<=1039.5)]
            else:
                self.LaserSpec = self.LaserSpec/avgs
            return True
        except (SeaBreezeError,AttributeError):
            return False

    def acqINSpec(self,int_time, avgs):
        dirname = os.path.dirname(__file__)
        file_path = os.path.join(dirname, 'Intensity_Calibration.txt')
        calibration = np.genfromtxt(file_path,skip_header=1)
        wav_calib = calibration[:,0]
        int_calib = calibration[:,1]
        calib_factor = interp1d(wav_calib,int_calib)

        try:
        #Set integration time and initialize array to zero in order to average
            self.spec.integration_time_micros(int_time)
            self.INSpec = np.zeros(self.spec.pixels)

            for i in range(avgs):
                self.INSpec += self.spec.intensities()
            if type(self.bckg) != type(None):
                self.INSpec = self.INSpec/avgs - self.bckg
                # self.wav = self.spec.wavelengths()
                # wav = self.wav[(self.wav>=350)&(self.wav<=1039.5)]

                # self.INSpec = self.INSpec[(self.wav>=350)&(self.wav<=1039.5)]*calib_factor(wav)
                # self.wav = self.wav[(self.wav>=350)&(self.wav<=1039.5)]
            else:
                self.INSpec = self.INSpec/avgs
            return True
        except (SeaBreezeError,AttributeError):
            return False

    def acqOUTSpec(self,int_time, avgs):
        dirname = os.path.dirname(__file__)
        file_path = os.path.join(dirname, 'Intensity_Calibration.txt')
        calibration = np.genfromtxt(file_path,skip_header=1)
        wav_calib = calibration[:,0]
        int_calib = calibration[:,1]
        calib_factor = interp1d(wav_calib,int_calib)

        try:
        #Set integration time and initialize array to zero in order to average
            self.spec.integration_time_micros(int_time)
            self.OUTSpec = np.zeros(self.spec.pixels)

            for i in range(avgs):
                self.OUTSpec += self.spec.intensities()

            if type(self.bckg) != type(None):

                self.OUTSpec = self.OUTSpec/avgs - self.bckg
                # self.wav = self.spec.wavelengths()
                # wav = self.wav[(self.wav>=350)&(self.wav<=1039.5)]
                # self.OUTSpec = self.OUTSpec[(self.wav>=350)&(self.wav<=1039.5)]*calib_factor(wav)
                # self.wav = self.wav[(self.wav>=350)&(self.wav<=1039.5)]
            else:
                self.OUTSpec =  self.OUTSpec/avgs


            return True
        except (SeaBreezeError,AttributeError):
            return False

    def calcPLQE(self,LaserBounds,PLBounds):

        if type(self.LaserSpec)!=type(None) and type(self.INSpec)!=type(None) and type(self.OUTSpec)!=type(None):        
            try:
                outcount = self.OUTSpec[(self.wav>=350)&(self.wav<=1039.5)] - self.bckg[(self.wav>=350)&(self.wav<=1039.5)]
                wav = self.wav[(self.wav>=350)&(self.wav<=1039.5)]

                lasercount = self.LaserSpec[(self.wav>=350)&(self.wav<=1039.5)]- self.bckg[(self.wav>=350)&(self.wav<=1039.5)]

                incount = self.INSpec[(self.wav>=350)&(self.wav<=1039.5)] - self.bckg[(self.wav>=350)&(self.wav<=1039.5)]

            except TypeError:
                outcount = self.OUTSpec[(self.wav>=350)&(self.wav<=1039.5)] 
                wav = self.wav[(self.wav>=350)&(self.wav<=1039.5)]

                lasercount = self.LaserSpec[(self.wav>=350)&(self.wav<=1039.5)]

                incount = self.INSpec[(self.wav>=350)&(self.wav<=1039.5)]


            dirname = os.path.dirname(__file__)
            file_path = os.path.join(dirname, 'Intensity_Calibration.txt')
            calibration = np.genfromtxt(file_path,skip_header=1)
            wav_calib = calibration[:,0]
            int_calib = calibration[:,1]

            calib_factor = interp1d(wav_calib,int_calib)

            #Get wavelength ranges for laser and PL
            laserwavfilt = wav[(wav >= LaserBounds[0]) & (wav <=LaserBounds[1])] # Laser wavelength range
            plwavfilt = wav[(wav >= PLBounds[0]) & (wav <=PLBounds[1])]

            #OUT
            lasercountfiltout = outcount[(wav >= LaserBounds[0]) & (wav <=LaserBounds[1])]*calib_factor(laserwavfilt) # Counts in laser wavelength range

            plcountfiltout = outcount[(wav >= PLBounds[0]) & (wav <=PLBounds[1])]*calib_factor(plwavfilt) # Counts in PL wavelength range

            # IN
            lasercountfiltin = incount[(wav >= LaserBounds[0]) & (wav <=LaserBounds[1])]*calib_factor(laserwavfilt) # Counts in laser wavelength range
            plcountfiltin = incount[(wav >= PLBounds[0]) & (wav <=PLBounds[1])]*calib_factor(plwavfilt) # Counts in PL wavelength range

            # Empty/Laser
            lasercountfiltempty = lasercount[(wav >= LaserBounds[0]) & (wav <=LaserBounds[1])]*calib_factor(laserwavfilt) # Counts in laser wavelength range
            plcountfiltempty = lasercount[(wav >= PLBounds[0]) & (wav <=PLBounds[1])]*calib_factor(plwavfilt) # Counts in PL wavelength range

            # Calc PLQE
            A = 1 - np.trapz(lasercountfiltin)/np.trapz(lasercountfiltout)
            self.n = 100*((np.trapz(plcountfiltin) - (1 - A)*np.trapz(plcountfiltout))/(np.trapz(lasercountfiltempty)*A))
            self.n = round(self.n, 2)
            return self.n, True
        else:
            return None, False


