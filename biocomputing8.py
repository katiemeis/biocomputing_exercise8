#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 14:00:31 2018

@author: charrington
"""
# 1
import pandas
scores=pandas.read_csv("UWvMSU_1-22-13.txt",header=0,sep="\t")

scoresframe=pandas.DataFrame(columns=['time','UW','MSU'])

UWscore=0
MSUscore=0


for i in range(0,len(scores)):
    if scores.iloc[i,1]=="UW":
        UWscore+=scores.iloc[i,2]
    else:
        MSUscore+=scores.iloc[i,2]
        
    scoresframe.loc[len(scoresframe)]=[scores.iloc[i,0],UWscore,MSUscore]
    
    
import matplotlib.pyplot as plt
plt.plot(time,UWscore,'r-',time,MSUscore,'g-')

#2 guess my number

import numpy

list=range(1,100)
user_guess=0

def numbergame():
    numberchoice=numpy.random.choice(list)
    print ('Im thinking of a number 1-100...')
    user_guess=raw_imput('guess:')
    while user_guess!=numberchoice:
        if user_guess > numberchoice:
            print ('Lower')
        elif user_guess < numberchoice:
            print ('Lower')
        else:
            print ('Correct!')
    
numbergame()









    
        












