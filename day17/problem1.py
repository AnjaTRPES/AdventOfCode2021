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
        return 'InVel '+str(self.initial) +'=> maxY: ' + str(self.maxY)
    
    def canProbeReachX(self):
        if self.xVel == 0:
            return (self.targetArea['x'][0]< self.x <self.targetArea['x'][1])
        else: 
            return True

targetAreaSample = {'x': [20, 30], 'y': [-10, -5]} #in 6,9, maxY = 45

'''
bestProbe = Probe(0, 0, None)
for x in range(-targetAreaSample['x'][1], targetAreaSample['x'][1], 1):
    for y in range(-targetAreaSample['x'][1], targetAreaSample['x'][1], 1):
        newProbe = Probe(x, y, targetAreaSample)
        while newProbe.hasProbeOvershot() is False:
            newProbe.step()
            newProbe.isProbeInTarget()
        if newProbe.inTarget is True:
            if newProbe.maxY > bestProbe.maxY:
                bestProbe = newProbe

print(bestProbe)    
'''
def findBestProbe(targetArea):
    bestProbe2 = Probe(0, 0, None)
    y_over = False
    #starting x: 1, starting y = 
    y = 0
    y_overCounter = 0
    while y_overCounter < 7:
        x = 0
        x_over = False
        oneProbeFoundTarget = False
        while x_over is False:
            newProbe = Probe(x, y, targetArea)
            while newProbe.hasProbeOvershot() is False:
                newProbe.step()
                newProbe.isProbeInTarget()
            if newProbe.inTarget is True:
                oneProbeFoundTarget = True
                if newProbe.maxY > bestProbe2.maxY:
                    bestProbe2 = newProbe
            if newProbe.x > targetArea['x'][1]:
                #overshot!
                x_over = True
                if oneProbeFoundTarget is False:
                    y_overCounter += 1
            x += 1
        y += 1
    return bestProbe2
        
print(findBestProbe(targetAreaSample))        
   

'''
testProbe = Probe(6, 9, targetAreaSample)
overshot = False
while overshot is False:
    testProbe.step()
    testProbe.isProbeInTarget()
    print(testProbe.inTarget)
    overshot = testProbe.hasProbeOvershot()
print('max Height:', testProbe)
'''


targetAreaPuzzle = {'x': [265, 287], 'y': [-103, -58]}

print(findBestProbe(targetAreaPuzzle))   #1275 is not it... too low # or: 5253
