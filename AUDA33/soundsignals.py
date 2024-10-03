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

#Signal settings
signal_length = 2 #Length in s
shape = 'sinusoid' #Choose between sinusoid, square, triangle, sawtooth_init_slope, and sawtooth_final_slope.
sq_duty_cycle=0.5 #Duty cycle for square waves
amplitude = 1 
frequency = 440 #In Hz
sampling_frequency = 44100 #Sampling frequncy in Hz

#Define the signal
time=np.arange(0,signal_length,1/sampling_frequency)
if shape=='sinusoid':
    signal=amplitude*np.sin(2*np.pi*frequency*time)
elif shape=='square':
    signal=scisig.square(time,sq_duty_cycle)

#Plot the signal
plt.plot(time,signal)
plt.show()

#Listen to the signal
sd.play(signal, sampling_frequency)
sd.wait()
sd.stop()
