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
from scipy.ndimage import gaussian_filter1d
import matplotlib.pyplot as plt

class NoSpectraToProcess(Exception):
    pass

class NoSignal(Exception):
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
        self.filtbckg = None
        self.filtLaserSpec = None
        self.filtINSpec = None
        self.filtOUTSpec = None
        self.laserwavfilt = None
        self.plwavfilt = None
        self.plcountfiltout = None
        self.lasercountfiltout = None
        self.lasercountfiltin = None
        self.plcountfiltin = None
        self.lasercountfiltempty = None
        self.laserbckg = None
        self.inplbckg = None
        self.outplbckg = None
        self.signal =  False


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

        # dirname = os.path.dirname(__file__)
        # file_path = os.path.join(dirname, 'Intensity_Calibration.txt')
        # calibration = np.genfromtxt(file_path,skip_header=1)
        # wav_calib = calibration[:,0]
        # int_calib = calibration[:,1]
        # calib_factor = interp1d(wav_calib,int_calib)
        try:
        #Set integration time and initialize array to zero in order to average
            self.spec.integration_time_micros(int_time)
            self.LaserSpec = np.zeros(self.spec.pixels)
            for i in range(avgs):
                self.LaserSpec += self.spec.intensities()
                self.progress = int(i/avgs)

            self.LaserSpec = self.LaserSpec/avgs
            self.signal =  False
            # if type(self.bckg) != type(None):
            #     self.LaserSpec = self.LaserSpec/avgs - self.bckg
            #     # self.wav = self.spec.wavelengths()
            #     # wav = self.wav[(self.wav>=350)&(self.wav<=1039.5)]

            #     # self.LaserSpec = self.LaserSpec[(self.wav>=350)&(self.wav<=1039.5)]*calib_factor(wav)
            #     # self.wav = self.wav[(self.wav>=350)&(self.wav<=1039.5)]
            # else:
            #     self.LaserSpec = self.LaserSpec/avgs
            return True
        except (SeaBreezeError,AttributeError):
            return False

    def acqINSpec(self,int_time, avgs):
        # dirname = os.path.dirname(__file__)
        # file_path = os.path.join(dirname, 'Intensity_Calibration.txt')
        # calibration = np.genfromtxt(file_path,skip_header=1)
        # wav_calib = calibration[:,0]
        # int_calib = calibration[:,1]
        # calib_factor = interp1d(wav_calib,int_calib)

        try:
        #Set integration time and initialize array to zero in order to average
            self.spec.integration_time_micros(int_time)
            self.INSpec = np.zeros(self.spec.pixels)

            for i in range(avgs):
                self.INSpec += self.spec.intensities()

            self.INSpec = self.INSpec/avgs
            self.signal =  False
            # if type(self.bckg) != type(None):
            #     self.INSpec = self.INSpec/avgs - self.bckg
            #     # self.wav = self.spec.wavelengths()
            #     # wav = self.wav[(self.wav>=350)&(self.wav<=1039.5)]

            #     # self.INSpec = self.INSpec[(self.wav>=350)&(self.wav<=1039.5)]*calib_factor(wav)
            #     # self.wav = self.wav[(self.wav>=350)&(self.wav<=1039.5)]
            # else:
            #     self.INSpec = self.INSpec/avgs
            return True
        except (SeaBreezeError,AttributeError):
            return False

    def acqOUTSpec(self,int_time, avgs):
        # dirname = os.path.dirname(__file__)
        # file_path = os.path.join(dirname, 'Intensity_Calibration.txt')
        # calibration = np.genfromtxt(file_path,skip_header=1)
        # wav_calib = calibration[:,0]
        # int_calib = calibration[:,1]
        # calib_factor = interp1d(wav_calib,int_calib)

        try:
        #Set integration time and initialize array to zero in order to average
            self.spec.integration_time_micros(int_time)
            self.OUTSpec = np.zeros(self.spec.pixels)

            for i in range(avgs):
                self.OUTSpec += self.spec.intensities()


            self.OUTSpec =  self.OUTSpec/avgs
            self.signal =  False

            return True
        except (SeaBreezeError,AttributeError):
            return False



    def thresholding_algo(self,y,bckg,lag, threshold, influence):
        signals = np.zeros(len(y))
        filteredY = np.array(y)
        avgFilter = np.mean(bckg)
        stdFilter = np.std(bckg)
        # avgFilter = [0]*len(bckg)
        # stdFilter = [0]*len(bckg)
    #    avgFilter[lag - 1] = np.mean(y[0:lag])
        # avgFilter[lag - 1] = np.mean(bckg[0:lag])
    #    stdFilter[lag - 1] = np.std(y[0:lag])
        # stdFilter[lag - 1] = np.std(bckg[0:lag])

        signals[(y-avgFilter > threshold*stdFilter)] = 1


    #     for i in range(lag, len(y)):
    #         if abs(y[i] - avgFilter[i-1]) > threshold * stdFilter [i-1]:
    #             if y[i] > avgFilter[i-1]:
    #                 signals[i] = 1
    #             else:
    #                 signals[i] = -1
    #
    #             filteredY[i] = influence * y[i] + (1 - influence) * filteredY[i-1]
    # #            avgFilter[i] = np.mean(filteredY[(i-lag+1):i+1])
    #             # avgFilter[i] = np.mean(bckg[(i-lag+1):i+1])
    # #            stdFilter[i] = np.std(filteredY[(i-lag+1):i+1])
    #             # stdFilter[i] = np.std(bckg[(i-lag+1):i+1])
    #         else:
    #             signals[i] = 0
    #             filteredY[i] = y[i]
    #            avgFilter[i] = np.mean(filteredY[(i-lag+1):i+1])
                # avgFilter[i] = np.mean(bckg[(i-lag+1):i+1])
    #            stdFilter[i] = np.std(filteredY[(i-lag+1):i+1])
                # stdFilter[i] = np.std(bckg[(i-lag+1):i+1])

        return dict(signals = np.asarray(signals),
                avgFilter = np.asarray(avgFilter),
                stdFilter = np.asarray(stdFilter))


    def find_idx(array,value):
        return (np.abs(array - value)).argmin()

    def detect_signal(self,LaserBounds,PLBounds,calib_filepath,inplthreshold,outplthreshold,laserthreshold):

        #returns arrays with detected signals for laser and inPL, outPL
        try:

            wav = self.wav[(self.wav>=350)&(self.wav<=1039.5)]
            lasercount = gaussian_filter1d(self.LaserSpec[(self.wav>=350)&(self.wav<=1039.5)],sigma=5,order=0,axis=0)
            outcount = gaussian_filter1d(self.OUTSpec[(self.wav>=350)&(self.wav<=1039.5)],sigma=5,order=0,axis=0)
            incount = gaussian_filter1d(self.INSpec[(self.wav>=350)&(self.wav<=1039.5)],sigma=5,order=0,axis=0)
            self.filtbckg = gaussian_filter1d(self.bckg[(self.wav>=350)&(self.wav<=1039.5)],sigma=5, order=0,axis=0)

            # wav = self.wav[(self.wav>=350)&(self.wav<=1039.5)]
            # lasercount = self.LaserSpec[(self.wav>=350)&(self.wav<=1039.5)]
            # outcount = self.OUTSpec[(self.wav>=350)&(self.wav<=1039.5)]
            # incount = self.INSpec[(self.wav>=350)&(self.wav<=1039.5)]
            # self.filtbckg =self.bckg[(self.wav>=350)&(self.wav<=1039.5)]


            calibration = np.genfromtxt(calib_filepath,skip_header=1)
            wav_calib = calibration[:,0]
            int_calib = calibration[:,1]

            calib_factor = interp1d(wav_calib,int_calib)


            self.laserwavfilt = wav[(wav >= LaserBounds[0]) & (wav <=LaserBounds[1])]
            self.plwavfilt = wav[(wav >= PLBounds[0]) & (wav <=PLBounds[1])]


            self.plcountfiltout = outcount[(wav >= PLBounds[0]) & (wav <=PLBounds[1])]
            self.lasercountfiltout = outcount[(wav >= LaserBounds[0]) & (wav <=LaserBounds[1])]

            self.lasercountfiltin = incount[(wav >= LaserBounds[0]) & (wav <=LaserBounds[1])]
            self.plcountfiltin = incount[(wav >= PLBounds[0]) & (wav <=PLBounds[1])]

            self.lasercountfiltempty = lasercount[(wav >= LaserBounds[0]) & (wav <=LaserBounds[1])]

            # print(np.shape(self.plcountfiltin))
            # print(np.shape(self.filtbckg[(wav >= PLBounds[0]) & (wav <=PLBounds[1])]))
            lag = 150
            inpl_detect = self.thresholding_algo(self.plcountfiltin,self.filtbckg[(wav >= PLBounds[0]) & (wav <=PLBounds[1])],lag,inplthreshold,0)
            outpl_detect = self.thresholding_algo(self.plcountfiltout,self.filtbckg[(wav >= PLBounds[0]) & (wav <=PLBounds[1])],lag,outplthreshold,0)
            laser_detect = self.thresholding_algo(self.lasercountfiltempty,self.filtbckg[(wav >= LaserBounds[0]) & (wav <=LaserBounds[1])],lag,laserthreshold,0)


            inpl_detect_idx = np.where(np.abs(inpl_detect["signals"])==1)[0]
            outpl_detect_idx = np.where(np.abs(outpl_detect["signals"])==1)[0]
            laser_detect_idx = np.where(np.abs(laser_detect["signals"])==1)[0]



            self.laserbckg = self.filtbckg[(wav >= LaserBounds[0]) & (wav <=LaserBounds[1])]
            self.inplbckg = self.filtbckg[(wav >= PLBounds[0]) & (wav <=PLBounds[1])]
            self.outplbckg = self.filtbckg[(wav >= PLBounds[0]) & (wav <=PLBounds[1])]

            laserx = self.laserwavfilt[laser_detect_idx]
            lasery = self.lasercountfiltempty[laser_detect_idx] - self.laserbckg[laser_detect_idx]
            inplx = self.plwavfilt[inpl_detect_idx]
            inply = self.plcountfiltin[inpl_detect_idx] - self.inplbckg[inpl_detect_idx]
            outplx = self.plwavfilt[outpl_detect_idx]
            outply = self.plcountfiltout[outpl_detect_idx] - self.outplbckg[outpl_detect_idx]


            self.plcountfiltin = self.plcountfiltin - self.outplbckg
            self.plcountfiltout = self.plcountfiltout - self.inplbckg
            self.lasercountfiltempty = self.lasercountfiltempty -self.laserbckg
            self.lasercountfiltin = self.lasercountfiltin-self.laserbckg
            self.lasercountfiltout = self.lasercountfiltout-self.laserbckg

            # print(self.plwavfilt[outpl_detect_idx])
            # print(calib_factor(self.plwavfilt[inpl_detect_idx]))

            # print(np.max(calib_factor(self.laserwavfilt[laser_detect_idx])))
            # print(np.max(calib_factor(self.plwavfilt[inpl_detect_idx])))


            self.plcountfiltin[outpl_detect_idx] = self.plcountfiltout[outpl_detect_idx]*calib_factor(self.plwavfilt[outpl_detect_idx])
            # self.plcountfiltout[inpl_detect_idx] = self.plcountfiltout[inpl_detect_idx]*calib_factor(self.plwavfilt[inpl_detect_idx])
            self.plcountfiltin[inpl_detect_idx] = self.plcountfiltin[inpl_detect_idx]*calib_factor(self.plwavfilt[inpl_detect_idx])
            # print(self.plwavfilt[inpl_detect_idx])
            self.lasercountfiltempty[laser_detect_idx] = self.lasercountfiltempty[laser_detect_idx]*calib_factor(self.laserwavfilt[laser_detect_idx])
            self.lasercountfiltout[laser_detect_idx] = self.lasercountfiltout[laser_detect_idx]*calib_factor(self.laserwavfilt[laser_detect_idx])
            self.lasercountfiltin[laser_detect_idx] = self.lasercountfiltin[laser_detect_idx]*calib_factor(self.laserwavfilt[laser_detect_idx])



            if len(laser_detect_idx)>1 and len(inpl_detect_idx)>1:
                self.signal =  True
            else:
                self.signal = False

            return laserx, lasery, inplx, inply, outplx, outply

        except TypeError:
            raise NoSpectraToProcess()
        # except Exception as e:
            # raise e



    def calcPLQE(self,LaserBounds,PLBounds,calib_filepath):

        if self.signal != True:
            raise NoSignal()

        if type(self.LaserSpec)!=type(None) and type(self.INSpec)!=type(None) and type(self.OUTSpec)!=type(None):
            try:
                # Calc PLQE
                A = 1 - np.trapz(self.lasercountfiltin)/np.trapz(self.lasercountfiltout)
                # plt.figure()
                # plt.plot(self.lasercountfiltin-self.laserbckg)
                # plt.plot(self.lasercountfiltout-self.laserbckg)
                # plt.show()
                # print(np.trapz(self.lasercountfiltin-self.laserbckg))
                # print(np.trapz(self.lasercountfiltout-self.laserbckg))
                self.n = 100*((np.trapz(self.plcountfiltin) - (1 - A)*np.trapz(self.plcountfiltout))/(np.trapz(self.lasercountfiltempty)*A))
                self.n = round(self.n, 2)
                return self.n, True
            except Exception as e:
                raise e
        else:
            return None, False
