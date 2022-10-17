from itertools import groupby

puzzle_input = '1321131112'

def look_and_say(n:str):
  if len(n) == 1:
    return "1" + str(n)
  out = ""
  grouped = [list(group) for d, group in groupby(n)]
  for seq in grouped:
    out += str(len(seq)) + seq[0]

  return out

for i in range(50):
  puzzle_input = look_and_say(puzzle_input)

print(len(puzzle_input))
