start = 20151125

def calcTotalOperations(rows, collumns):
    totalOperations = 0
    for i in range(rows+collumns-1):
        totalOperations+=i
    totalOperations+=collumns-1
    return totalOperations

def alg(number):
    return (number*252533)%33554393

totalOperations = calcTotalOperations(2947, 3029)

currentCode = start

for i in range(totalOperations):
    currentCode = alg(currentCode)

print(currentCode)