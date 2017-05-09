from random import randint,shuffle
import random


for i in range(trials):
    
    
    shuffle(kidsandteachers)
    kandt_concat=''.join(kidsandteachers)
    print(kandt_concat)
    if kandt_concat.count('KTK')==3:
            success+=1
            print('success: '+str(success))

print ("successes: "+str(success))        
print((success)/trials*100,'%')
