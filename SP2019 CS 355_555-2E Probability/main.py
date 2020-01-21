import random

def florist(days):
    r1c1 = 0
    r1c2 = 0
    r1c3 = 0
    r2c1 = 0
    r2c2 = 0
    r2c3 = 0
    r3c1 = 0
    r3c2 = 0
    r3c3 = 0
    totalRose = 0
    totalCard = 0
        
    for i in range(days):
        print("Day" + str(i + 1))
        for i in range(101):
            customer = random.randint(1,101)
            if (customer  <= 40):
                r1c1 = r1c1 + 1
                totalRose = totalRose + 1
                totalCard = totalCard + 1
            
            elif (customer > 40 and customer <= 60):
                r1c2 = r1c2 + 1
                totalRose = totalRose + 6
                totalCard = totalCard + 1
                
            elif (customer > 60 and customer <= 70):
                r1c3 = r1c3 + 1
                totalRose = totalRose + 12
                totalCard = totalCard + 1
                
            elif (customer > 70 and customer <= 75):
                r2c1 = r2c1 + 1
                totalRose = totalRose + 1
                totalCard = totalCard + 2
                
            elif (customer > 75 and customer <= 82):
                r2c2 = r2c2 + 1
                totalRose = totalRose + 6
                totalCard = totalCard + 2
                
            elif (customer > 82 and customer <= 95):
                r2c3 = r2c3 + 1
                totalRose = totalRose + 12
                totalCard = totalCard + 2
        
            
            elif(customer == 96):
                r3c1 = r3c1 + 1
                totalRose = totalRose + 1
                totalCard = totalCard + 3
            elif (customer == 97):
                r3c2 = r3c2 + 1
                totalRose = totalRose + 6
                totalCard = totalCard + 3
            else:
                r3c3 = r3c2 + 1
                totalRose = totalRose + 12
                totalCard = totalCard + 3
            
            print(r1c1)
            print(r1c2)
            print(r1c3)
            print(r2c1)
            print(r2c2)
            print(r2c3)
            print(r3c1)
            print(r3c2)
            print(r3c3)
            
            print("Total Roses sold is " + str(totalRose))
            print("Total Gift Cards sold is " + str(totalCard))


florist(10)
            
                
            