#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 08:48:48 2024
Explantory sine signals.
@author: gdf724
"""

import numpy as np
import scipy.signal as scisig
import matplotlib.pyplot as plt

#Signal settings
angle = np.arange(0,2*np.pi,2*np.pi/2000) 
amplitude = 1 

#Simple plot
plt.rc('axes', labelsize=16)
fig, ax = plt.subplots()
ax.plot(angle,amplitude*np.sin(angle))
ax.set_xlabel('Vinkel i radianer')
ax.set_xticks([0,np.pi/2,np.pi,3*np.pi/2,2*np.pi])
ax.grid()
ax.set_ylabel('Amplitud')
plt.show()

#Comparison plots amplitude
angle = np.arange(0,8*np.pi,2*np.pi/2000) 

fig, axs = plt.subplots(2, 1, layout='constrained')
axs[0].plot(angle,amplitude*np.sin(angle))
axs[0].set_xlabel('Vinkel i radianer')
axs[0].set_ylabel('Amplitud')

axs[1].plot(angle,0.5*amplitude*np.sin(angle))
axs[1].set_ylim(-amplitude,amplitude)
axs[1].set_xlabel('Vinkel i radianer')
axs[1].set_ylabel('Amplitud')
plt.show()

#Comparison plot frequency
frequency = 5 #Frequency in Hz
signal_length = 1 #Length in s
sampling_frequency = 2000 #Sampling frequncy in Hz
time=np.arange(0,signal_length,1/sampling_frequency)
fig, axs = plt.subplots(2, 1, layout='constrained')
axs[0].plot(time,amplitude*np.sin(2*np.pi*frequency*time))
axs[0].set_xlabel('Tid / s')
axs[0].set_ylabel('Amplitud')

axs[1].plot(time,amplitude*np.sin(2*np.pi*2*frequency*time))
axs[1].set_ylim(-amplitude,amplitude)
axs[1].set_xlabel('Tid / s')
axs[1].set_ylabel('Amplitud')
plt.show()


#Comparison plot phase
phase = 0.5*np.pi
fig, axs = plt.subplots(2, 1, layout='constrained')
axs[0].plot(angle,amplitude*np.sin(angle))
axs[0].set_xlabel('Vinkel i radianer')
axs[0].set_ylabel('Amplitud')

axs[1].plot(angle,amplitude*np.sin(angle+phase))
axs[1].set_ylim(-amplitude,amplitude)
axs[1].set_xlabel('Vinkel i radianer')
axs[1].set_ylabel('Amplitud')
plt.show()

