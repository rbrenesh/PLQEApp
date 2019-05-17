import numpy as np
import matplotlib.pyplot as plt

from scipy.ndimage import gaussian_filter1d


def thresholding_algo(y,bckg,lag, threshold, influence):
    signals = np.zeros(len(y))
    filteredY = np.array(y)
    avgFilter = [0]*len(y)
    stdFilter = [0]*len(y)
#    avgFilter[lag - 1] = np.mean(y[0:lag])
    avgFilter[lag - 1] = np.mean(bckg[0:lag])
#    stdFilter[lag - 1] = np.std(y[0:lag])
    stdFilter[lag - 1] = np.std(bckg[0:lag])
    for i in range(lag, len(y)):
        if abs(y[i] - avgFilter[i-1]) > threshold * stdFilter [i-1]:
            if y[i] > avgFilter[i-1]:
                signals[i] = 1
            else:
                signals[i] = -1

            filteredY[i] = influence * y[i] + (1 - influence) * filteredY[i-1]
#            avgFilter[i] = np.mean(filteredY[(i-lag+1):i+1])
            avgFilter[i] = np.mean(bckg[(i-lag+1):i+1])
#            stdFilter[i] = np.std(filteredY[(i-lag+1):i+1])
            stdFilter[i] = np.std(bckg[(i-lag+1):i+1])
        else:
            signals[i] = 0
            filteredY[i] = y[i]
#            avgFilter[i] = np.mean(filteredY[(i-lag+1):i+1])
            avgFilter[i] = np.mean(bckg[(i-lag+1):i+1])
#            stdFilter[i] = np.std(filteredY[(i-lag+1):i+1])
            stdFilter[i] = np.std(bckg[(i-lag+1):i+1])

    return dict(signals = np.asarray(signals),
                avgFilter = np.asarray(avgFilter),
                stdFilter = np.asarray(stdFilter))
    
    
def find_idx(array,value):
    return (np.abs(array - value)).argmin()
    
    

def detect_signal(wavelength, counts , bckg ,low_idx, high_idx, signal_type):
    
    #counts and signal must already be low pass filtered (eg. with a Gaussian convolution)
    #returns the indices of the detected signal within the low_idx:high_idx window
    
    if signal_type == 'PL':
        detect = thresholding_algo(counts[low_idx:high_idx],bckg,150,4,0)
        
    else:
        detect = thresholding_algo(counts[low_idx:high_idx],bckg,150,4.5,0)
        
        
        
    signal_idx =   np.where(np.abs(detect["signals"])==1)[0] 
    
    return signal_idx
    
if __name__== "__main__":
    
    spectrum = np.genfromtxt('RB120_HPA_PLQE_Sample1_Spot1_in.txt')
    bckg = np.genfromtxt('RB120_HPA_PLQE_bckg.txt')
    
    
    filt_data = gaussian_filter1d(spectrum[:,1],sigma=5,order=0,axis=0)
    filt_noise = gaussian_filter1d(bckg[:,1],sigma=5,order=0,axis=0)
    
    plt.figure()
    plt.plot(spectrum[:,0],spectrum[:,1])
#    plt.plot(bckg[:,0],filt_noise)
    plt.plot(spectrum[:,0],filt_data)
    plt.yscale('log')
    
    laser_low = find_idx(spectrum[:,0],450)
    laser_high = find_idx(spectrum[:,0],600)
    
    pl_low = find_idx(spectrum[:,0],650)
    pl_high =find_idx(spectrum[:,0],900)
    
    
#    edge_idx = gaussian_filter1d(filt_data[pl_low:pl_high],sigma=20,order=1)
    
#    laser = thresholding_algo(filt_data[laser_low:laser_high],bckg[:,1][laser_low:laser_high],100,3,0)
    laser = thresholding_algo(filt_data[laser_low:laser_high],filt_noise,150,4.5,0)
#    laser = thresholding_algo(bckg[:,1][laser_low:laser_high],bckg[:,1][laser_low:laser_high],100,3,0)
#    pl = thresholding_algo(filt_data[pl_low:pl_high],bckg[:,1][pl_low:pl_high],100,3,0)
    pl = thresholding_algo(filt_data[pl_low:pl_high],filt_noise,150,4,0)
#    pl = thresholding_algo(bckg[:,1][pl_low:pl_high],bckg[:,1][pl_low:pl_high],100,3,0)
#    plt.plot()
#    plt.plot(spectrum[:,0][pl_low:pl_high][np.argmax(edge_idx):np.argmin(edge_idx)],spectrum[:,1][pl_low:pl_high][np.argmax(edge_idx):np.argmin(edge_idx)])
    
    a= spectrum[:,0][laser_low:laser_high][np.where(np.abs(laser["signals"])==1)]
    b = spectrum[:,1][laser_low:laser_high][np.where(np.abs(laser["signals"])==1)]
    
    ext = 40
    signal_idx = np.where(np.abs(pl["signals"])==1)[0]
#    lowidx  = np.arange(signal_idx[0]-ext,signal_idx[0],1)
#    highidx = np.arange(signal_idx[-1]+1,signal_idx[-1]+ext+1,1)
#    signal_idx = np.hstack((lowidx,signal_idx,highidx))
    
    
    d = spectrum[:,0][pl_low:pl_high][signal_idx]
    e =filt_data[pl_low:pl_high][signal_idx]
    
#    a = spectrum[:,0][laser_low:laser_high]
#    b = spectrum[:,1][laser_low:laser_high]
    plt.plot(a,b)
    plt.plot(d,e)
    
    
    plt.figure()
    plt.plot(spectrum[:,0][laser_low:laser_high], np.abs(laser["signals"]))
    plt.plot(spectrum[:,0][pl_low:pl_high], np.abs(pl["signals"]))
#    plt.plot(spectrum[:,0][pl_low:pl_high], edge_idx)
    
    
    
#    plt.plot(spectrum[:,0][pl_low:pl_high][np.argmax(edge_idx):np.argmin(edge_idx)],spectrum[:,1][pl_low:pl_high][np.argmax(edge_idx):np.argmin(edge_idx)])