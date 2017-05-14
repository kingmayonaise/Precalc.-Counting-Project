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


kidsandteachers=['K','K','K','K','K','K','K','K','K','K','K','K','T','T','T']

success=0
trials=10000
for i in range(trials):
    
    
    shuffle(kidsandteachers)
    #print(''.join(kidsandteachers))
    numberofKTK=0
    for j in range(11):
        if (kidsandteachers[j]+kidsandteachers[j+1]+kidsandteachers[j+2]+kidsandteachers[j+3]+kidsandteachers[j+4])=='KKTKK':
            numberofKTK+=1
            if numberofKTK==3:
                numberofKTK=0
                success+=1
                #print('success: '+str(success))

print ("successes: "+str(success))        
print((success)/trials*100,'%')
"""

pairs=[1,1,2,2,3,3,4,4,5,5]


success=0
trials=10
paircount=0
onepair=0
twopair=0
threepair=0
fourpair=0
fivepair=0
for i in range(trials):
    paircount=0
    shuffle(pairs)
    print(pairs)
    for j in range(8):
        if (int(str(pairs[j])+str(pairs[j+1]))%11)==0:
           paircount+=1
           print('pair')
    if paircount==1:
        onepair+=1
    elif paircount==2:
        twopair+=1
    elif paircount==3:
        threepair+=1
    elif paircount==4:
        fourpair+=1
    elif paircount==5:
        fivepair+=1
print(onepair,twopair,threepair,fourpair,fivepair)
print((onepair*((22680/1134000)*1))+(twopair*((5040/1134000)*2))+(threepair*((1260/1134000)*3))+(fourpair*((360/1134000)*4))+(fivepair*((120/1134000)*5)))


    
    
    
    
