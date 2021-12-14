# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 07:36:55 2021

@author: Anja
"""

from collections import Counter

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
            pairInsertionRules[chunks[0]] =chunks[0][0]+chunks[1]+chunks[0][1]
        else:
            polymerTemplate = line
    return polymerTemplate, pairInsertionRules

def goStep(polymerTemplate, pairInsertionRules):
    nextTemplate = ''
    for i in range(len(polymerTemplate)-1):
        if i != len(polymerTemplate) - 2:
            nextTemplate += pairInsertionRules[polymerTemplate[i:i+2]][0:2]
        else:
            nextTemplate += pairInsertionRules[polymerTemplate[i:i+2]]
    return nextTemplate

def goNSteps(polymerTemplate, pairInsertionRules, N):
    for i in range(N):
        polymerTemplate = goStep(polymerTemplate, pairInsertionRules)
        #print('step', i, ': ', polymerTemplate)
    return polymerTemplate

def numberOfElements(polymerTemplate):
    c = Counter(polymerTemplate)
    maxKey = max(c, key=c.get)
    minKey = min (c, key=c.get)
    print ('subtraction: ', c[maxKey]-c[minKey])
    return c

polymerTemplate, pairInsertionRules = loadFile('sample.txt')
polymerTemplate = goNSteps(polymerTemplate, pairInsertionRules, 1)
counter = numberOfElements(polymerTemplate)
print(counter)




