#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 11:46:49 2024
Generate waveforms, listen to how they sound.
@author: Mikael Novén
"""

import numpy as np
import scipy.signal as scisig
import matplotlib.pyplot as plt
import sounddevice as sd
import scipy.fft as scifft

#Signal settings
signal_length = 2 #Length in s
shape = 'square' #Choose between sinusoid, square, triangle, sawtooth_init_slope, and sawtooth_final_slope.
sq_duty_cycle=0.8 #Duty cycle for square waves
amplitude = 1 
frequency = 110 #In Hz
sampling_frequency = 44100 #Sampling frequncy in Hz

#Define the signal and one wavelength
time=np.arange(0,signal_length,1/sampling_frequency)
if shape=='sinusoid':
    waveform_time=np.arange(0,1/frequency,1/sampling_frequency)
    signal=amplitude*np.sin(2*np.pi*frequency*time)
    waveform=amplitude*np.sin(2*np.pi*frequency*waveform_time)
elif shape=='square':
    waveform_time=time[0:2*round(sampling_frequency/frequency)]
    signal=scisig.square(2*np.pi*frequency*time,sq_duty_cycle)
    waveform=signal[0:2*round(sampling_frequency/frequency)]
elif shape=='sawtooth_init_slope':
    waveform_time=np.arange(0,2/frequency,1/sampling_frequency)
    signal=amplitude*scisig.sawtooth(2*np.pi*frequency*time)
    waveform=amplitude*scisig.sawtooth(2*np.pi*frequency*waveform_time)
elif shape=='sawtooth_final_slope':
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

#Listen to the signal
sd.play(signal, sampling_frequency)
sd.wait()
sd.stop()


