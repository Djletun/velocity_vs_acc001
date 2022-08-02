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
ax.plot(data[:][:, 0],data[:][:, 1],linewidth = 1, color ='black')
#plt.show()
plt.savefig(SignalFileName + '.pdf', dpi=300)
# signal len = 0.5 sec max ampl = 0.9
