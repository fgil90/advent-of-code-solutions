data = open('01.txt', 'r')
lines = [line.strip() for line in data]

total = 0
largests = [0,0,0]

for cal in lines:
    if cal == '':
        if total > largests[0]:
            largests.pop()
            largests.insert(0,total)
        elif total > largests[1]:
            largests.pop()
            largests.insert(1, total)
        elif total > largests[2]:
            largests.pop()
            largests.append(total)
        total = 0
        continue
    total += int(cal)

print(sum(largests))


