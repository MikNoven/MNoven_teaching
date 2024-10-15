#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 08:16:32 2024
Fourier synthesis example
@author: gdf724
"""

import numpy as np
import scipy.signal as scisig
import matplotlib.pyplot as plt
import sounddevice as sd

#Signal settings
signal_length = 2 #Length in s
amplitude = 1.57 #To make component amplitude simple
frequency = 440 #In Hz
sampling_frequency = 44100 #Sampling frequncy in Hz

#Define the signal and one wavelength
time=np.arange(0,signal_length,1/sampling_frequency)
waveform_time=np.arange(0,2/frequency,1/sampling_frequency)
signal=amplitude*scisig.sawtooth(2*np.pi*frequency*time)
signal=signal[::-1]
waveform=amplitude*scisig.sawtooth(2*np.pi*frequency*waveform_time)
waveform=waveform[::-1]

#Plot the whole signal and one wavelength
fig, axs = plt.subplots(2, 1, layout='constrained')
axs[0].plot(time,signal)
axs[0].set_xlabel('Time (s)')
axs[0].set_ylabel('Amplitude')

axs[1].plot(waveform_time,waveform)
axs[1].set_xlabel('Time (s)')
axs[1].set_ylabel('Amplitude')
plt.show()


#Play standard signal
sd.play(signal, sampling_frequency) #device=0 should be mini-tele jack.
sd.wait()
sd.stop()

#Sawtooth example
Fourier_components=6
synth_signal=np.zeros(len(time))
for itr in range(1,Fourier_components+1,1):
    synth_signal=synth_signal+(1/itr)*np.sin(2*np.pi*itr*frequency*time) #N.B! Amplitude only correct for this series.
    
    
fig = plt.figure(figsize=(7, 7), layout='constrained')
fig.suptitle('Fourirer synthesis with '+str(Fourier_components)+' series components.', fontsize=20)
axs = fig.subplot_mosaic([["waveform"],
                          ["magnitude"]])
axs["waveform"].set_title("Waveform")
axs["waveform"].plot(waveform_time, waveform, color='k')
axs["waveform"].plot(waveform_time, synth_signal[0:len(waveform_time)], color='b', linestyle='dashed')
axs["waveform"].set_xlabel("Time (s)")
axs["waveform"].set_ylabel("Amplitude")

# plot different spectrum types:
axs["magnitude"].set_title("Magnitude Spectrum")
axs["magnitude"].magnitude_spectrum(synth_signal, Fs=sampling_frequency, color='C1')

plt.show()

sd.play(synth_signal, sampling_frequency) #device=0 should be mini-tele jack.
sd.wait()
sd.stop()

    