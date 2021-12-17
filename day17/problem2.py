# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 07:15:36 2021

@author: Anja
"""


class Probe:
    def __init__(self, xVel, yVel, targetArea):
        self.initial = (xVel, yVel)
        self.xVel = xVel
        self.yVel = yVel
        self.x = 0
        self.y = 0
        self.targetArea = targetArea
        self.maxY = 0
        self.inTarget = False

    def step(self):
        self.x += self.xVel
        self.y += self.yVel
        if self.xVel > 0:
            self.xVel -= 1
        elif self.xVel < 0:
            self.xVel += 1
        self.yVel -= 1
        if self.y > self.maxY:
            self.maxY = self.y
    
    def isProbeInTarget(self):
        if self.inTarget is False:
            if (self.targetArea['x'][0]<= self.x <=self.targetArea['x'][1]):
                if (self.targetArea['y'][0]<= self.y <=self.targetArea['y'][1]):
                    self.inTarget = True
    
    def hasProbeOvershot(self):
        return self.y < self.targetArea['y'][0]
    
    def __repr__(self):
        return str(self.initial)
    
    def __lt__(self, other):
        return self.initial > other.initial
    
    def canProbeReachX(self):
        if self.xVel == 0:
            return (self.targetArea['x'][0]< self.x <self.targetArea['x'][1])
        else: 
            return True

targetAreaSample = {'x': [20, 30], 'y': [-10, -5]} #in 6,9, maxY = 45



def findAllProbes(targetArea):
    allProbes = []
    y_over = False
    #starting x: 1, starting y = 
    y = targetArea['y'][0]
    y_overCounter = 0
    while y_overCounter < 100:
        x = 0
        x_overCounter = 0
        oneProbeFoundTarget = False
        while x_overCounter < 200:
            newProbe = Probe(x, y, targetArea)
            while newProbe.hasProbeOvershot() is False:
                newProbe.step()
                newProbe.isProbeInTarget()
            if newProbe.inTarget is True:
                oneProbeFoundTarget = True
                allProbes.append(newProbe)
            if newProbe.x > targetArea['x'][1]:
                #overshot!
                x_overCounter += 1
            x += 1
        if oneProbeFoundTarget is False:
            y_overCounter += 1
        y += 1
    return allProbes
    
allProbesSample = findAllProbes(targetAreaSample)
allProbesSample.sort()
print(allProbesSample)
#print(findBestProbe(targetAreaSample))        
   




targetAreaPuzzle = {'x': [265, 287], 'y': [-103, -58]}

allProbesPuzzle = findAllProbes(targetAreaPuzzle)
print(len(allProbesPuzzle)) #343 # 652 #712 #1770 #
