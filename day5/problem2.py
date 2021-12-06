# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 18:04:47 2021

@author: Anja
"""

import pandas as pd
import numpy as np

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "[" + str(self.x) + ", " + str(self.y) + "]"

class Vent:
    def __init__(self, point1, point2):
        self.start = point1
        self.end = point2
        self.vertical = False
        self.horizontal = False
        self.diagonal = False
        if (self.start.x == self.end.x):
            self.vertical = True
        elif (self.start.y == self.end.y):
            self.horizontal = True
        else:
            self.diagonal = True
        self.pointList = self.makeIntermPoints()
        
    def makeIntermPoints(self):
        pointList = []
        if self.vertical:
            if self.start.y < self.end.y:
                for i in range(self.start.y, self.end.y + 1):
                    pointList.append(Point(self.start.x, i))
            else:
                for i in range(self.start.y, self.end.y -1, -1):
                    pointList.append(Point(self.start.x, i))
        if self.horizontal:
            if self.start.x < self.end.x:
                for i in range(self.start.x, self.end.x + 1):
                    pointList.append(Point(i, self.start.y))
            else:
                for i in range(self.start.x, self.end.x -1, -1):
                    pointList.append(Point(i, self.start.y))
        if self.diagonal:
            if self.start.x < self.end.x:
                if self.start.y < self.end.y:
                    for i, x in enumerate(range(self.start.x, self.end.x + 1)):
                        pointList.append(Point(x, self.start.y + i))
                else:
                    for i, x in enumerate(range(self.start.x, self.end.x + 1)):
                        pointList.append(Point(x, self.start.y - i))
            else:
                if self.start.y < self.end.y:
                    for i, x in enumerate(range(self.start.x, self.end.x -1, -1)):
                        pointList.append(Point(x, self.start.y + i))
                else:
                    for i, x in enumerate(range(self.start.x, self.end.x -1, -1)):
                        pointList.append(Point(x, self.start.y - i))
        return pointList
    
    def __str__(self):
        returnStr = '['
        for point in self.pointList:
            returnStr += str(point)
        return returnStr +']'


def load_data(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    vents = []
    Xmax = 0
    Ymax = 0
    for line in lines:
        points = line.split(' -> ')
        coordStart = points[0].split(',')
        start = Point(int(coordStart[0]), int(coordStart[1]))
        coordEnd = points[1].split(',')
        end = Point(int(coordEnd[0]), int(coordEnd[1]))
        vents.append(Vent(start, end))
        if max([start.x, end.x]) > Xmax:
            Xmax = max([start.x, end.x])
        if max([start.y, end.y]) > Ymax:
            Ymax = max([start.y, end.y])
    return vents, Xmax, Ymax

def getOverlapped(Xmax, Ymax, vents):
    playfield = np.zeros((Xmax+1, Ymax+1))
    for vent in vents:
        print(vent.start, vent.end, vent)
        for point in vent.pointList:
            playfield[point.y, point.x] += 1
    print(playfield)
    return (playfield > 1).sum()
    

vents, Xmax, Ymax = load_data('input.txt')

print('overlapped', getOverlapped(Xmax, Ymax, vents))


