# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 07:59:51 2021

@author: Anja
"""

import numpy as np
from collections import Counter


# with a Counter object!!
def loadFishCounter(filename):
    data = np.loadtxt(filename, delimiter=',')
    fishes = {i:0 for i in range(9)}
    for d in data:
        fishes[d] += 1
    return fishes

def afterDays(fishes, days):
    for d in range(days):
        #print('Day ', d+1, fishes)
        tempDict = {}
        tempDict[8] = fishes[0]
        tempDict.update({i-1: fishes[i] for i in range(1, 9)})
        tempDict[6] += fishes[0]
        fishes = tempDict
    return fishes

def getAmoundFishes(fishes):
    return sum([i for i in fishes.values()])

fishes = loadFishCounter('input.txt')
fishes = afterDays(fishes, 256)
print(getAmoundFishes(fishes))
        





