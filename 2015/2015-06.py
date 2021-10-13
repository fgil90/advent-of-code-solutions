# --- Day 6: Probably a Fire Hazard ---
# Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

# Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

# Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

# To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

# For example:

# turn on 0,0 through 999,999 would turn on (or leave on) every light.
# toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
# turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
# After following the instructions, how many lights are lit?

# Your puzzle answer was 377891.

# --- Part Two ---
# You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

# The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

# The phrase turn on actually means that you should increase the brightness of those lights by 1.

# The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

# The phrase toggle actually means that you should increase the brightness of those lights by 2.

# What is the total brightness of all lights combined after following Santa's instructions?

# For example:

# turn on 0,0 through 0,0 would increase the total brightness by 1.
# toggle 0,0 through 999,999 would increase the total brightness by 2000000.
# Your puzzle answer was 14110788.


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