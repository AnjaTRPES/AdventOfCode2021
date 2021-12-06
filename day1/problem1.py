# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 17:32:48 2021

@author: Anja
"""

import numpy as np

Realdata = np.loadtxt("input.txt")

testData= [199,
200,
208,
210,
200,
207,
240,
269,
260,
263]


def find_N(data):
    Nincrease = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            Nincrease += 1
    return Nincrease

def find_N_sliding_window(data):
    Nincrease = 0
    g = 0
    while (g < len(data)-3):
        first_sum = sum(data[g:g+3])
        second_sum = sum(data[g+1:g+4])
        if second_sum > first_sum:
            Nincrease += 1
        g += 1
    return Nincrease
        

print('testSet', find_N_sliding_window(testData)) #1461 not correct???
print('realData', find_N_sliding_window(Realdata))













