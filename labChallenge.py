def primeLstGen(n):
    numTestList = [True] * (n + 1)          #create a list with True value
    primes = []                             #create empty list
    for i in range(2, n + 1):               #Set for loop condition 
        if numTestList[i]:                  #
            primes.append(i)
        for j in range(i, n + 1, i):
            numTestList[j] = False
    return primes

print(primeLstGen(250))

result = open("results.txt","w")

countRes = 0
for pnum in primeLstGen(250):
    result.write(str(pnum) + "\n")
    countRes += 1
#result.close()
print("Prime numbers amount - " + str(countRes))
