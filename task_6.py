day_1 = int(input())
day_2 = int(input())
day_3 = int(input())
repeat = (day_1 == day_2) + (day_1 == day_3) + (day_2 == day_3)
if repeat == 1:
    repeat = 2
print(repeat)
