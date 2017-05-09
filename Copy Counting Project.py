from random import randint,shuffle
import random

kidsandteachers=['K','K','K','K','K','K','K','K','K','K','K','K','T','T','T']

success=0
trials=10
print(len(kidsandteachers[0]+kidsandteachers[1]+kidsandteachers[2]))
for i in range(trials):
    
    
    shuffle(kidsandteachers)
    print(kidsandteachers)
    for j in range(13):
        if (len(kidsandteachers[j]+kidsandteachers[j+1]+kidsandteachers[j+2]=='KTK')==9):
            success+=1
            print('success: '+str(success))

print ("successes: "+str(success))        
print((success)/trials*100,'%')
