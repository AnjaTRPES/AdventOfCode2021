# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 09:03:40 2021

@author: Anja
"""
import numpy as np


class point:
    def __init__(self, val=0):
        self.val = val
    


def loadImageAndAlgo(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    algo = lines[0]
    lines.pop(0)
    lines.pop(0)
    xLen = len(lines[0])-1
    yLen = len(lines)
    image = np.zeros((xLen+20, yLen+20))
    for y, line in enumerate(lines):
        line = line.rstrip()
        for x, char in enumerate(line):
            if char == '#':
                image[y+10, x+10]=1
            else:
                image[y+10, x+10]=0
    return algo, image

def getNextPixel(flatStr, algo):
    posAlgo = int(flatStr, 2)
    return algo[posAlgo]

def applyAlgo(image, algo, startbg=0):
    xDir, yDir = image.shape
    #calculate ntext bg
    flString = ''.join([str(int(startbg)) for i in range(9)])
    bgPixel = getNextPixel(flString, algo)  
    if bgPixel == '.':
        bgPixel = 0
    else:
        bgPixel = 1
    if bgPixel == 0:
        newImage = np.zeros((xDir+4, yDir+4))
    else:
        newImage = np.ones((xDir+4, yDir+4))
    for y in range(1, yDir-1):
        for x in range(1, xDir-1):
            flattened = image[y-1:y+2,x-1:x+2].flatten()
            flString = ''.join([str(int(val)) for val in flattened])
            nextPix = getNextPixel(flString, algo)
            if nextPix == '#':
                newImage[y+2, x+2] = 1
            else:
                newImage[y+2, x+2] = 0
    return newImage, bgPixel

def printImage(image):
    lines = []
    for y in range(image.shape[0]):
        line = []
        for x in range(image.shape[1]):
            if image[y,x]==1:
                line.append('#')
            else:
                line.append('.')
        line.append('\n')
        lines.append(''.join(line))
    return ''.join(lines)

algo, image = loadImageAndAlgo('input.txt')
bg = 0
for n in range(50):
    image, bg = applyAlgo(image, algo, bg)
#newImage2, bg = applyAlgo(newImage, algo, bg)
#print(printImage(newImage2))
print(image.sum()) #5622.0 is the right answer!
    
#t = np.array([[0,0,0],[1,0,0],[0,1,0]])
    
    