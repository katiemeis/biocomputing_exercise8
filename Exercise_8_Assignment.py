#Problem 1:

import pandas as pd
import matplotlib.pyplot as pyplot
game_data = pd.read_csv("UWvMSU_1-22-13.txt", sep = "\t")
game_dataframe = pd.DataFrame(columns=["time","MSUscore","UWscore"])
MSUscore = 0
UWscore = 0
for i in range(0,len(game_data)):
    if (game_data.team.iloc[i] == "UW"):
        UWscore += game_data.score[i]
        game_dataframe.loc[len(game_dataframe)]=[game_data.time[i],MSUscore,UWscore]
    elif (game_data.team.iloc[i] == "MSU"):
        MSUscore += game_data.score[i]
        game_dataframe.loc[len(game_dataframe)]=[game_data.time[i],MSUscore,UWscore]
        
pyplot.plot(game_dataframe.time,game_dataframe.MSUscore,"g-",game_dataframe.time,game_dataframe.UWscore,"r-")

#Problem 2

import random
number = random.randint(1,101)
guess = 0
while guess != number:
    print("Please enter a number between 1 and 100: ")
    guess = int(input())
    if (guess > number):
        print("Lower!")
    elif (guess < number):
        print("Higher!")
    else:
        print("Correct!")
        break