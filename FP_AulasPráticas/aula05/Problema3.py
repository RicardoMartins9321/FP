# a)
list = []


def inputFloatList():
    while True:
        n = input('Number: ')
        if n == '':
            break
        else:
            value = int(n)
            list.append(value)
    return list


# b)

menor = []


def countLower(list, v):
    for i in list:
        if i < v:
            menor.append(i)
    return menor


# c)

def minmax(list):
    if len(list) == 0:
        return None
    minm = list[0]
    maxm = list[0]

    for i in list:
        if minm < i:
            minm = i
        elif maxm > i:
            maxm = i
    return maxm, minm


# d)


def media():
    lista = inputFloatList()
    avg = (minmax(lista)[0] + minmax(lista)[1])/2
    menor1 = countLower(lista, avg)

    print(f'A média do minímo e máximo é {avg}')
    print(f'Os números {menor1} são inferiores à media')


media()
