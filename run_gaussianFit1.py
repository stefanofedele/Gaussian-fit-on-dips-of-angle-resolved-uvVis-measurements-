# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 22:56:30 2015

@author: fedel_000
"""
import matplotlib.pyplot as plt
import os
import pandas as pd

Path = 'C:\\Users\\fedel_000\\Documents\\Python Scripts\\gaussFit1.py'

Angle1 = []
xPeak = []
yPeak = []
Sigma = []
index = 0
plt.figure(2)

global line1
global line2
global fig

#xlim_left = raw_input('x lim left\n')
#xlim_right = raw_input('x lim right\n')

for j in range(200, 825, 25):
#for j in range(1):
    Angle = str(j/10.0)
    Angle1 = Angle1 + [float(Angle)]    
    Angle = Angle.replace('.', '_')
    exec(open(Path).read())
    #exec(Path)
    xPeak = xPeak + [xpeak]
    yPeak = yPeak + [ypeak]    
    Sigma = Sigma + [sigma]
    plt.figure(2)
    plt.subplot(311)
    plt.xlabel('Angle')
    plt.ylabel('wavelength $\lambda$ (nm)')
    plt.plot(Angle1[index], xPeak[index], '+', linewidth=3.0)
    plt.xlim(00, 70)
    plt.subplot(312)
    plt.xlabel('Angle')
    plt.ylabel('Intensity')
    plt.plot(Angle1[index], yPeak[index], '+', linewidth=3.0)
    plt.xlim(0, 70)
    plt.subplot(313)
    plt.plot(Angle1[index], Sigma[index], '+', linewidth=3.0)
    plt.xlabel('Angle')
    plt.ylabel('$\sigma$ (nm)')
    plt.xlim(0, 70)
    plt.draw()
    index = index + 1

#Angle = '20_0'
#execfile(Path)

sampleIndex = files[fileNumber].find('ml') + 2
sampleName = files[fileNumber][2:sampleIndex]

energy = [1.24e3/wavelength for wavelength in xPeak]

Dic = { 'angle': Angle1, 'wavelength (nm)': xPeak, 'energy (eV)': energy, 'intensity': yPeak, 'sigma': Sigma }
df = pd.DataFrame(Dic)

pathDesktop = r"C:\Users\fedel_000\Desktop\Measurements\Reflectance_12_09_angle_resolved"
os.chdir(pathDesktop)
writer = pd.ExcelWriter('uvVisAngle' + sampleName + '.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='uvVisAngle' )

#df1.to_excel(writer, sheet_name='sheet2')
writer.save()
writer.close()











