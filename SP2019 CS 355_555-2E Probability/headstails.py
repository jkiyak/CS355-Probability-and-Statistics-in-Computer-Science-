import random


number = 10
heads = 0
tails = 0

for i in range(number):
    probability = random.randint(0,100)
    if (probability >= 0 and probability <= 75):
        heads +=1
    else:
        tails+=1

print(heads)
print(tails)
headpercent = float(heads/number)
print("The percentage of heads is" , + headpercent * 100, "percent")
