import ru_local as ru

parrots = int(input())
if 2 <= parrots % 10 <= 4 and not (11 <= parrots % 100 <= 14):
    parrot = ru.PARROT_1
elif parrots % 10 == 1 and not (parrots % 100 == 11):
    parrot = ru.PARROT_2
else:
    parrot = ru.PARROT_3
print(parrots, parrot)
