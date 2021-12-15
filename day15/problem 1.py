# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 07:44:15 2021

@author: Anja
"""

from queue import PriorityQueue

class CavePoint:
    def __init__(self, risk):
        self.risk = risk
        self.shortestRisk = None
        self.visited = False
        self.left = None
        self.right = None
        self.up = None
        self.down = None
    
    def __repr__(self):
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
    for x in range(len(cave)):
        for y in range(len(cave[0])):
            if x > 0:
                cave[x][y].left = cave[x-1][y]
            if y > 0:
                cave[x][y].up = cave[x][y-1]
            if x < (len(cave) - 1):
                cave[x][y].right = cave[x+1][y]
            if y < (len(cave[1]) - 1):
                cave[x][y].down = cave[x][y+1]
            cavePoints.append(cave[x][y])
    return cavePoints, cave[0][0], cave[-1][-1]


def dijistra(cave, start):
    D = {cP: float('inf') for cP in range(len(cave))}
    cpR = {cP: i for i, cP in enumerate(cave)}
    D[cpR[start]] = 0

    pq = PriorityQueue(0)
    pq.put((0, start))
    start.shortestRisk = 0
    
    while not pq.empty():
        (prevRisks, cavePoint) = pq.get()
        cavePoint.visited = True
        
        for neighbour in [cavePoint.left, cavePoint.right, cavePoint.up, cavePoint.down]:
            if neighbour is not None:
                if neighbour.visited is False:
                    oldRisk = D[cpR[neighbour]]
                    newRisk = prevRisks + neighbour.risk
                    if newRisk <= oldRisk:
                        neighbour.shortestRisk = newRisk
                        pq.put( (newRisk, neighbour) )
                        D[cpR[neighbour]] = newRisk
    return D
                                      
                
cave, start, end = loadCave('input.txt') 
print('loaded!')              
D = dijistra(cave, start)
print('shortest risk: ', D[len(cave)-1])
                
                
                
                
                
            