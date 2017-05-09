from random import randint,shuffle
import random

kidsandteachers=['K','K','K','K','K','K','K','K','K','K','K','K','T','T','T']

success=0
trials=10000
print(len(kidsandteachers[0]+kidsandteachers[1]+kidsandteachers[2]))
for i in range(trials):
    
    
    shuffle(kidsandteachers)
    print(kidsandteachers)
    numberofKTK=0
    for j in range(13):
        if (kidsandteachers[j]+kidsandteachers[j+1]+kidsandteachers[j+2])=='KTK':
            numberofKTK+=1
            if numberofKTK==3:
                success+=1
                print('success: '+str(success))

print ("successes: "+str(success))        
print((success)/trials*100,'%')
