# --- Day 9: All in a Single Night ---
# Every year, Santa manages to deliver all of his presents in a single night.

# This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?

# For example, given the following distances:

# London to Dublin = 464
# London to Belfast = 518
# Dublin to Belfast = 141
# The possible routes are therefore:

# Dublin -> London -> Belfast = 982
# London -> Dublin -> Belfast = 605
# London -> Belfast -> Dublin = 659
# Dublin -> Belfast -> London = 659
# Belfast -> Dublin -> London = 605
# Belfast -> London -> Dublin = 982
# The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

# What is the distance of the shortest route?

# Your puzzle answer was 117.

# --- Part Two ---
# The next year, just to show off, Santa decides to take the route with the longest distance instead.

# He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.

# For example, given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.

# What is the distance of the longest route?

# Your puzzle answer was 909.

import parse

distancesInput = [line.strip() for line in open('2015-09.txt', 'r')]
citiesList = set()
distancesDict = {}

totalDistances = {}

for distance in distancesInput:
    parsedLine = parse.parse("{0} to {1} = {2}", distance)
    origin = parsedLine[0]
    destination = parsedLine[1]
    distance = int(parsedLine[2])

    distancesDict[(origin, destination)] = distance
    distancesDict[(destination, origin)] = distance

    citiesList.add(origin)
    citiesList.add(destination)

def loopThroughCities(cities, startingCity, distance, path):
    if len(cities) == 1:
        newPath = path + "->"
        totalDistances[path] = distance
        return distance
    
    newCitiesList = set(cities)
    newCitiesList.remove(startingCity)
    newCitiesDictionary = {}
    for city in newCitiesList:
        newPath = path + "->" + city
        newCitiesDictionary[city] = loopThroughCities(newCitiesList, city, distancesDict[(startingCity, city)]+distance, newPath)

    return newCitiesDictionary

for city in citiesList:
    loopThroughCities(citiesList, city, 0, city)

print(min(totalDistances.values()))
