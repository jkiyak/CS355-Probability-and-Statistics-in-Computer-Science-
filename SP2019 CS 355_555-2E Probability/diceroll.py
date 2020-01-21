import random

def diceroll(numberofrolls):

    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    
    for i in range(numberofrolls):
        x = random.randint(0,9)
        if (x >= 0 and x <=1):
            one = one + 1
        elif (x>= 1 and x <= 3):
            two = two + 1
        elif (x>= 3 and x <= 4):
            three = three + 1
        elif (x>= 4 and x <= 6):
            four = four + 1
        elif (x>= 6 and x <= 7):
            five = five + 1
        elif (x>= 7 and x <= 9):
            six = six + 1

    lessthanfour = (one + two + three) / numberofrolls
    print("The probability for each roll to be less than 4 are")
    print(lessthanfour * 100)


diceroll(10)
diceroll(100)
diceroll(1000)
diceroll(10000)
diceroll(100000)
      
