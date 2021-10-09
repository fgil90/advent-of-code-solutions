instructions = [line.strip() for line in open('2015-06.txt', 'r')]

# lights = [False]
lights = [0]
rowSize = 1000

for i in range(999999):
    # lights.append(False)
    lights.append(0)

def extractInformationFromLine(command, line):

    # this function parses the line into a tuple of the format: (command, xInit, yInit, xEnd, yEnd)
    line = line.replace(command, "")
    line = line.strip()
    tempTuple = line.partition("through")
    xyInitTempTuple = tempTuple[0].partition(',')
    xyEndTempTuple = tempTuple[2].partition(',')
    commandCoordinates = (command, int(xyInitTempTuple[0]), int(xyInitTempTuple[2]), int(xyEndTempTuple[0]), int(xyEndTempTuple[2]))
    return commandCoordinates

def changeLights(command, xInit, yInit, xEnd, yEnd):
    if command == "turn on":
        for i in range(xInit,xEnd+1):
            for j in range(yInit,yEnd+1):
                # lights[rowSize * j + i] = True
                lights[rowSize * j + i] +=1
                
                
    if command == "turn off":
        for i in range(xInit,xEnd+1):
            for j in range(yInit,yEnd+1):
                if lights[rowSize * j + i] > 0:
                    # lights[rowSize * j + i] = False
                    lights[rowSize * j + i] -=1
                
    if command == "toggle":
        for i in range(xInit,xEnd+1):
            for j in range(yInit,yEnd+1): 
                # lights[rowSize * j + i] = not lights[rowSize * j + i]
                lights[rowSize * j + i] += 2
                

for line in instructions:
    if "on" in line:
        currentRange = extractInformationFromLine("turn on", line)
        changeLights(*currentRange)

    if "off" in line:
        currentRange = extractInformationFromLine("turn off", line)
        changeLights(*currentRange)

    if "toggle" in line:
        currentRange = extractInformationFromLine("toggle", line)
        changeLights(*currentRange)

# print(lights.count(True))
print(sum(lights))