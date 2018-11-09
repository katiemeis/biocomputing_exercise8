#Exercise 8 

#Number 1
import pandas as pd
UWvMSU=pd.read_csv('UWvMSu_1-22-13.txt', header=0, sep="\t")

score=pd.DataFrame(columns=['time', 'UWscore', 'MSUscore'])
MSUscore=0
UWscore=0
for i in range(1,len(UWvMSU)):
    if UWvMSU.iloc[i,1]=='UW':
        time=UWvMSU.iloc[i,0]
        UWscore=UWscore+UWvMSU.iloc[i,2]
        score=score.append({'time':time, 'UWscore':UWscore, 'MSUscore':MSUscore},ignore_index=True)
    else:
        time=UWvMSU.iloc[i,0]
        MSUscore=MSUscore+UWvMSU.iloc[i,2]
        score=score.append({'time':time,'UWscore':UWscore, 'MSUscore':MSUscore},ignore_index=True)
score.head(10)

import matplotlib.pyplot as plt

plt.plot('time','UWscore',data=score)
plt.plot('time', 'MSUscore', data=score)

#Number 2
import numpy as np
number=np.random.choice(100,1)
i='False' 
 
while i =='False':
    guess=raw_input("I'm thinking of a number 1-100, whats your guess?")
    guessint=int(guess)
   
    if guessint>number:
        print("Guess Lower")
    elif guessint<number:
        print("Guess Higher")
    else:
        print("Correct!")
        i='True'  
    
    

















































