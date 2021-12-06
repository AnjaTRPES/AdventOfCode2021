# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 09:28:44 2021

@author: Anja
"""

import numpy as np
import pandas as pd

df = pd.read_csv('sample.txt', sep=' ', names=['motion', 'value'])


def get_total_forward(df):
    forward = df[df['motion']=='forward'].value.sum()
    return forward

def get_total_down(df):
    down = df[df['motion'] == 'down'].value.sum()
    return down

def get_total_up(df):
    up = df[df['motion'] == 'up'].value.sum()
    return up

def get_depth(df):
    return get_total_down(df) - get_total_up(df)

def get_multiplicator(df):
    return get_total_forward(df)*get_depth(df)

f = get_total_forward(df)
print('forward', f, 'depth', get_depth(df))
print('multiplicator ', get_multiplicator(df))

df2 = pd.read_csv('input.txt', sep=' ', names=['motion', 'value'])
print('multiplicator ', get_multiplicator(df2))




