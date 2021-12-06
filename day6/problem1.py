# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 07:59:51 2021

@author: Anja
"""

import numpy as np

class Lanternfish:
    
    def __init__(self, cycle):
        self.timer = cycle
        self.spawned = False
    
    def update(self):
        if self.timer != 0:
            self.timer -= 1
            self.spawned = False
        else:
            self.timer = 6
            self.spawned = True
            
    def __str__(self):
        return str(self.timer)


def loadFishes(filename):
    data = np.loadtxt(filename, delimiter=',')
    fishes = [Lanternfish(i) for i in data]
    return fishes


def simulateDays(fishes, days):
    for day in range(days):
        newFishes = []
        for fish in fishes:
            fish.update()
            if fish.spawned:
                newFishes.append(Lanternfish(8))
        fishes.extend(newFishes)
        
        #print('After ', day+1, 'day: ', [str(f) for f in fishes])
    return len(fishes)
    
    
fishes = loadFishes('sample.txt')
#print(simulateDays(fishes, 18))
print(simulateDays(fishes, 256))










