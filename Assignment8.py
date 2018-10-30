# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 10:51:24 2018

@author: Patrick
"""

#Number 1
import pandas as pd
scoring=pd.read_table('UWvsMSU_1-22-13.txt',header=0,delim_whitespace=True, names=('time','team','score'))
UWscore=0
UWpoints=[]
UWtime=[]
MSUscore=0
MSUpoints=[]
MSUtime=[]
for i in range(0,len(scoring.time)):
    if scoring.team[i]=='UW':
        UWscore+=scoring.score[i]
        UWpoints.append(UWscore)
        time=scoring.time[i]
        UWtime.append(time)
    elif scoring.team[i]=='MSU':
        MSUscore+=scoring.score[i]
        MSUpoints.append(MSUscore)
        time=scoring.time[i]
        MSUtime.append(time)
        
import matplotlib.pyplot as plt
plt.plot(UWtime,UWpoints,'r-')
plt.plot(MSUtime,MSUpoints,'g-')
plt.show()

#Number 2
import random
num=random.randint(1,101)
print ("I'm thinking of a number 1-100...")
while guess != num:
    guess=input()
    guess = int(guess)
    if guess>num:
        print ('lower')    
    elif guess<num:
        print ('higher')
    elif guess==num:
        print ('Correct!')

        
