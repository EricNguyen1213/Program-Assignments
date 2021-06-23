myDict = {"Apple":3, "Banana": 5, "Carrot": 2}
myList = [2,5,6,8]
myTuple = (0,1,2)
mySet = {"Dog", "Cat", "Rat"}

print(myDict["Apple"], myList[-1], myTuple[0])

myDict["Apple"] = 0
del myDict["Carrot"]
myDict["Cantelope"] = 3

myList[3] = 2
myList = myList[1:3]

myList.append(3)
myList.extend(newList)
myList.insert(3,"whoa")

print(myList)

myList.pop(-2)
print(myList.pop(-2))
myList.remove("whoa")
myList.remove(2)
myList.clear()

print(myList)

tupleEntry = myTuple[2]
print(tupleEntry)




