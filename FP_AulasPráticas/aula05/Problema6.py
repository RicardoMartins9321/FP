x = str(input('Enter your frase: '))


def countDigits(x):
    p = 0
    for i in x:
        if i.isdigit() == True:
            p += 1
    return p


print(countDigits(x))
