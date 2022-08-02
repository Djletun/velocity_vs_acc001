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

print(data[:][:, 1])
print(data[:][:, 0])
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

ax.plot(range(0,500),signal_interp,linewidth = 1, color ='black')
plt.savefig(SignalFileName + '.new.pdf', dpi=300)