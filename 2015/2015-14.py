data = [line.strip() for line in open('2015-14.txt', 'r')]
size = len(data)

speeds = []
durations = []
rests = []
is_active = [True]*size
distances = [0]*size
scores = [0]*size

for d in data:
    words = d.split()
    speeds.append(int(words[3]))
    durations.append(int(words[6]))
    rests.append(int(words[-2]))

curr_timer = durations.copy()
race_time = 2503

for t in range(race_time):
    for i, status in enumerate(is_active):
        if curr_timer[i] <= 0:
            is_active[i] = not status
            if is_active[i]:
                curr_timer[i] = durations[i]
            else:
                curr_timer[i] = rests[i]
        if is_active[i]:
            distances[i] += speeds[i]
        curr_timer[i] -= 1
    winner_index = distances.index(max(distances))
    scores[winner_index] += 1
    # print(distances)
    # print(is_active)
    # print(durations)
    # print(' ')

print("Biggest distance is ", max(distances))
print("Highest score is ", max(scores))

    
