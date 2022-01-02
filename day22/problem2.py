# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 08:17:56 2021

@author: Anja
"""
import numpy as np
import pandas as pd


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
            
            
on, xpos, ypos, zpos = loadInstructions('sample3.txt')            

xArray = np.array(xpos)
yArray = np.array(ypos)
zArray = np.array(zpos)

minLx = xArray.min()
minLy = yArray.min()
minLz = zArray.min()
maxLx = xArray.max()+1
maxLy = yArray.max()+1
maxLz = zArray.max()+1
# grid is in -50 to 50     
reactor = np.zeros(((maxLx - minLx)*2+2, (maxLy - minLy)*2+2, (maxLz - minLz)*2+2), dtype = np.int8) 
#print(on[0], xpos[0], ypos[0], zpos[0])
for h in range(len(on)):
    #print('instruction:', xpos[h], ypos[h], zpos[h], on[h])
    mins = [xpos[h][0]-minLx,
            ypos[h][0]-minLy,
            zpos[h][0]-minLz]
    maxs = [xpos[h][1]+maxLx,
            ypos[h][1]+maxLy,
            zpos[h][1]+maxLz] 
    #print('instruction:', mins, maxs)
    if (mins[0] < maxs[0]) and (mins[1] < maxs[1]) and (mins[2] < maxs[2]):
        #okay, I can execute the instruction!
        if on[h] is True:
            #print('turning on')
            reactor[mins[0]:maxs[0], mins[1]:maxs[1], mins[2]:maxs[2]] += 1
            reactor[reactor > 1] = 1
        else:
            #print('turning off')
            reactor[mins[0]:maxs[0], mins[1]:maxs[1], mins[2]:maxs[2]] -= 1
            reactor[reactor < 0] = 0
        
    else:
        print('invalid instructions')
    
    reactor = np.abs(reactor)
    
    print('cubes on after instructions: ', reactor.sum())

print('cubes on after instructions: ', reactor.sum(), ' should be 590784')

        
            
            
            
            
            
        