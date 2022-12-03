data = open('02.txt', 'r')
lines = [line.strip() for line in data]

win = 6
draw = 3
lose = 0

rock = 1
paper = 2
scissors = 3

score = 0

lookup = {
    "A X": lose + scissors,
    "A Y": draw + rock,
    "A Z": win + paper,
    "B X": lose + rock,
    "B Y": draw + paper,
    "B Z": win + scissors,
    "C X": lose + paper,
    "C Y": draw + scissors,
    "C Z": win + rock,
}

for line in lines:
    score += lookup[line]

print(score)



