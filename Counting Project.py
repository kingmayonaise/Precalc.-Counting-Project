from random import randint,shuffle
import random

cards=['K','K','K','K','Q','Q','Q','Q','J','J','J','J']

success=0
trials=1000

for i in range(trials):
    
    
    shuffle(cards)
    cards_concat=''.join(cards)
    print(cards)
    if ('KKKK' in cards_concat) or \
            ('JJJJ' in cards_concat) or\
            ('QQQQ' in cards_concat):
            success+=1
            print('success: '+str(success))

print ("successes: "+str(success))        
print((trials-success)/trials*100,'%')
