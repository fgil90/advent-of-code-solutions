import parse

circuit = [line.strip() for line in open('2015-07.txt', 'r')]

wireDictionary = {}

# def parseSignal(signal):
#     if ("RSHIFT" in signal) or ("LSHIFT" in signal) or ("AND" in signal) or ("OR" in signal):
#         parsedSignal = list(parse.parse('{0} {1} {2} -> {3}', signal))
        
#     if "NOT" in signal:
#         parsedSignal = list(parse.parse('{0} {1} -> {2}', signal)) 
#     for character in signal:
#         if character.isdigit():
#             parsedSignal = list(parse.parse('{0} -> {1}', signal))
#             break


while len(circuit) > 0 :
    for signal in circuit:
        if ("RSHIFT" in signal) or ("LSHIFT" in signal) or ("AND" in signal) or ("OR" in signal):
            parsedSignal = list(parse.parse('{0} {1} {2} -> {3}', signal))

            if parsedSignal[1] == "AND":
                if parsedSignal[0].isdigit():
                    if parsedSignal[2] in wireDictionary.keys():
                        # print(len(circuit))
                        wireDictionary[parsedSignal[3]] = int(parsedSignal[0]) & int(wireDictionary[parsedSignal[2]])
                        circuit.remove(signal)

            if parsedSignal[1] == "OR":
                if parsedSignal[0].isdigit():
                    if parsedSignal[2] in wireDictionary.keys():
                        wireDictionary[parsedSignal[3]] = int(parsedSignal[0]) & int(wireDictionary[parsedSignal[2]])
                        # print(len(circuit))
                        circuit.remove(signal)

            if parsedSignal[0] in wireDictionary.keys():
                if parsedSignal[1] == "RSHIFT":
                    wireDictionary[parsedSignal[3]] = int(wireDictionary[parsedSignal[0]]) >> int(parsedSignal[2])
                    # print(len(circuit))
                    circuit.remove(signal)
                if parsedSignal[1] == "LSHIFT":
                    wireDictionary[parsedSignal[3]] = int(wireDictionary[parsedSignal[0]]) << int(parsedSignal[2])
                    # print(len(circuit))
                    circuit.remove(signal)
                if parsedSignal[1] == "AND":
                    if parsedSignal[2] in wireDictionary.keys():
                        wireDictionary[parsedSignal[3]] = int(wireDictionary[parsedSignal[0]]) & int(wireDictionary[parsedSignal[2]])
                        # print(len(circuit))
                        circuit.remove(signal)
                if parsedSignal[1] == "OR":
                    if parsedSignal[2] in wireDictionary.keys():
                        wireDictionary[parsedSignal[3]] = int(wireDictionary[parsedSignal[0]]) | int(wireDictionary[parsedSignal[2]])
                        # print(len(circuit))
                        circuit.remove(signal)
        else:
            if "NOT" in signal:
                parsedSignal = list(parse.parse('{0} {1} -> {2}', signal)) 
                if parsedSignal[1] in wireDictionary.keys():
                    wireDictionary[parsedSignal[2]] = ~int(wireDictionary[parsedSignal[1]])
                    # print(len(circuit))
                    circuit.remove(signal)
                continue
        
            parsedSignal = list(parse.parse('{0} -> {1}', signal))
            if parsedSignal[0].isdigit():
                wireDictionary[parsedSignal[1]] = int(parsedSignal[0])
                # print(len(circuit))
                circuit.remove(signal)
                continue
            if parsedSignal[0] in wireDictionary.keys():
                wireDictionary[parsedSignal[1]] = int(wireDictionary[parsedSignal[0]])
                # print(len(circuit))
                circuit.remove(signal)
                continue
    
print(wireDictionary["a"])
                
