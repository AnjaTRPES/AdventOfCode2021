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

inputs = []
instructions = []
for line in lines:
    line = line.rstrip()
    chunks = line.split(' ')
    if chunks[0] == 'inp':
        inputs.append(instructions)
        instructions = []
    instructions.append(chunks)
inputs.append(instructions)
inputs.pop(0)  


'''
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
                elif chunks[0] == 'div':
                    values[chunks[1]] = int(values[chunks[1]]/b)
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
'''

for test in [95299897999897]:# not valid, it said it is too high??
    test = str(test)
    if '0' not in test: 
        if int(test[3]) == int(test[4]):
            if int(test[5]) + 1 == int(test[6]):
                if int(test[7]) + 2 == int(test[8]):
                    if int(test[2]) + 7 == int(test[9]):
                        if int(test[10]) - 1 == int(test[11]):
                            if int(test[1]) + 4 == int(test[12]):
                                if int(test[0]) - 2 == int(test[13]):
                                    print('found one:', test)
                                    break
    if int(test)%100000 == 0:
        print(test)

# The instructions:
# Start: zi: 0
# Input 0: z0: zi*26+inp0+7
# Input 1: z1: z0*26+inp1+8
# Input 2: z2: z1*26+inp2+16
# Input 3: z3: z2*26+inp3+8
# Input 4: z4: z2             if inp3 == inp4
# Input 5: z5: z4*26+inp5+12 
# Input 6: z6: z4             if inp5-1 == inp6
# Input 7: z7: z6*26+inp7+8
# Input 8: z8: z6             if inp7+2 == inp8
# Input 9: z9: z1             if inp2+7 == inp9
# Input 10: z10: z9*26+inp10+4
# Input 11: z11: z9           if inp10 -1 == inp11
# Input 12: z12: z0           if inp1+4 == inp12
# Input 13: z13: 0            if inp0-2 == inp13

# resulted in highest number: 95299987999897 => was not accepted. 
# Rechecking puzzle input
# Input 0: z0: zi*26+inp0+7
# Input 1: z1: z0*26+inp1+8
# Input 2: z2: z1*26+inp2+16
# Input 3: z3: z2*26+inp3+8
# Input 4: z4: z2             if inp3 == inp4
# Input 5: z5: z2*26+inp5+12 
# Input 6: z6: z2             if inp5+1 == inp6 # error here!
# Input 7: z7: z2*26+inp7+8
# Input 8: z8: z2             if inp7+2 == inp8
# Input 9: z9: z1             if inp2+7 == inp9
# Input 10: z10: z1*26+inp10+4
# Input 11: z11: z1           if inp10 -1 == inp11
# Input 12: z12: z0           if inp1+4 == inp12
# Input 13: z13: 0            if inp0-2 == inp13

'''
# In equations:
inp0 = inp13 + 2 # inp0= 9, inp13 = 7
inp1 = inp12 - 4 # inp12= 9, inp1 = 5
inp2 = inp9 - 7  # inp9=9, inp2=2
inp3 = inp4 # both must be 9
inp5 = inp6 - 1 # inp6=9, inp5=8
inp7 = inp8 - 2 # inp8=9, inp7=7
inp10 = inp11+1 # inp10=9, inp11 = 8
#MN: 95299897999897
'''









