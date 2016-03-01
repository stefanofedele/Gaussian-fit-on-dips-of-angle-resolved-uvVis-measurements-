# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:40:20 2015

@author: fedel_000
"""

import matplotlib.pyplot as plt
import numpy as np
#import random
import pandas as pd
import os
import time


def integTimeValue(files):
   integTimeIndex = files.find('integTime')
   integTimeIndex = integTimeIndex + len('integTime')
   integTimeIndex1 = files.find('Average') - 1
   integTime = files[ integTimeIndex :integTimeIndex1 ]
   integTime = integTime.replace('_', '.')
   integTime = float(integTime)
   return integTime


xlim_left = 400
xlim_right = 1000
#plt.close(1)
#Angle = '00_0'
#path = "C:\Users\\fedel_000\Desktop\Measurements\Reflectance_10_09_angle_resolved\\" + Angle + "degrees"
#path = "C:\Users\\fedel_000\Desktop\\Measurements\Reflectance_10_21_angle_resolved\\" + Angle + "degrees"
path = r"C:\Users\fedel_000\Desktop\Measurements\Reflectance_12_09_angle_resolved" + "\\" + Angle + "degrees"

files = os.listdir(path)
files.sort()

backgroundNumber = 1
fileNumber = 4#8
wavelength = pd.read_csv(path + '/' + files[backgroundNumber], sep=',', header=None)[0].astype(float)
background = pd.read_csv(path + '/' +  files[backgroundNumber], sep=',', header=None)[1].astype(float)/integTimeValue( files[backgroundNumber] )
signal = pd.read_csv(path + '/' +  files[fileNumber], sep=',', header=None)[1].astype(float)/integTimeValue( files[fileNumber] )
reflectance = signal/background

angle = files[fileNumber].index('angle')
L = len('angle')
angle =angle + L
angle = float( files[fileNumber][ angle : angle + 4].replace('_', '.') )#<-------

fig1 = plt.figure(1)

ax = fig1.add_subplot(111)
#ax.add_title(files[fileNumber][:-4])
spectra, = ax.plot(wavelength, reflectance, linewidth=2.0)
plt.draw()



ax.set_xlim(xlim_left, xlim_right)
ylim1 = np.where(wavelength > 400)[0][0]
ylim2 = np.where(wavelength > 1000)[0][0]
ylim = np.max(reflectance[ylim1 : ylim2])
ax.set_ylim(0, ylim)
[(leftx, lefty), (rightx, righty)] = plt.ginput(2)
a = np.where( wavelength < leftx)
b = np.where( wavelength < rightx)
leftIndex = a[0][len(a[0]) - 1]
rightIndex = b[0][len(b[0]) - 1]

wavelengthSelected = wavelength[ leftIndex : rightIndex ]
reflectanceSelected = reflectance[ leftIndex : rightIndex ]


def gaussFit(x, gauss, ax):
    #global line1
    #global line2
    #concavity = raw_input("print -1 for negative concavity and +1 for positive concavity\n")    
    #concavity = float(concavity)    
    concavity = np.average( np.diff( np.diff(gauss) ) ) # average value of second derivative
    #print concavity
    if  concavity > 0:
        gauss = - gauss # to invert concavity
        level = abs(np.min(gauss) ) + 1 # to avoid negative (abs) or zero ( + 1 ) values in the logaritm
        gauss = gauss + abs(level) 
        #plt.plot(x, gauss, 'k')   
        #plt.draw()

    log_gauss = np.log(gauss)
    a, b, c= np.polyfit(x, log_gauss, 2)
    sigma_0 = (abs(2*a))**-0.5
    x_medio_0 = - b/(2*a)
    P_0 = np.sqrt(np.pi*2) *sigma_0*np.exp(c+ x_medio_0*b/2)
    

    
    gaussfit = P_0/(np.sqrt(2*np.pi) * sigma_0)* np.exp( -( x - x_medio_0 )**2/( 2*sigma_0**2 ) )
      
    y_medio_0 = np.max(gaussfit)
          
    
    if concavity > 0:
        gaussfit = gaussfit - level
        gaussfit = - gaussfit
        
        y_medio_0 = y_medio_0 - level
        y_medio_0 = - y_medio_0
    
    
    line1, = ax.plot(x, gaussfit, 'k--', linewidth=2.0)
    line2, = ax.plot(x_medio_0, y_medio_0, 'r+', linewidth=4.0)
    #plt.draw()
    return x_medio_0, y_medio_0, sigma_0, line1, line2
 
xpeak , ypeak, sigma, line1, line2 = gaussFit(wavelengthSelected, reflectanceSelected, ax)   
plt.draw()
#plt.pause(1)
time.sleep(1)

#spectra.remove()
#line1.remove()
#line2.remove()
#time.sleep(2)
#line1.remove()
#plt.close(1)