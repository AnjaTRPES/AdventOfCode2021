# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 08:47:49 2021

@author: Anja
"""

import numpy as np


def loadFile(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    
    coords = []
    folds = []
    maxX = 0
    maxY = 0
    for line in lines:
        if line[0] in '01234566789':
            line = line.rstrip()
            sp = line.split(',')
            x = int(sp[0])
            y = int(sp[1])
            coords.append([x, y])
            if x > maxX:
                maxX = x
            if y > maxY:
                maxY = y
        if line[0] == 'f':
            line = line.rstrip()
            sp = line.split(' ')
            sp2 = sp[2].split('=')
            folds.append([sp2[0], int(sp2[1])])
    
    paper = np.zeros((maxY+1, maxX+1))
    for coord in coords:
        paper[coord[1], coord[0]] = 1
    return paper, folds


def foldPaper(fold, paper):
    foldLine = fold[1]
    if fold[0] == 'y':
        paper2 = paper[:foldLine, :]
        paperFoldedTop = np.flipud(paper[foldLine+1:, :])
        return paper2 + paperFoldedTop
    if fold[0] == 'x':
        paper2 = paper[:, :foldLine]
        paperFoldedTop = np.fliplr(paper[:, foldLine+1:])
        return paper2 + paperFoldedTop
        
def getDots(paper):
    dots = 0
    for line in paper:
        for val in line:
            if val != 0:
                dots += 1
    return dots
        
def foldCompletly(paper, folds):
    for fold in folds:
        print('papershape', paper.shape, 'fold', fold)
        paper = foldPaper(fold, paper)
    return paper

def makeReadable(paper):
    readPaper = ""
    for x in range(paper.shape[0]):
        line = ""
        for y in range(paper.shape[1]):
            if paper[x, y] > 0:
                line += '#'
            else:
                line += "."
        line += "\n"
        readPaper += line
    return readPaper
        

paper, folds = loadFile('input.txt')

foldedPaper = foldCompletly(paper, folds)

print(makeReadable(foldedPaper))
