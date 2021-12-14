# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 07:36:55 2021

@author: Anja
"""

from collections import Counter
import time

def loadFile(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    
    pairInsertionRules = {}
    for line in lines:
        line = line.rstrip()
        if line == '':
            pass
        elif '->' in line:
            chunks = line.split(' -> ')
            pairInsertionRules[chunks[0]] =Counter([chunks[0][0]+chunks[1],chunks[1]+chunks[0][1]])
        else:
            polymerTemplate = line
    ppC = []
    for i in range(len(polymerTemplate)-1):
        ppC.append(polymerTemplate[i:i+2])
    return Counter(ppC), pairInsertionRules, polymerTemplate[-1]


def goStep(polymerTemplate, pairInsertionRules):
    newCounter = Counter()
    for pp in polymerTemplate:
        amount = polymerTemplate[pp]
        newPairs = pairInsertionRules[pp]
        for newPair in newPairs:
            newCounter[newPair] = newCounter[newPair]+amount
    return newCounter

def goNSteps(polymerTemplate, pairInsertionRules, N):
    for i in range(N):
        polymerTemplate = goStep(polymerTemplate, pairInsertionRules)
    return polymerTemplate

def getAmountOfElements(polymerTemplate, endLetter):
    amountEl = Counter()
    for pp in polymerTemplate:
        amount = polymerTemplate[pp]
        amountEl[pp[0]] = amountEl[pp[0]] + amount
    amountEl[endLetter] = amountEl[endLetter]+1
    return amountEl

def numberOfElements(c):
    maxKey = max(c, key=c.get)
    minKey = min (c, key=c.get)
    print ('subtraction: ', c[maxKey]-c[minKey])


polymerTemplate, pairInsertionRules, endLetter = loadFile('input.txt')
#print(polymerTemplate)
polymerTemplate = goNSteps(polymerTemplate, pairInsertionRules, 40)
#print(polymerTemplate)
c = getAmountOfElements(polymerTemplate, endLetter)
numberOfElements(c)



