from random import randint,shuffle
import random

cards=['K','K','K','K','Q','Q','Q','Q','J','J','J','J']

success=0
trials=10000

for i in range(trials):
    
    
    shuffle(cards)
    print(cards)
    for j in range(4):
        if (cards[j]+cards[j+1]+cards[j+2]+cards[j+3]=='KKKK') \
                or (cards[j]+cards[j+1]+cards[j+2]+cards[j+3]=='QQQQ') \
                or (cards[j]+cards[j+1]+cards[j+2]+cards[j+3]=='JJJJ'):
            print('success')
            success+=1
            break
        
print((trials-success)/trials*100,'%')
