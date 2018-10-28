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
numberchoice=numpy.random.choice(list)
def numbergame():
    print ('Im thinking of a number 1-100...')
    user_guess=int(raw_input('guess:'))
    while user_guess!=numberchoice:
        if user_guess > numberchoice:
            print ('Lower')
            user_guess=int(raw_input('guess:'))
        elif user_guess < numberchoice:
            print ('Higher')
            user_guess=int(raw_input('guess:'))    
    if user_guess==numberchoice:
        print ('Correct!')

numbergame()


        


     
    
      
    











    
        












