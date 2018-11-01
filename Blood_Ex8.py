import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


### Problem 1
data = pd.read_table('UWvMSU_1-22-13.txt')
times = list(data['time'])

UW = data.copy()
del UW['team']
UW.iloc[0,1] = 0
UW.iloc[-1,1] = 0
MSU = data.copy()
del MSU['team']
MSU.iloc[0,1] = 0
MSU.iloc[-1,1] = 0

for i,time in enumerate(times):
    if data.iloc[i,1]=='UW':
        UW.iloc[i,1] = UW.iloc[i-1,1]+ data.iloc[i,2]
        MSU.iloc[i,1] = MSU.iloc[i-1,1]
    else:
        UW.iloc[i,1] = UW.iloc[i-1,1]
        MSU.iloc[i,1] = MSU.iloc[i-1,1]+ data.iloc[i,2]

plt.figure()
plt.plot(times,UW.iloc[:,1],'r-',times,MSU.iloc[:,1],'g-')


### Problem 2
import random as random
def rander():
    num = random.randint(1,100)
    print num
    print "Guess an integer between 1 and 100 inclusive"
    print "Guess:  "
    guess = input()
    guess = int(guess)
    while guess != num:
        print "num ", num
        print "guess ", guess
        if guess<num:
            print "Higher"
        else:
            print "Lower"
        print "Guess:  "
        guess = input()
        guess = int(guess)
    print "You got it!"
rander()
