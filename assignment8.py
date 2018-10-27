#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 10:31:24 2018

@author: lcampbe3

exercise 8
"""

#1
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_table("UWvMSU_1-22-13.txt",header=0, sep="\t")

UW_score=0
MSU_score=0

scores=pd.DataFrame(columns=['time','UW', 'MSU'])

for i in range(0, len(data)):
    if data.iloc[i,1] == "UW":
        UW_score += data.iloc[i,2]
        
    else:
        MSU_score += data.iloc[i,2]
        
    scores.loc[len(scores)]=[data.iloc[i,0], UW_score, MSU_score]

plt.plot(scores.time, scores.UW,'-r', scores.time, scores.MSU, '-g')


#2
import random

user_guess=-1
num=random.randint(0,100)

print("I'm thinking of a number 1-100...")
print(num)

while(True):
    user_guess = raw_input('Guess: ')
    user_guess = int(user_guess)
    
    if user_guess < num:
        print("Higher")
        
    elif user_guess > num:
        print("Lower")
        
    else:
        print("Correct!")
        break


         