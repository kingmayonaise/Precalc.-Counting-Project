from random import randint,shuffle
import random

cards=['K','K','K','K','Q','Q','Q','Q','J','J','J','J']

failure=0
trials=10

for i in range(trials):
    
    
    shuffle(cards)
    print(cards)
    cards_concat=''.join(cards)
    if ('KKKK' in cards_concat) or \
            ('JJJJ' in cards_concat) or\
            ('QQQQ' in cards_concat):
            failure+=1
            print('failure')

print((trials-failure)/trials*100,'%')


"""
kidsandteachers=['K','K','K','K','K','K','K','K','K','K','K','K','T','T','T']

success=0
trials=10
for i in range(trials):
    
    
    shuffle(kidsandteachers)
    print (kidsandteachers)
    numberofKTK=0
    for j in range(11):
        if (kidsandteachers[j]+kidsandteachers[j+1]+kidsandteachers[j+2]+ \
                            kidsandteachers[j+3]+kidsandteachers[j+4])=='KKTKK':
            numberofKTK+=1
            if numberofKTK==3:
                numberofKTK=0
                success+=1
                print('success')

print((success)/trials*100,'%')
"""

"""
siblings=[1,1,2,2,3,3,4,4,5,5]

trials=10000
paircounters=[0,0,0,0,0]
for i in range(trials):
    paircount=0
    shuffle(siblings)
    #print(siblings)
    for j in range(9):
        if (int(str(siblings[j])+str(siblings[j+1]))%11)==0:
           paircount+=1

    if paircount>0:
        #print(str(paircount)+' pairs')
        paircounters[paircount-1]+=1
print('Expected value: '+str(((paircounters[0]/trials)*1)+((paircounters[1]/trials)*2)+((paircounters[2]/trials)*3) \
                                    +((paircounters[3]/trials)*4)+((paircounters[4]/trials)*5)))


print ('1 pairs '+str(paircounters[0]/trials))
print ('2 pairs '+str(paircounters[1]/trials))
print ('3 pairs '+str(paircounters[2]/trials))
print ('4 pairs '+str(paircounters[3]/trials))
print ('5 pairs '+str(paircounters[4]/trials))
"""
    
    
    
    
