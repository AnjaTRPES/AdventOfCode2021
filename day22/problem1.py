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
            
            
on, xpos, ypos, zpos = loadInstructions('sample.txt')            

minL = -50
maxL = 51
# grid is in -50 to 50     
reactor = np.zeros((50*2+2, 50*2+2, 50*2+2)) 
#print(on[0], xpos[0], ypos[0], zpos[0])
for h in range(len(on)-2):
    #print('instruction:', xpos[h], ypos[h], zpos[h], on[h])
    mins = [xpos[h][0]+50,
            ypos[h][0]+50,
            zpos[h][0]+50]
    maxs = [xpos[h][1]+51,
            ypos[h][1]+51,
            zpos[h][1]+51] 
    #print('instruction:', mins, maxs)
    for i in range(3):
        if mins[i] < 0:
            #print('changed min')
            mins[i] = 0
        if maxs[i] < 0:
            #print('changed min2')
            maxs[i] = 0
        if maxs[i] > maxL*2+1:
            # print('changed min3')
            maxs[i] = maxL*2
        if mins[i] > maxL*2+1:
            #print('changed min4')
            mins[i] = maxL*2
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
    
    print('cubes on after', h,' instructions on?', on[h],': ', reactor.sum())

print('cubes on after instructions: ', reactor.sum(), ' should be 590784')

        
            
            
            
            
            
        