#Exercise 8 

import pandas as pd
UWvMSU=pd.read_csv('UWvMSu_1-22-13.txt', header=0, sep="\t")
print(UWvMSU)

#done
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
print(score)


import matplotlib.pyplot as plt

fig=plt.pyplot.figure(figsize=(3.0,3.0))
axes1 = fig.add_subplot(1, 1, 1)
axes1.set_ylabel('y-axis')
axes1.set_xlabel('x-axis')
axes1.plot(score)
fig.tight_layout()
plt.pyplot.show()



plt.plot(time,UWscore,'r-',time,MSUscore,'g-')





































































