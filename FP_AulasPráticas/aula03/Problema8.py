a1 = float(input('Enter a1: '))
b1 = float(input('Enter b1: '))
a2 = float(input('Enter a2: '))
b2 = float(input('Enter b2: '))


def intersects(a1, b1, a2, b2):
    if a1 >= b1 or a2 >= b2:
        x = print('Error')
    elif (a1 < a2 < b1) or (a1 < b2 < b1):
        x = print('True')
    else:
        x = print('False')
    return x


x = intersects(a1, b1, a2, b2)
