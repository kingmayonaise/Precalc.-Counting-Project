from random import randint,shuffle
import random

cards=['K','K','K','K','Q','Q','Q','Q','J','J','J','J']

failures=0
trials=10

for i in range(trials):
    
    
    shuffle(cards)
    print(cards)
    for j in range(4):
        if cards[j]+cards[j+1]+cards[j+2]+cards[j+3]=='KKKK'or'QQQQ'or'JJJJ':
            print('failure')
            #failures+=1
            #break
        
#print((trials-failures)/trials*100,'%')
