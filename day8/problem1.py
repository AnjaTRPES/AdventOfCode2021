# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 12:58:29 2021

@author: Anja
"""

class entry:
    def __init__(self, segments, output):
        self.segments = segments
        self.output = output
     
    def __str__(self):
        return str(self.segments) + '|' + str(self.output)


def loadFile(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    entries =  []
    for line in lines:
        splitted = line[:-1].split(' | ')
        entries.append(entry(splitted[0].split(' '), splitted[1].split(' ')))
    return entries

def getEasyDigits(entries):
    Neasy = 0
    for entry in entries:
        #print(entry)
        for o in entry.output:
            if len(o) in [2, 3, 4, 7]:
                #print(o)
                Neasy += 1
    return Neasy

entries = loadFile('input.txt')
print('Neasy', getEasyDigits(entries))
