import random as rand
import numpy as np

def fibonacciFinder(max):
    i = 0
    j = 1
    k = 0
    while i < max:
        print(k)
        k = i + j
        i = j
        j = k
    return("Fibonacci yay")

def primeFinder (max):
    for i in range(2, max):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)
    return(max)

#print(fibonacciFinder(100), primeFinder(15))

def triangleArea(base, height):
    area = base * height/2
    return  area

n=5
m=5
areaList = [0]*n*m
for b in range(0,n):
    areaList[b] = triangleArea(b,6)

print(areaList)

Menu = {"burgers": 12.99, "fries": 3.99, "shakes": 1.50}
def foodSum(Dict, item1, item2):
    sum = Dict[item1] + Dict[item2]
    print("The total price of your order of " + item1 + " and " + item2 + " is $" + str(sum))
    sum*= 1.0925
    print("With taxes will be $" + str(sum))

listPlayers = [1,2,3,4,5,6,7]
length = len(listPlayers)
for i in range(length):
    length = len(listPlayers)
    randomNumber = rand.randint(0,length-1)
    listPlayers.pop(randomNumber)
    #print(listPlayers)

listNumbers = []
size = 5
for i in range(size):
    listNumbers.append(10*np.random.random())




i = 1
while i < len(listNumbers):
    j = 1
    while j > 0 and listNumbers[j-1] > listNumbers[j]:
        temp = listNumbers[j]
        listNumbers[j] = listNumbers[j+1]
        listNumbers[j+1] = temp
        j-=1
    i += 1

print(listNumbers)

        
