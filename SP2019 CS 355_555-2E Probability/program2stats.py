import random
import statistics

def main():
    cars = 10000 ##change car variable here
    minutes = 0
    my_randoms = []
    dictionary = {}
    dictionary['AB'] = 5
    dictionary['AC'] = 6
    dictionary['BD'] = 4
    dictionary['BE'] = 7
    dictionary['CE'] = 4
    dictionary['CF'] = 6
    dictionary['DG'] = 4
    dictionary['DH'] = 6
    dictionary['EH'] = 6
    dictionary['EI'] = 4
    dictionary['FI'] = 3
    dictionary['FJ'] = 7
    dictionary['GK'] = 4
    dictionary['HK'] = 4
    dictionary['HL'] = 8
    dictionary['IL'] = 6
    dictionary['IM'] = 4
    dictionary['JM'] = 5
    dictionary['KN'] = 4
    dictionary['LN'] = 5
    dictionary['LO'] = 6
    dictionary['MO'] = 5
    dictionary['NP'] = 5
    dictionary['OP'] = 5

    for z in range(0,1): ##change the second option to how many times you want to change
        for x in range(cars):
            for y in range(0,16):
                minutes = 0
                my_randoms = random.sample(range(0, 100), 15)
                if (my_randoms[0] in range(0,10)):
                    minutes =  minutes  + dictionary.get('AB')
                elif (my_randoms[0] in range(11,100)):
                    minutes = minutes + dictionary.get('AC')

                if (my_randoms[1] in range(0,20)):
                    minutes =  minutes  + dictionary.get('BD')
                elif (my_randoms[1] in range(21,100)):
                    minutes = minutes + dictionary.get('BE')
                
                if (my_randoms[2] in range(0,30)):
                    minutes =  minutes  + dictionary.get('CE')
                elif (my_randoms[2] in range(31,100)):
                    minutes = minutes + dictionary.get('CF')

                if (my_randoms[3] in range(0,10)):
                    minutes =  minutes  + dictionary.get('DG')
                elif (my_randoms[3] in range(11,100)):
                    minutes = minutes + dictionary.get('DH')

                if (my_randoms[4] in range(0,40)):
                    minutes =  minutes  + dictionary.get('EH')
                elif (my_randoms[4] in range(41,100)):
                    minutes = minutes + dictionary.get('EI')
                
                if (my_randoms[5] in range(0,20)):
                    minutes =  minutes  + dictionary.get('FI')
                elif (my_randoms[5] in range(21,100)):
                    minutes = minutes + dictionary.get('FJ')

                if (my_randoms[6] in range(1,101)):
                    minutes =  minutes  + dictionary.get('GK')

                if (my_randoms[7] in range(0,30)):
                    minutes =  minutes  + dictionary.get('HK')
                elif (my_randoms[7] in range(31,100)):
                    minutes = minutes + dictionary.get('HL')

                if (my_randoms[8] in range(0,50)):
                    minutes =  minutes  + dictionary.get('IL')
                elif (my_randoms[8] in range(51,100)):
                    minutes = minutes + dictionary.get('IM')

                if (my_randoms[9] in range(0,100)):
                    minutes =  minutes  + dictionary.get('JM')

                if (my_randoms[10] in range(0,100)):
                    minutes =  minutes  + dictionary.get('KN')

                if (my_randoms[11] in range(0,40)):
                    minutes =  minutes  + dictionary.get('LN')
                elif (my_randoms[11] in range(41,100)):
                    minutes = minutes + dictionary.get('LO')

                if (my_randoms[12] in range(0,100)):
                    minutes =  minutes  + dictionary.get('MO')

                if (my_randoms[13] in range(0,100)):
                    minutes =  minutes  + dictionary.get('NP')

                if  (my_randoms[14] in range(0,100)):
                    minutes =  minutes  + dictionary.get('NP')
                

        print(my_randoms)
        print("Total Minutes is" , minutes)
        print("The average travel time for", cars, "cars is" , y / cars * x)
        print("The standard deviation is:" , statistics.stdev(my_randoms))

        
    
            






main()
    
