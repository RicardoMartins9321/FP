import turtle

t = turtle.Turtle()
try:
    with open('FP_AulasPráticas/aula06/drawing.txt', 'r') as numbers:
        for line in numbers:
            if line == 'UP\n':
                t.up()
            elif line == 'DOWN\n':
                t.down()
            else:
                t.goto(int(line.split()[0]), int(line.split()[1]))
except FileNotFoundError:
    print('File not found')

turtle.Screen().exitonclick()

