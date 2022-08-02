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
    reader = csv.DictReader(csvfile)
    print(*reader)

    #for row in spamreader:
       # print(', '.join(row))
