##problem 16

import random

rolls = 10
success = 0
failure = 0





for i in range(rolls):
 coinchoice = random.randint(1,3)
 if (coinchoice == 1): ##heads in both faces
   failure = failure+1
 elif (coinchoice == 2): ##heads and tails
   success = success+1
 elif (coinchoice == 3): ##tails on both faces
   failure = failure+1

 probability = (success / failure)

print("The probability is", probability * 100)



##problem 22
k = 5
m = 10
n = 5

for i in range(k):
  k = k-1
  total = (m+n+1)


probability = m / total
print("The probability is" , probability)
