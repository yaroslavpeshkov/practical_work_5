import ru_local as ru

mass_lb = float(input())
height_in = float(input())
bmi = mass_lb/(height_in**2) * 4.53e-1 / 2.54e-2**2
if bmi < 16:
    print(ru.SEVERE_DEFICIENCY)
elif bmi <= 18.49:
    print(ru.INSUFFICIENT)
elif bmi <= 24.99:
    print(ru.STANDARD)
elif bmi <= 29.99:
    print(ru.OVERWEIGHT)
elif bmi <= 34.99:
    print(ru.OBESITY_1)
elif bmi <= 39.99:
    print(ru.OBESITY_2)
else:
    print(ru.OBESITY_3)
