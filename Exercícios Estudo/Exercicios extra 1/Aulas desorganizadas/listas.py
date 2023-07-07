#Function for inputing numbers into a list
list1 = []

def inputFloatList():
    while True:
        n = input("Number: ")
        if n == "":
            break
        else:
            value = float(n)
            list1.append(value)
    return list1


menor_v = []

def countLower():
    v = float(input("Define o valor de v: "))
    for i in list1:
        if i < v:
            menor_v.append(i)
    return menor_v


def minmax():
    if len(list1) == 0:
        return None
    min_n = list1[0]
    max_n = list1[0]

    for i in list1:
        if min_n < i:
            min_n = i
        elif max_n > i:
            max_n = i
    return max_n, min_n

menor_media = []

def inferior_media():
    media = (minmax(list1)[0] + minmax(list1)[1]) / 2
    return media

print("A lista completa dos números é:", inputFloatList())
print("Os números:", countLower(), "são inferiores ao valor de v")
print("Estes são o minimo e máximo, respetivamente:", minmax())
#print("Os números:", inferior_media(), "são inferiores à media", )