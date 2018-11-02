# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 10:20:42 2018

@author: bretl
"""

#question 1
import numpy as np
from plotnine import *
import pandas as pd
score=pd.read_csv('UWvMSU_1-22-13.txt',header=0,sep='\t')

cumscores = (score.groupby(by=['team','time']).sum().groupby(level=[0]).cumsum())

cumscorebyteam=cumscores.reset_index(level=['team', 'time'])

a = ggplot(cumscorebyteam, aes(x='time', y='score', color='team'))
a+geom_line()


#Question 2
import random
randy=random.randint(1,100)
guess=int(raw_input("Enter a number between 1 and 100. If you are wrong, drop out of grad school."))
while randy != "guess":
    print
    if guess < randy:
        print"Too low. Grad school isn't looking great..."
        guess = int(raw_input("Enter a number between 1 and 100. If you are wrong, drop out of grad school"))
    elif guess > randy: 
        print "Too high. What are you doing here?"
        guess = int(raw_input("Enter a number between 1 and 100. If you are wrong, drop out of grad school"))
    else:
        print"Correct! But still what are you doing here??"
        break
    print
