# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 17:39:32 2021

@author: Anja
"""

import numpy as np
import pandas as pd

def get_powerCons(filename):
    file1 = open(filename, 'r')
    Lines = file1.readlines()
    file1.close()
    
    sums = np.zeros(len(Lines[0])-1)
    
    for line in Lines:
        for i, chara in enumerate(line.split('\n')[0]):
            sums[i] += int(chara)
            
    # transform to binary
    gamma = ''
    epsilon = ''
    
    for s in sums:
        if s > len(Lines)/2:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    power_cons = gamma* epsilon
    print(power_cons)

get_powerCons('sample.txt')
get_powerCons('input.txt')

def get_oxygen_cons(filename):
    file1 = open(filename, 'r')
    Lines = file1.readlines()
    file1.close()
    
    pos = 0
    while len(Lines) != 1:
        # which is the most common bit?
        N1 = 0
        for line in Lines:
            N1 += int(line[pos])
        
        if N1 >= len(Lines)/2:
            commonBit = '1'
        else:
            commonBit = '0'
        #print('most common Bit', commonBit)
        #delete those with that bit
        for n in range(len(Lines)-1, -1, -1):
            if (Lines[n][pos] != commonBit):
                Lines.pop(n)
        pos += 1
        #print('len of lines', len(Lines))
    return int(Lines[0], 2)

def get_co2_scrub(filename):
    file1 = open(filename, 'r')
    Lines = file1.readlines()
    file1.close()
    
    pos = 0
    while len(Lines) != 1:
        # which is the most common bit?
        N1 = 0
        for line in Lines:
            N1 += int(line[pos])
        
        if N1 >= len(Lines)/2:
            commonBit = '1'
        else:
            commonBit = '0'
        #print('most common Bit', commonBit)
        #delete those with that bit
        for n in range(len(Lines)-1, -1, -1):
            if (Lines[n][pos] == commonBit):
                Lines.pop(n)
        pos += 1
        #print('len of lines', len(Lines))
    return int(Lines[0], 2)

ox = get_oxygen_cons('input.txt') 
scrub = get_co2_scrub('input.txt')   
print(ox*scrub)    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        