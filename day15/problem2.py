# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 07:44:15 2021

@author: Anja
"""

from queue import PriorityQueue
import numpy as np

class CavePoint:
    def __init__(self, risk):
        self.risk = risk
        self.shortestRisk = None
        self.visited = False
        self.neighbours = []
        self.neighboursNextGrid = []
        self.nextGrid = False
   
    def __repr__(self):
        return str(self.risk)
        retStr = 'risk: ' + str(self.risk) + '\n'
        retStr += 'shortestRisk: ' + str(self.shortestRisk) + '\n'
        retStr += 'visited: ' + str(self.visited)
        return retStr
    
    
    def __lt__(self, otherPoint):
        return self.shortestRisk < otherPoint.shortestRisk

# sounds like dijistra's algorithm <- always wanted to code that :)

def loadCave(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    cave = []
    for line in lines:
        line = line.rstrip()
        c = []
        for val in line:
            c.append(CavePoint(int(val)))
        cave.append(c)
    # aaand interconnect!
    cavePoints = []
    lastRowPos = []
    rightRowPos = []
    leftRowPos = []
    for x in range(len(cave)):
        for y in range(len(cave[0])):
            if x > 0:
                cave[x][y].neighbours.append(cave[x-1][y])
            if y > 0:
                cave[x][y].neighbours.append(cave[x][y-1])
            if x < (len(cave) - 1):
                cave[x][y].neighbours.append(cave[x+1][y])
            if y < (len(cave[1]) - 1):
                cave[x][y].neighbours.append(cave[x][y+1])
                
            cavePoints.append(cave[x][y])
    return cave, cave[0][0], cave[-1][-1]


def dijistra(cave, start, startRisk = 0):
    D = {}
    cpR = {}
    i = 0
    for x, cPRow in enumerate(cave):
        for y, cP in enumerate(cPRow):
            cpR[cP] = i
            D[i] = float('inf')
            i += 1
    D[cpR[start]] = 0

    pq = PriorityQueue(0)
    pq.put((0, start))
    start.shortestRisk = startRisk
    while not pq.empty():
        (prevRisks, cavePoint) = pq.get()
        cavePoint.visited = True

        for neighbour in cavePoint.neighbours:
            if neighbour.visited is False:
                if neighbour.nextGrid is False:
                    oldRisk = D[cpR[neighbour]]
                    newRisk = prevRisks + neighbour.risk
                    if newRisk < oldRisk:
                        neighbour.shortestRisk = newRisk
                        pq.put((newRisk, neighbour))
                        D[cpR[neighbour]] = newRisk
    return D, cpR


    flatCave = []
    for gridLine in gridCave:
        for cave in gridLine:
            for caveLine in cave:
                for cavePoint in caveLine:
                    flatCave.append(cavePoint)
    return flatCave, gridCave[0][0][0][0], gridCave[-1][-1][-1][-1]
    


def loadCave5(filename, N):
    f = open(filename)
    lines = f.readlines()
    f.close()
    cave = []
    for line in lines:
        line = line.rstrip()
        c = []
        for val in line:
            c.append(CavePoint(int(val)))
        cave.append(c)
    # and repeat!
    shapeC = len(cave)
    nextRiskDict = {i: i+1 for i in range(1, 9)}
    nextRiskDict[9] = 1
    for col in range(N-1):
        for row in range(N):
            if (col == 0) and (row != 0):
                for pos in range(shapeC):
                    cave.append([CavePoint(nextRiskDict[cP.risk]) for cP in cave[shapeC*(row-1)+pos]])
            
            else:
                for x in range(shapeC):
                    pos = row*shapeC + x
                    cave[pos].extend([CavePoint(nextRiskDict[cP.risk]) for cP in cave[pos][-shapeC:]])

    # aaand interconnect!
    for x in range(len(cave)):
        for y in range(len(cave[0])):
            if x > 0:
                cave[x][y].neighbours.append(cave[x-1][y])
            if y > 0:
                cave[x][y].neighbours.append(cave[x][y-1])
            if x < (len(cave) - 1):
                cave[x][y].neighbours.append(cave[x+1][y])
            if y < (len(cave[1]) - 1):
                cave[x][y].neighbours.append(cave[x][y+1])
    
    return cave, cave[0][0], cave[-1][-1]

                
cave, start, end = loadCave5('input.txt', 5) 
print('loaded!') 
D, cPR = dijistra(cave, start)
print('shortest risk one Cave: ', D[(len(cave)*len(cave[0])-1)])




                
                
                
                
                
            