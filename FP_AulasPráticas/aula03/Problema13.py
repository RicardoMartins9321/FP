def mdc(a, b):
    while a % b > 0:
        r = a % b
        b = mdc(b, r)
    return b


a = int(input('First value: '))
b = int(input('Second value: '))
print(mdc(a, b))
