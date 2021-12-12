# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 11:31:56 2021

@author: Anja
"""

class Cave:
    def __init__(self, name, Type):
        self.name = name
        self.type = Type
        self.neighbours = []
        
    def __str__(self):
        return str(self.name)
    
    def __repr__(self):
        return str(self.name)
    
    def nextPathPoss(self, paths, lastCaveName):
        #print('exploring', self.name, paths)
        
        if self.name == 'end':
            return [p+'-end' for p in paths]
        
        if (self.type == 'big') or (self.type == 'start'):
            nextPaths = []
            for path in paths:
                for neighbour in self.neighbours:
                    if neighbour.name != lastCaveName and (neighbour.type != 'start'):
                        pathsFoundFromThere = neighbour.nextPathPoss([path+'-'+self.name], self.name)
                        for p in pathsFoundFromThere:
                            nextPaths.append(p)
            return nextPaths

        
        elif self.type == 'small':
            nextPaths = []
            for path in paths:
                for neighbour in self.neighbours:
                    if (neighbour.type != 'start') and (self.name not in path.split('-')):
                        pathsFoundFromThere = neighbour.nextPathPoss([path+'-'+self.name], self.name)
                        for p in pathsFoundFromThere:
                            nextPaths.append(p)
            return nextPaths



def readFile(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    caves = {}
    startcave = None
    endcave = None
    cavesStrings = []
    #first load all the caves
    for line in lines:
        print(line)
        line = line.rstrip()
        splitted = line.split('-')
        for sp in splitted:
            if sp not in cavesStrings:
                cavesStrings.append(sp)
                if sp == 'start':
                    caveType = 'start'
                elif sp == 'end':
                    caveType = 'end'
                elif sp.islower():
                    caveType = 'small'
                else:
                    caveType = 'big'
                caves[sp] = Cave(sp, caveType)
    print(caves)
    #now link the paths
    for line in lines:
        line = line.rstrip()
        splitted = line.split('-')
        caves[splitted[0]].neighbours.append(caves[splitted[1]])
        caves[splitted[1]].neighbours.append(caves[splitted[0]])
    return caves


caves = readFile('input.txt')  
pathList = caves['start'].nextPathPoss([''], '')
pathList.sort()     
print('all paths:', len(pathList))
#for p in pathList:
#    print(p)
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                