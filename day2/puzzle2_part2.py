# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 09:28:44 2021

@author: Anja
"""

import numpy as np
import pandas as pd

df = pd.read_csv('sample.txt', sep=' ', names=['motion', 'value'])

def get_multiplicator(df):
    horizontal = 0
    depth = 0
    aim = 0
    for i in range(df.shape[0]):
        if df.motion[i] == 'forward':
            horizontal += df.value[i]
            depth += aim*df.value[i]
        elif df.motion[i] == 'down':
            aim += df.value[i]
        elif df.motion[i] == 'up':
            aim -= df.value[i]
        print('motion: ', df.motion[i], 'hor=', horizontal, 'd=', depth)
    return horizontal*depth



print(get_multiplicator(df))


df2 = pd.read_csv('input.txt', sep=' ', names=['motion', 'value'])


print(get_multiplicator(df2))


