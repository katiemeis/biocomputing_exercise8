#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 10:58:07 2018

@author: Mac
"""

#Question 1: Plotting sports data

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('UWvMSU_1-22-13.txt', sep = '\t')
out = pd.DataFrame(columns=['time','scoreMSU','scoreUW'])

scoreMSU = 0
scoreUW = 0

for i in range(0,len(data)):
    if data.team.iloc[i] == 'UW':
        scoreUW += data.score[i]
        out.loc[len(out)]=[data.time[i],scoreMSU,scoreUW]
    elif data.team.iloc[i] == 'MSU':
        scoreMSU += data.score[i]
        out.loc[len(out)]=[data.time[i],scoreMSU,scoreUW]
        
plt.plot(out.time,out.scoreMSU,'g-',out.time,out.scoreUW,'r-')

#Question 2: Guess this number!
import random
num = random.randint(1,100)
guess = 0

while guess != num:
    guess = input("Please enter a number between 1 and 100: ")
    if (guess > num):
        print("too high")
    elif (guess < num):
        print("too low")
    else:
        print("got it!")
        break