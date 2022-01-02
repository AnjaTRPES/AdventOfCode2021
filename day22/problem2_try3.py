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
        self.cubesOff = None
        
    def intersect(self, otherCube):
        xlim = None
        ylim = None
        zlim = None
        if (self.xlim[0] <= otherCube.xlim[1]) and (self.xlim[1] >= otherCube.xlim[0]):
            xlim = [max([self.xlim[0], otherCube.xlim[0]]),
                    min([self.xlim[1], otherCube.xlim[1]])]
        if (self.ylim[0] <= otherCube.ylim[1]) and (self.ylim[1] >= otherCube.ylim[0]):
            ylim = [max([self.ylim[0], otherCube.ylim[0]]),
                    min([self.ylim[1], otherCube.ylim[1]])]
        if (self.zlim[0] <= otherCube.zlim[1]) and (self.zlim[1] >= otherCube.zlim[0]):
            zlim = [max([self.zlim[0], otherCube.zlim[0]]),
                    min([self.zlim[1], otherCube.zlim[1]])]
            
        # assuming the otherCube is in the middle of this cube:
        if (self.xlim[0]<= xlim[0]) and (self.xlim[1] >= xlim[1]):
            if (self.ylim[0]<= ylim[0]) and (self.ylim[1] >= ylim[1]):
                if (self.zlim[0]<= zlim[0]) and (self.zlim[1] >= zlim[1]):
                    #aha, we are in the middle!
                    if otherCube.on is True:
                        return None, None #nothing needs to be turned on or off!
                    else:
                        return None, otherCube
    
        if (xlim != None) and (ylim != None) and (zlim != None):
            # it is properly intersecting.
            # Thus dividing it into different regions??
            # that is hard... tricky business!
            intersect = CubeRegion(xlim, ylim, zlim, on=True)
            otherCubes = []
            if xlim[0] < otherCube.xlim[1]:
                if xlim[1] < otherCube.xlim[1]:
                    x0 = xlim[1]
                    x1 = otherCube.xlim[1]
                    if ylim[0] < otherCube.ylim[1]:
                        if ylim[1] < otherCube.ylim[1]:
                            y0 = ylim[1]
                            y1 = otherCube.ylim[1]
                            if zlim[0] < otherCube.zlim[1]:
                                if zlim[1] < otherCube.zlim[1]:
                                    z0 = zlim[1]
                                    z1 = otherCube.zlim[1]
                                    otherCubes.append(CubeRegion([x0,x1],
                                                                 [y0, y1],
                                                                 [z0, z1]))
                                else:
                                        
                        else:
                            pass
                else:
                    pass
            else:
                pass
                

            
        else:
            # assuming the otherCube is not intersecting at all
            if otherCube.on is True:
                return otherCube, None
            else:
                # I will turn stuff off!
                return None, intersect
    
    
    def getIntersectCube(self, otherCube):
        xlim = None
        ylim = None
        zlim = None
        if (self.xlim[0] <= otherCube.xlim[1]) and (self.xlim[1] >= otherCube.xlim[0]):
            xlim = [max([self.xlim[0], otherCube.xlim[0]]),
                    min([self.xlim[1], otherCube.xlim[1]])]
        if (self.ylim[0] <= otherCube.ylim[1]) and (self.ylim[1] >= otherCube.ylim[0]):
            ylim = [max([self.ylim[0], otherCube.ylim[0]]),
                    min([self.ylim[1], otherCube.ylim[1]])]
        if (self.zlim[0] <= otherCube.zlim[1]) and (self.zlim[1] >= otherCube.zlim[0]):
            zlim = [max([self.zlim[0], otherCube.zlim[0]]),
                    min([self.zlim[1], otherCube.zlim[1]])]
        if (xlim != None) and (ylim != None) and (zlim != None):  
            return CubeRegion(xlim, ylim, zlim, on=True)
        else:
            return None
            
            
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

def getSum(cubesOn, cubesOff):
    sumOn = sum([cube.cubes for cube in cubesOn])
    if len(cubesOff) > 0:
        sumOff = sum([cube.cubes for cube in cubesOff])
    else:
        sumOff = 0
    return sumOn-sumOff

cubesOn = [cubeRegions[0]]
cubesOff = []
'''
for n in [1,1,1]:
    print('#######')
    newCube = cubeRegions[n]
    for c in range(len(cubesOn)):
        cube = cubesOn[c]
        cubeOn, intersect = cube.intersect(newCube)
        print('cubeOn', cubeOn, 'cubeOff', cubeOff)
        cubesOn.append(cubeOn)
        cubesOff.append(cubeOff)
        print('on: ', cubesOn, 'off: ', cubesOff, 'total:', getSum(cubesOn, cubesOff))
    '''
    if newCube.on == True:
        cubesOn.append(newCube)
    '''
    print('   on: ', cubesOn, 'off: ', cubesOff, 'total:', getSum(cubesOn, cubesOff))
    #print('round ', n, 'sum: ', getSum(cubesOn, cubesOff))
'''
cubesOn = [cubeRegions[0]]
cubesIntersect = []
cubes2much = []
for n in [1, 1, 1]:
    newCube = cubeRegions[n]
    for c in range(len(cubesIntersect)):
        #does the new cube intersect with it??


                
# cubes on after 0  instructions on? True :  139590.0
# cubes on after 1  instructions on? True :  210918.0
# cubes on after 2  instructions on? True :  225476.0
# cubes on after 3  instructions on? True :  328328.0
# cubes on after 4  instructions on? True :  387734.0
# cubes on after 5  instructions on? True :  420416.0
# cubes on after 6  instructions on? True :  436132.0
# cubes on after 7  instructions on? True :  478727.0
# cubes on after 8  instructions on? True :  494759.0
# cubes on after 9  instructions on? True :  494804.0
# cubes on after 10  instructions on? False :  492164.0
# cubes on after 11  instructions on? True :  534936.0
# cubes on after 12  instructions on? False :  534936.0
# cubes on after 13  instructions on? True :  567192.0
# cubes on after 14  instructions on? False :  567150.0
# cubes on after 15  instructions on? True :  592167.0
# cubes on after 16  instructions on? False :  588567.0
# cubes on after 17  instructions on? True :  592902.0
# cubes on after 18  instructions on? False :  590029.0
# cubes on after 19  instructions on? True :  590784.0

#print('points on', len(pointsOnDict))


