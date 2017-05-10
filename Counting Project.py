from random import randint,shuffle
import random
"""
cards=['K','K','K','K','Q','Q','Q','Q','J','J','J','J']

success=0
trials=10000

for i in range(trials):
    
    
    shuffle(cards)
    cards_concat=''.join(cards)
  #  print(cards)
    if ('KKKK' in cards_concat) or \
            ('JJJJ' in cards_concat) or\
            ('QQQQ' in cards_concat):
            success+=1
#            print('success: '+str(success))

#print ("successes: "+str(success))        
#print((trials-success)/trials*100,'%')
"""

kidsandteachers=['K','K','K','K','K','K','K','K','K','K','K','K','T','T','T']

success=0
trials=10000
for i in range(trials):
    
    
    shuffle(kidsandteachers)
    print(''.join(kidsandteachers))
    numberofKTK=0
    for j in range(11):
        if (kidsandteachers[j]+kidsandteachers[j+1]+kidsandteachers[j+2]+kidsandteachers[j+3]+kidsandteachers[j+4])=='KKTKK':
            numberofKTK+=1
            if numberofKTK==3:
                numberofKTK=0
                success+=1
                print('success: '+str(success))

print ("successes: "+str(success))        
print((success)/trials*100,'%')

"""
pairs=[1,1,2,2,3,3,4,4,5,5]


success=0
trials=10
for i in range(trials):
    
    shuffle(pairs)
   # print(pairs)
    for j in range(8):
        if (int(str(pairs[j])+str(pairs[j+1]))%11)==0:
         #   print('pair')
    """
    
    
    
    
