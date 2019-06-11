import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import pandas as pd
ds = pd.read_csv('datasets/AIS_2017_01_Zone01.csv')

#style.use('dark_background')
#style.use('seaborn-dark')
style.use('ggplot')

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_title("AIS Tracking")
ax.set_xlim(62.7, 64.0)
ax.set_ylim(-175.0, -174.0)
ax.set_autoscale_on(False)
#plt.ion()

def animate(i):
    global count
    lat=np.array(ds[ds['MMSI']==273898000]['LAT'])[count:count+10:]
    lon=np.array(ds[ds['MMSI']==273898000]['LON'])[count:count+10:]
    count+=1
    #graph_data = open('example.txt','r').read()
    #lines = graph_data.split('\n')
    #xs = []
    #ys = []
    #for line in lines:
    #    if len(line) > 1:
    #        x, y = line.split(',')
    #        xs.append(float(x))
    #        ys.append(float(y))
    ax.clear()
    ax.set_title("AIS Tracking")
    ax.set_xlabel('Latitude')
    ax.set_ylabel('Longitude')
    ax.set_xlim(62.7, 64.0)
    ax.set_ylim(-175.0, -174.0)
    ax.set_autoscale_on(False)
    ax.plot(lat, lon)

count=0
ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()