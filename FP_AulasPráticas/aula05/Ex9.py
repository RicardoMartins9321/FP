s = input('Texto:')

# a)


def evenThenOdd(s):
    return s[0::2] + s[1::2]


""" print(evenThenOdd(s)) """


# b)
def noduplicates(s):
    lst = []
    for i in s:
        lst.append(i)
    for x in range(len(lst)):
        if x < len(lst)-1:
            if lst[x] == lst[x+1]:
                lst.pop(x)
    str = ''
    for element in lst:
        str += element
    return str


""" print(noduplicates(s)) """

# c)

n = int(input('Número: '))


def repeatenumber(n):
    if n >= 0:
        lst = []
        for i in range(1, n+1):
            for y in range(i):
                lst.append(i)
        return lst


""" print(repeatenumber(n)) """

# d)
lst = []
while True:
    n = input('Número da lista: ')
    if n == '':
        break
    else:
        lst.append(int(n))


def maximo(lst):
    maxim = int(lst[0])
    index = -1
    index_max = 0
    for i in lst:
        index += 1
        if i > maxim:
            maxim = i
            index_max = index
    return index_max


print(maximo(lst))
