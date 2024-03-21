import ru_local as ru

number = int(input())
reversed_number = (number % 10) * 1000 + ((number % 100) // 10) * 100 + ((number % 1000) // 100) * 10 + number // 1000
if number == reversed_number:
    print(ru.REAL)
else:
    print(ru.CROOKED)
