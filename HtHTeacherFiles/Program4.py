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