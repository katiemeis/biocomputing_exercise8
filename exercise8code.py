# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 10:57:41 2018

@author: Cole
"""

# this code corresponds to the solutions for Biocomputing exercise 8 due 11/2/18


# part 1:
# using the score-by-score information from this game summarized in 
# "UWvMSU_1-22-13.txt", generate a graph that shows the cumulative score progression over the length of the game for both teams

import pandas as pd

gameData=pd.read_csv('UWvMSU_1-22-13.txt',header=0,sep='\t')

UWout=pd.DataFrame(columns=['time','cumScore'])
MSUout=pd.DataFrame(columns=['time','cumScore'])

cumMSU=0 # set a starting point for the game score
cumUW=0 # for both teams

countMSU=1
countUW=1

for i in range(0,len(gameData.time)): # step through for the whole game
    if gameData.team[i]=='MSU': # step through all the MSU scores first
        cumMSU=cumMSU+gameData.score[i] # add to the cumulative score
        MSUout.loc[countMSU]=[gameData.time[i],cumMSU] #  save the time and cumScore data
        countMSU=countMSU+1
    
    elif gameData.team[i]=='UW':
        cumUW=cumUW+gameData.score[i]
        UWout.loc[countUW]=[gameData.time[i],cumUW]
        countUW=countUW+1
        
# plotting
import matplotlib.pyplot as plt


plt.plot(UWout.time,UWout.cumScore,'r-',MSUout.time,MSUout.cumScore,'g-')        

# part 2:
# write a game called "guess my number"
# the computer will generate a random number between 1 and 100
# the user types in a number and the computer replies either "Lower", "Higher", or "Correct"
# player keeps guessing until they guess correctly

import numpy as np

val=np.random.choice(99)+1 # 0 base indexing, so go up to 99 and then add one
# this ensures that the value is between 1-100 and does not contain 0

print("I'm thinking of a number 1-100...")

guess=input("Guess: ")

while guess!=val:
    if guess>val:
        print "Lower"
    elif guess<val:
        print "Higher"
        
    guess=input("Guess: ")

    
# when you exit the loop, the value is correct
print "Correct!"    










