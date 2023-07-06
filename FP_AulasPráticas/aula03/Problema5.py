x1 = int(input('First number: '))
x2 = int(input('Second number: '))


def max(x1, x2):
    if x1 > x2:
        value = x1
        print(f'The max value is {x1}')
    else:
        value = x2
        print(f'The max value is {x2}')
    return value


max(1, 5)
