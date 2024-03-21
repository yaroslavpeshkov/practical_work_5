import ru_local as ru

knat_input = int(input())
sickle_input = knat_input // 29
knat = knat_input % 29
galleon = sickle_input // 17
sickle = sickle_input % 17

if 2 <= galleon % 10 <= 4 and not (11 <= galleon % 100 <= 14):
    galleons = ru.GALLEON_1
elif galleon % 10 == 1 and not (galleon % 100 == 11):
    galleons = ru.GALLEON_2
else:
    galleons = ru.GALLEON_3

if 2 <= sickle % 10 <= 4 and not (11 <= sickle % 100 <= 14):
    sickles = ru.SICKLE_1
elif sickle % 10 == 1 and not (sickle % 100 == 11):
    sickles = ru.SICKLE_2
else:
    sickles = ru.SICKLE_3

if 2 <= knat % 10 <= 4 and not (11 <= knat % 100 <= 14):
    knats = ru.KNAT_1
elif knat % 10 == 1 and not (knat % 100 == 11):
    knats = ru.KNAT_2
else:
    knats = ru.KNAT_3

if galleon != 0:
    print(galleon, galleons)
if sickle != 0:
    print(sickle, sickles)
if knat != 0:
    print(knat, knats)
