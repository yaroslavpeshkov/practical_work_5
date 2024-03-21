import turtle
import ru_local as ru

xc = float(input('xc = '))
yc = float(input('yc = '))
r = float(input('r = '))
x = float(input('x = '))
y = float(input('y = '))

turtle.up()
turtle.setposition(xc, yc - r)
turtle.down()
turtle.circle(r)
turtle.up()
turtle.setposition(x, y)
turtle.down()
turtle.dot(8, 'red')

turtle.up()
turtle.setposition(xc, yc - r - 20)
turtle.down()
if ((abs(x-xc))**2 + (abs(y-yc))**2)**0.5 < r:
    turtle.color('red')
    turtle.write(ru.INSIDE, False, 'left', ('Arial', 15, 'normal'))
elif ((abs(x-xc))**2 + (abs(y-yc))**2)**0.5 > r:
    turtle.color('red')
    turtle.write(ru.OUTSIDE, False, 'left', ('Arial', 15, 'normal'))
else:
    turtle.color('red')
    turtle.write(ru.ONSIDE, False, 'left', ('Arial', 15, 'normal'))

turtle.done()
