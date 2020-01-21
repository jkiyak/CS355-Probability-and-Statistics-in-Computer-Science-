import matplotlib.pyplot as plt
import numpy as np
import random

A = [] # create an empty list for player A
B = [] # create an empty list for player A
C = [] # create an empty list for player A

for _ in range(30):
# create a bias of 70% chance
    if random.random() <= 0.7:
        A.append(1)
    else:
        A.append(0)

for _ in range(20):
# create a bias of 60% chance
    if random.random() <= 0.6:
        B.append(1)
    else:
        B.append(0)

for _ in range(10):
# create a bias of 50% chance
    if random.random() <= 0.5:
        C.append(1)
    else:
        C.append(0)

A_shots=sum(A)
B_shots=sum(B)
C_shots=sum(C)

print(A)
print(B)
print(C)
print(A_shots)
print(B_shots)
print(C_shots)


x = np.arange(3)
plt.bar(x, height= [30,20,10])

plt.xticks(x, ['PlayerA','PlayerB','PlayerC'])
plt.show()
