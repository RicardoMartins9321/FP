x1 = float(input('Num1: '))
x2 = float(input('Num2: '))
x3 = float(input('Num3: '))

if x1 > x2 and x1 > x3:
    print('Maximum:', x1)
elif x2 > x1 and x2 > x3:
    print('Maximum:', x2)
else:
    print('Maximum:', x3)
