# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 13:16:49 2019

@author: Dell
"""

#-----bulid model-----#
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
ds = pd.read_csv('datasets/AIS_2017_01_Zone01.csv')
'''
MMIS: Maritime mobile service identity
SOG:  Speed over ground
COG:  Course over ground
'''



'''
xk = A.xk-1 + B.uk + wk-1
zk = H.xk + vk
'''
x=np.array(ds[ds['MMSI']==273898000]['LAT'])[149:189:]
y=np.array(ds[ds['MMSI']==273898000]['LON'])[149:189:]
sog=np.array(ds[ds['MMSI']==273898000]['SOG'])[149:189:]
cog=np.array(ds[ds['MMSI']==273898000]['SOG'])[149:189:]
velx=list(map(lambda x,y:math.cos(math.radians(x))*y,cog,sog))
vely=list(map(lambda x,y:math.sin(math.radians(x))*y,cog,sog))

#sog2=np.array(ds[ds['MMSI']==477444700]['SOG'])[0:100:1]
#sog3=np.array(ds[ds['MMSI']==370024000]['SOG'])[0:100:1]
#sog4=np.array(ds[ds['MMSI']==273898000]['SOG'])[0:100:1]

plt.plot(x, y, label = 'ID:273898000')
#plt.plot(range(len(sog2)), sog2, label = 'SOG2')
#plt.plot(range(len(sog3)), sog3, label = 'SOG3')
#plt.plot(range(len(sog4)), sog4, label = 'SOG4')

plt.legend()
plt.show()

kf=[]
x0=y0=x[0]
P0=1
A=B=1
xx=[]
yy=[]
Q=0.1
R=0.1
for c in range(0,len(x)):
    i,j,vx,vy = x[c],y[c],velx[c],vely[c]
    
    #-----time-update(prediction)-----#
    '''
    xk = A.xk-1 + B.uk
    Pk = A.Pk-1.At + Q
    '''
    xk=x0+vx
    yk=y0+vy
    Pk=P0+Q
    #-----measurement-update(correction)-----#
    '''
    Kk = (Pk.Ht) / (H.Pk.Ht + R)
    xk = xk + Kk(zk - K.xk)
    Pk = (1 - Kk.H)Pk
    '''
    Kk=Pk/(Pk+R)
    xk=xk+Kk*(i-xk)
    yk=yk+Kk*(j-yk)
    Pk=(1-Kk)*Pk
    #-----append estimate----#
    xx.append(xk)
    yy.append(yk)
    x0=xk
    y0=yk
    P0=Pk
plt.plot(x, y, label='Measurements')
plt.plot(xx,yy, label = 'KF')
plt.legend()
plt.show()
