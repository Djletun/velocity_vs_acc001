#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import csv
import os


if os.name == 'nt':
    symbol = '\\'
if os.name == 'posix':
    symbol = '/'
#/home/me/PycharmProjects/velocity_vs acc001/data01/0.CSV
#print(os.environ)
dir_path = os.path.dirname(os.path.abspath(__file__)) + symbol
print('dir_path=', dir_path)
SignalFileName = dir_path + 'data01'+symbol+'0.CSV'
print(SignalFileName)
with open(SignalFileName, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    data = np.array(list(reader)).astype(float)

#print(data[:][:, 1])
#print(data[:][:, 0])
fig, ax = plt.subplots()
#ax.plot(data[:][:, 0],data[:][:, 1],linewidth = 1, color ='black')
#plt.show()
#plt.savefig(SignalFileName + '.pdf', dpi=300)
# signal len = 0.5 sec max ampl = 0.9
max_x = data[:][-1,0]
null_y = data[:][0,1]
max_y = max(data[:][:,1])
ampl=max_y - null_y

x_val = np.linspace(0, max_x, 500)
signal_interp = 1/ampl*(np.interp(x_val, data[:][:, 0],data[:][:, 1])-null_y)
velocity_signal = np.empty(shape=500)
velocity_signal[0]=0
velocity_signal[1:] = np.diff(signal_interp)
acc_signal = np.empty(shape=500)
acc_signal[0]=0
acc_signal[1:]=np.diff(velocity_signal)
dt=10
acc_signal_n=np.empty(shape=500+dt)
acc_signal_n[:len(acc_signal)]=acc_signal
acc_signal_n[len(acc_signal):len(acc_signal)+dt]=acc_signal[-1]
velocity_signal_trapz = np.empty(shape=500)

velocity_signal_trapz[0]=0
for i in range(499):
    velocity_signal_trapz[i+1] = np.trapz(acc_signal[i:i+1+dt])
y=velocity_signal_trapz
print(len(y))

ax.plot(range(0,500),y,linewidth = 1, color ='black')
plt.savefig(SignalFileName + '.acc_to_vel.pdf', dpi=300)
