# --- Day 7: Some Assembly Required ---
# This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

# Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

# The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

# For example:

# 123 -> x means that the signal 123 is provided to wire x.
# x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
# p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
# NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
# Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

# For example, here is a simple circuit:

# 123 -> x
# 456 -> y
# x AND y -> d
# x OR y -> e
# x LSHIFT 2 -> f
# y RSHIFT 2 -> g
# NOT x -> h
# NOT y -> i
# After it is run, these are the signals on the wires:

# d: 72
# e: 507
# f: 492
# g: 114
# h: 65412
# i: 65079
# x: 123
# y: 456
# In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?

# Your puzzle answer was 956.

# --- Part Two ---
# Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a). What new signal is ultimately provided to wire a?

# Your puzzle answer was 40149.


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
                
