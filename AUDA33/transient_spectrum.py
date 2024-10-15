#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 08:10:59 2024
Transient spectrum
@author: gdf724
"""
import numpy as np
import scipy.signal as scisig
import matplotlib.pyplot as plt

#### Helper functions #####
def square_wave(period,pulse_width,time_window,sampling_frequency):
    time=np.arange(0,time_window,1/sampling_frequency)
    signal=np.zeros(len(time))
    
    top_counter=0
    trough_counter=0
    for itr in range(len(signal)):
        if itr>pulse_width*sampling_frequency and top_counter<pulse_width*sampling_frequency and trough_counter==0:
            signal[itr]=1
            top_counter=top_counter+1
        if top_counter>=pulse_width*sampling_frequency:
            if trough_counter<(period-pulse_width)*sampling_frequency:
                trough_counter=trough_counter+1
            else:
                top_counter=0
                trough_counter=0
        
    return signal

#Signal settings
time_window=1 # in s
period=2 # in s
pulse_width=0.002 #in s
sampling_frequency = 44100 #Sampling frequncy in Hz

#Define the signal and one wavelength
signal=square_wave(period, pulse_width, time_window, sampling_frequency)
time=np.arange(0,time_window,1/sampling_frequency)
#Plot spectrum
fig = plt.figure(figsize=(7, 7), layout='constrained')
axs = fig.subplot_mosaic([["waveform"],
                          ["signal"],
                          ["magnitude1"]])
axs["waveform"].set_title("Waveform")
axs["waveform"].plot(time[0:int(0.1*sampling_frequency)], signal[0:int(0.1*sampling_frequency)], color='k')
axs["waveform"].set_xlabel("Time (s)")
axs["waveform"].set_ylabel("Amplitude")

axs["signal"].set_title("Signal")
axs["signal"].plot(time, signal, color='k')
axs["signal"].set_xlabel("Time (s)")
axs["signal"].set_ylabel("Amplitude")

axs["magnitude1"].set_title(str(period)+" s period")
axs["magnitude1"].magnitude_spectrum(signal, Fs=sampling_frequency, color='C1')
axs["magnitude1"].set_xlim(0,3000)


plt.show()
