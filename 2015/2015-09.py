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

# import sys
# from itertools import permutations

# places = set()
# distances = dict()
# for line in open('2015-09.txt'):
#     (source, _, dest, _, distance) = line.split()
#     places.add(source)
#     places.add(dest)
#     distances.setdefault(source, dict())[dest] = int(distance)
#     distances.setdefault(dest, dict())[source] = int(distance)

# shortest = sys.maxsize
# longest = 0
# for items in permutations(places):
#     dist = sum(map(lambda x, y: distances[x][y], items[:-1], items[1:]))
#     shortest = min(shortest, dist)
#     longest = max(longest, dist)

# print("shortest: %d" % (shortest))
# print("longest: %d" % (longest))