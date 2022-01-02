# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 11:04:32 2021

@author: Anja
"""
import time

f = open('input.txt')
lines = f.readlines()
f.close()

w = 0
x = 0
y = 0
z = 0

instructions = []
for line in lines:
    line = line.rstrip()
    chunks = line.split(' ')
    instructions.append(chunks)



# a fourteen digit model number.. all varying between 9 and 1. 
for test in ['13579246899999']: # range(99999999999999, -1, -1): # ['13579246899999']:# 
    start = time.time()  
    modelNumber = str(test)
    if '0' not in modelNumber:
        inputCounter = 0
        values = {'x': 0, 'y': 0, 'z': 0, 'w': 0}
        
        for chunks in instructions:
            if chunks[0] == 'inp':
                values[chunks[1]] = int(modelNumber[inputCounter])
                inputCounter += 1
                #print('input:',  values[chunks[1]])
            else:
                try:
                    b = int(chunks[2])
                except ValueError:
                    b = values[chunks[2]]
                if chunks[0] == 'add':
                    values[chunks[1]] += b
                elif chunks[0] == 'mul':
                    values[chunks[1]] *= b
                elif chunks[0] == 'mod':
                    values[chunks[1]] = values[chunks[1]] % b
                elif chunks[0] == 'eql':
                    if values[chunks[1]] == b:
                        values[chunks[1]] = 1
                    else:
                        values[chunks[1]] = 0
            #print('line: ', line, '\n', values)
        print(modelNumber)
        if values['z'] == 0:
            print('found valid model number! ', modelNumber)
            break
        end = time.time()
        print('this took:', end-start)
print('to check all numbers: ', (end-start)*(99999999999999)/(60*60), 'h')
        
        
        
        
        
        
        
        
