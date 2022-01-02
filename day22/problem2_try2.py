# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 09:29:04 2021

@author: Anja
"""
import numpy as np

class CubeRegion:
    def __init__(self, xlim, ylim, zlim, on=True):
        self.xlim = xlim
        self.ylim = ylim
        self.zlim = zlim
        self.on = on
        self.cubes = (1+xlim[1]-xlim[0])*(1+ylim[1]-ylim[0])*(1+zlim[1]-zlim[0])
        
    def getIntersectionCube(self, otherCube):
        xlim = None
        ylim = None
        zlim = None
        if (self.xlim[0] <= otherCube.xlim[1]) and (self.xlim[1] >= otherCube.xlim[0]):
            xlim = [max([self.xlim[0], otherCube.xlim[0]]), min([self.xlim[1], otherCube.xlim[1]])]
        if (self.ylim[0] <= otherCube.ylim[1]) and (self.ylim[1] >= otherCube.ylim[0]):
            ylim = [max([self.ylim[0], otherCube.ylim[0]]), min([self.ylim[1], otherCube.ylim[1]])]
        if (self.zlim[0] <= otherCube.zlim[1]) and (self.zlim[1] >= otherCube.zlim[0]):
            zlim = [max([self.zlim[0], otherCube.zlim[0]]), min([self.zlim[1], otherCube.zlim[1]])]
        #print('intersect',xlim, ylim, zlim)
        intersectedCube = CubeRegion(xlim, ylim, zlim, on=True)
        if otherCube.on is True:
            # then I will add things! So I should return Cube + otherCube - intersect?
            return [self, otherCube], [intersect]
        else:
            # I will turn stuff off!
            return [self], [intersect]
        
    def __repr__(self):
        return str(self.cubes)


def loadInstructions(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    #I have [xmin, xmax], [ymin, ymax], [zmin, zmax] where max is inclusive!
    xpos = []
    ypos = []
    zpos = []
    on = []
    for line in lines:
        line = line.rstrip()
        if 'on' in line:
            on.append(True)
        else:
            on.append(False)
        chunks = line.split(',')   
        xchunks = chunks[0].split('=')
        xchunks2 = xchunks[1].split('..')
        xpos.append([int(xchunks2[0]), int(xchunks2[1])])
        
        ychunks = chunks[1].split('=')
        ychunks2 = ychunks[1].split('..')
        ypos.append([int(ychunks2[0]), int(ychunks2[1])])
        
        zchunks = chunks[2].split('=')
        zchunks2 = zchunks[1].split('..')
        zpos.append([int(zchunks2[0]), int(zchunks2[1])])
            
    return on, xpos, ypos, zpos       
            
            
on, xpos, ypos, zpos = loadInstructions('sample2.txt') 

  
           
cubeRegions = [CubeRegion(xpos[n], ypos[n], zpos[n], on[n]) for n in range(len(on))]

def getIntersection()
                


#print('points on', len(pointsOnDict))


