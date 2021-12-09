# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 17:55:18 2021

@author: Anja
"""

import numpy as np


class heatmap:

    
    def __init__(self, heatmap):    
        class coord:
            def __init__(self, value, left, right, up, down):
                self.value = value
                self.left = left
                self.up = up
                self.down = down
                self.right = right
            def __str__(self):
                return str(self.value)
        
        self.colL = len(heatmap)
        self.rowL = len(heatmap[0])
        self.maxV = max(max(heatmap))
        
        self.heatmap = []
        # initialize it
        for x in range(self.colL):
            col = []
            for y in range(self.rowL):
                col.append(coord(heatmap[x][y], None, None, None, None))
            self.heatmap.append(col)
        # link it
        for x in range(self.colL):
            for y in range(self.rowL):
                if y > 0:
                    self.heatmap[x][y].up = self.heatmap[x][y-1]
                if y < (self.rowL -1):
                    self.heatmap[x][y].down = self.heatmap[x][y+1]
                if x > 0:
                    self.heatmap[x][y].right = self.heatmap[x-1][y]
                if x < (self.colL -1):
                    self.heatmap[x][y].left = self.heatmap[x+1][y]
        
    def findBasins(self):
        basins = []
        #print(self.__str__())
        for x in range(self.colL):
            for y in range(self.rowL):
                if self.heatmap[x][y].value != 9:
                    #print('starting one basin')
                    basins.append(self.getBasin(self.heatmap[x][y]))
                    #print(self.__str__(), basins[-1])
        return basins
    
    def __str__(self):
        returnstr = ''
        for x in range(self.colL):
            returnstr += '['
            for y in range(self.rowL):
                returnstr += str(self.heatmap[x][y]) +','
            returnstr += ']\n'
        returnstr += '-------------'
        return returnstr
    
    def getBasin(self, point):
        if point == None:
            return 0
        if point.value == 9:
            return 0
        else:
            point.value = 9
            return 1 + self.getBasin(point.left) + self.getBasin(point.right) + self.getBasin(point.up) + self.getBasin(point.down)
            
        
        #self.lowPoints = self.getLowPoints()
        

    def getLowPoints(self):
        lowPoints = []
        
        for x in range(self.colL):
            for y in range(self.rowL):
                # need to compare to up, down, left, right (if exists)
                if y > 0:
                    up = self.heatmap[x][y-1]
                else:
                    up = self.maxV
                
                if y < (self.rowL - 1):
                    down = self.heatmap[x][y+1]
                else:
                    down = self.maxV
                if x > 0:
                    right = self.heatmap[x-1][y]
                else:
                    right = self.maxV
                if x < (self.colL -1):
                    left = self.heatmap[x+1][y]
                else:
                    left = self.maxV
                point = self.heatmap[x][y]
                #print(up, down, left, right)
                minDir = min([up, down, left, right])
                #print(point, minDir)
                if (point < minDir):
                    lowPoints.append(point)
        return lowPoints


    def getRiskLevels(self):
        riskLevel = 0
        for p in self.lowPoints:
            riskLevel += p + 1
        
        return riskLevel


def loadHeightmap(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    heatmap = []
    for line in lines:
        height = []
        for char in line:
            if char in '0123456789':
                height.append(int(char))
        heatmap.append(height)
    return heatmap

data = loadHeightmap('input.txt')
hm = heatmap(data)
basins = hm.findBasins()

basins.sort()

print(basins[-1]*basins[-2]*basins[-3])
    

#print(hm.findBasins())




