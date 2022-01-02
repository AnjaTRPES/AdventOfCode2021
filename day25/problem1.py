# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 09:57:50 2022

@author: Anja
"""
import numpy as np

class Cucumber:
    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY
        self.canMove = False
        self.nextPos = None


class SouthCucumber(Cucumber):
    def __init__(self, posX, posY):
        Cucumber.__init__(self, posX, posY)
    
    def setCanMove(self, canMove):
        self.canMove = canMove
        if canMove == False:
            self.nextPos = self.posY
    
    def move(self, height):
        if self.canMove == True:
            if self.posY + 1 == height:
                self.posY = 0
            else:
                self.posY += 1
        return self.posX, self.posY

class EastCucumber(Cucumber):
    def __init__(self, posX, posY):
        Cucumber.__init__(self, posX, posY)
    
    def setCanMove(self, canMove):
        self.canMove = canMove
        if canMove == False:
            self.nextPos = self.posX
    
    def move(self, width):
        if self.canMove == True:
            if self.posX + 1 == width:
                self.posX = 0
            else:
                self.posX += 1
        return self.posX, self.posY


class Seabed:
    def __init__(self, size, floor):
        self.width, self.height = size[0], size[1]
        self.southHerd = []
        self.eastHerd = []
        self.floor = floor
        for x in range(self.width):
            for y in range(self.height):
                if floor[x, y] == 1:
                    self.southHerd.append(SouthCucumber(x, y))
                if floor[x, y] == 2:
                    self.eastHerd.append(EastCucumber(x, y))
    
    def step(self):
        previous = np.copy(self.floor)
        self.moveEastHerd()
        self.moveSouthHerd()
        difference = self.floor - previous
        diff = np.sum(np.abs(difference))
        #print('diff:', diff)
        return (diff != 0)
    
    def moveEastHerd(self):
        self.checkCanMoveEast()
        self.moveEast()
        
    def moveSouthHerd(self):
        self.checkCanMoveSouth()
        self.moveSouth()
    
    def checkCanMoveEast(self):
        for cuc in self.eastHerd:
            if cuc.posX + 1 != self.width:
                cuc.nextPos = cuc.posX + 1
            else:
                cuc.nextPos = 0
            cuc.setCanMove(((self.floor[cuc.nextPos, cuc.posY] == 0)))
            
    def moveEast(self):
        self.floor[self.floor == 2] = 0
        #print('before moving east:', self)
        for cuc in self.eastHerd:
            self.floor[cuc.nextPos, cuc.posY] = 2
            cuc.posX = cuc.nextPos
    
    def moveSouth(self):
        self.floor[self.floor == 1] = 0
        #print('before moving south:', self)
        for cuc in self.southHerd:
            self.floor[cuc.posX, cuc.nextPos] = 1
            cuc.posY = cuc.nextPos
    
    def checkCanMoveSouth(self):
        for cuc in self.southHerd:
            if cuc.posY + 1 != self.height:
                cuc.nextPos = cuc.posY + 1
            else:
                cuc.nextPos = 0
            cuc.setCanMove(((self.floor[cuc.posX, cuc.nextPos] == 0)))
    
    def __repr__(self):
        lines = []
        for y in range(self.height):
            line = []
            for x in range(self.width):
                if floor[x, y] == 2:
                    line.append('>')
                elif floor[x, y] == 1:
                    line.append('v')
                elif floor[x, y] == 0:
                    line.append('.')
            line.append('\n')
            lines.append(''.join(line))
        return ''.join(lines)
                
        
def loadFloor(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    floor = np.zeros((len(lines[0].rstrip()), len(lines)))
    for y, line in enumerate(lines):
        line = line.rstrip()
        for x, char in enumerate(line):
            if char == 'v':
                floor[x, y] = 1 # south cucumber!
            if char == '>':
                floor[x, y] = 2 # east cucumber!
    return floor

floor = loadFloor('input.txt')

seabed = Seabed(floor.shape, floor)
steps = 0
changed = True
while changed:
    steps += 1
    changed = seabed.step()
    print(steps)

print('stopped changing after step: ', steps)

'''
print('Initial state:')
print(seabed)
changed = seabed.step()
print('\nAfter 1 step')
print(seabed)
'''   
        
        
        
        
        
        