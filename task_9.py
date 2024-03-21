tower_1, tower_2, tower_3 = map(int, input().split())
towers = [tower_1, tower_2, tower_3]
tower_max = towers[0]

for i in range(0, 3):
    if towers[i] > tower_max:
        tower_max = towers[i]
towers.remove(tower_max)

tower_min = towers[0]
for i in range(0, 2):
    if towers[i] < tower_min:
        tower_min = towers[i]
towers.remove(tower_min)

print(tower_max, towers[0], tower_min)
