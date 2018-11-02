#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 11:03:17 2018

@author: stephaniearaki
"""
#Question 1: Use score by score info to generate graph 
cd Desktop/biocomputing_exercise8
import pandas as pd
game=pd.read_csv('UWvMSU_1-22-13.txt', header=0, sep='\t')

out=pd.DataFrame(columns=['time','UWscore','MSUscore'])

MSUscore=0
UWscore=0

for i in range(1,len(game)):
    if game.iloc[i,1]=='UW':
        time=game.iloc[i,0]
        UWscore=UWscore+game.iloc[i,2]
        out=out.append({'time':time,'UWscore':UWscore, 'MSUscore':MSUscore},ignore_index=True)
    else:
        time=game.iloc[i,0]
        MSUscore=MSUscore+game.iloc[i,2]
        out=out.append({'time':time,'UWscore':UWscore, 'MSUscore':MSUscore},ignore_index=True)

import matplotlib.pyplot as plt

plt.plot('time','UWscore',data=out)
plt.plot('time', 'MSUscore',data=out)

plt.plot('time','UWscore','r-',data=out)
plt.plot('time','MSUscore','g-',data=out)

plt.plot('time','UWscore','r-','MSUscore','g-',data=out)
#did not work so could not graph together, but could graph separately


#Question 2: Write a game called guess my number

import numpy as np
randomnumber=np.random.choice(100,1)

guess=int(raw_input("I'm thinking of a number 1-100, what is your guess?"))

while randomnumber != 'guess':
    print
    if guess>randomnumber:
        print "Lower"
        guess=int(raw_input("I'm thinking of a number 1-100, what is your guess?"))
    elif guess<randomnumber:
        print "Higher"
        guess=int(raw_input("I'm thinking of a number 1-100, what is your guess?"))
    else:
        print "Correct!"
        break
    print
        
    