# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 10:25:37 2021

@author: Anja
"""


class octopus:
    def __init__(self, level):
        self.level = level
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.diagUpLeft = None
        self.diagUpRight = None
        self.diagDownLeft = None
        self.diagDownRight = None
        self.flashed = False
    
    def step(self):
        self.level += 1
    
    def flash(self):
        if (self.level > 9) and (self.flashed == False):
            self.flashed = True
            for neighbour in [self.right, self.left, self.up, self.down,
                              self.diagUpLeft, self.diagDownRight, 
                              self.diagDownLeft, self.diagUpRight]:
                if neighbour != None:
                    neighbour.level += 1
                    neighbour.flash()
    def hasResetFlash(self):
        if self.flashed == True:
            self.flashed = False
            self.level = 0
            return 1
        else:
            return 0
            
    
    

def loadfile(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    octgrid = []
    #load initial octopie
    for line in lines:
        octLine = []
        for char in line:
            if char in '0123456789':
                octLine.append(octopus(int(char)))
        octgrid.append(octLine)
    # Now link the octgrid!
    xLen = len(octgrid)
    yLen = len(octgrid[0])
    for x in range(xLen):
        for y in range(yLen):
            if x > 0:
                octgrid[x][y].left = octgrid[x-1][y]
            if x < (xLen - 1):
                octgrid[x][y].right = octgrid[x+1][y]
            if y > 0:
                octgrid[x][y].up = octgrid[x][y-1]
            if y < (yLen - 1):
                octgrid[x][y].down = octgrid[x][y+1]
            if (x > 0) and (y > 0):
                octgrid[x][y].diagUpLeft = octgrid[x-1][y-1]
            if (x > 0) and (y < (yLen - 1)):
                octgrid[x][y].diagDownLeft = octgrid[x-1][y+1]
            if (x < (xLen - 1)) and (y > 0):
                octgrid[x][y].diagUpRight = octgrid[x+1][y-1]
            if (x < (xLen -1)) and (y < (yLen -1)):
                octgrid[x][y].diagDownRight = octgrid[x+1][y+1]
    return octgrid
            
    
def goSteps(octgrid, steps):
    
    flashes = 0
    for step in range(steps):
        #Increase all starting levels!
        for octline in octgrid:
            for octo in octline:
                octo.step()
        #Flash!
        for octline in octgrid:
            for octo in octline:
                octo.flash()
        #Reset and count!
        for octline in octgrid:
            for octo in octline:
                flashes += octo.hasResetFlash()
    return flashes

def whenSimultaneouslyFlash(octgrid):
    i = 0
    allFlashed = False
    while (allFlashed == False):
        i += 1
        flashDuringStep = 0
        for octline in octgrid:
            for octo in octline:
                octo.step()
        #Flash!
        for octline in octgrid:
            for octo in octline:
                octo.flash()
        #Reset and count!
        for octline in octgrid:
            for octo in octline:
                flashDuringStep += octo.hasResetFlash()
        #print("step ", i, " flashes", flashDuringStep)
        #Check whether all flashed?
        if flashDuringStep == len(octgrid)*len(octgrid[0]):
            allFlashed = True
    return i

octgrid = loadfile('input.txt')
#print(goSteps(octgrid, 100))
print(whenSimultaneouslyFlash(octgrid))

