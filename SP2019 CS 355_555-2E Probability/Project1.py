##Project 1 Stats
##John Kiyak


import random
import array


def main():
  groupnumber = 100
  membernumber = 100
  populationnumber = groupnumber * membernumber
  grouparray = []
  memberarray = []

  for x in range(1,groupnumber+1):
    grouparray.append(x)
  
  for x in range(1,membernumber+1):
    memberarray.append(x)

  parent1group = random.randint(0,100)
  parent2group = random.randint(0,100)

  print("Parent1 is from group", parent1group)
  print("Parent2 is from group", parent2group)


  for i in range(round(populationnumber / 2)):
    childrensumcount = 0
    childgroup = random.randint(1,2)
    children = random.randint(0,3)
    if (children == 0):
        numberofchildren = 0
    elif(children == 1):
        numberofchildren = 1
        childrensumcount = childrensumcount + numberofchildren
    elif (children == 2):
        numberofchildren = 2
        childrensumcount = childrensumcount + numberofchildren
    else:
      numberofchildren = 3
      childrensumcount = childrensumcount + numberofchildren
    #print("These parents had" , numberofchildren, "children")
    
  print("The population increased by" , childrensumcount, "people")


  
  ##print(grouparray)
  ##print(memberarray)

main()
