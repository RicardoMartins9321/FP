x = str(input('Enter your quote: '))


def shorten(x):
    p = ''
    for i in x:
        if i.isupper() == True:
            p += i
    return p


print(shorten(x))
