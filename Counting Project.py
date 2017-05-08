from random import randint,shuffle
import random

cards=['K','K','K','K','Q','Q','Q','Q','J','J','J','J']

failures=0
trials=10

for i in range(trials):
    
    
    shuffle(cards)
    for j in range(11):
        print(cards)
            #failures+=1
            #break
        
#print((trials-failures)/trials*100,'%')