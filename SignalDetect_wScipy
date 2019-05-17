#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 15:14:32 2019

@author: robertobrenes
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
from scipy.signal import find_peaks, peak_widths


    
def find_idx(array,value):
    return (np.abs(array - value)).argmin()

spectrum = np.genfromtxt('RB120_HPA_PLQE_Sample1_Spot1_in.txt')
bckg = np.genfromtxt('RB120_HPA_PLQE_bckg.txt')


filt_data = gaussian_filter1d(spectrum[:,1]-bckg[:,1],sigma=10,order=0,axis=0)
#filt_noise = gaussian_filter1d(bckg[:,1],sigma=10,order=0,axis=0)



plt.figure()
plt.plot(spectrum[:,0],spectrum[:,1])
plt.plot(spectrum[:,0],filt_data)
plt.yscale('log')

laser_low = find_idx(spectrum[:,0],450)
laser_high = find_idx(spectrum[:,0],600)

pl_low = find_idx(spectrum[:,0],650)
pl_high =find_idx(spectrum[:,0],900)


laser_data = filt_data[laser_low:laser_high]
pl_data =filt_data[pl_low:pl_high]

peaks, _ = find_peaks(laser_data,height=5)
plt.figure()
plt.plot(laser_data)
plt.plot(peaks,laser_data[peaks],'x')
plt.yscale('log')

results = peak_widths(laser_data,peaks=peaks,rel_height=0.999)

plt.hlines(*results[1:])

pl_peaks, _ = find_peaks(pl_data,height=10)
plt.figure()
plt.plot(pl_data)
plt.plot(pl_peaks,pl_data[pl_peaks],'x')
plt.yscale('log')

pl_results = peak_widths(pl_data,peaks=pl_peaks,rel_height=0.9)


plt.hlines(*pl_results[1:])