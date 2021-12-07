# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 09:08:28 2021

@author: Anja
"""

import numpy as np


def minCosts(filename):
    data = np.loadtxt(filename, delimiter=',')
    
    minH = int(data.min())
    maxH = int(data.max())
    
    posH = [i for i in range(minH, maxH+1)]
    
    costs = []
    
    for pos in posH:
        fuel = 0
        for d in data:
            n = abs(pos-d)
            fuel += n*(n+1)/2
        costs.append(fuel)
            
    return min(costs)

print(minCosts('sample.txt'))
print(minCosts('input.txt'))