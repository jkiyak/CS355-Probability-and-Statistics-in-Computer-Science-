import random


## A = heads then tails
## B = tails then heads


def main():
    heads = 0
    coinflips = 0
    tails = 0
    p = 65 ##probablity of heads
    while coinflips <= 1:
        if random.randint(1,100) < p:
            print("Heads")
            heads += 1
            coinflips += 1  
        else:
            tails += 1
            coinflips += 1
            print("Tails")

    if heads == 2 or tails == 2:  ##double or tails = reroll
        print ("Reroll!")
        
   
    ## heads then tails = playerA wins
    ## tails then heads = playerB wins

main()





        
