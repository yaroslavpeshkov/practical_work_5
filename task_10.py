pin = int(input())
numbers = 0
pin_1 = pin
while pin_1 > 0:
    pin_1 = pin_1 // 10
    numbers += 1
number_1 = pin // 1000
number_2 = (pin % 1000) // 100
number_3 = (pin % 100) // 10
number_4 = (pin % 10)
repeat = (number_1 == number_2) + (number_1 == number_3) + (number_1 == number_4) + (number_2 == number_3) + (number_2 == number_4) + (number_3 == number_4)

if numbers == 4 and repeat == 0 and (pin < 1900 or pin > 2050):
    print('OK')
else:
    print('ERROR')
