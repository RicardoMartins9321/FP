import turtle

t = turtle.Turtle()

with open('drawing.txt', 'r') as numbers:
    for line in numbers:
        if line == 'UP\n':
            t.up()
        elif line == 'DOWN\n':
            t.down()
        else:
            t.goto(int(line.split()[0]), int(line.split()[1]))

turtle.Screen().exitonclick()
