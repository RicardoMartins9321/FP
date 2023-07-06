x1 = int(input('First number: '))
x2 = int(input('Second number: '))
x3 = int(input('Thrid number: '))


def max2(x1, x2):
    if x1 > x2:
        value = x1
    else:
        value = x2
    return value


def max3(x1, x2, x3):
    value2 = max2(x1, x2)
    value2 = max2(value2, x3)
    return value2


print(max2(3, -1))
print(max3(-2, 3, 7))
