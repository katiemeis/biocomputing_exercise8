#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 14:00:31 2018

@author: charrington
"""

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
    
    
    