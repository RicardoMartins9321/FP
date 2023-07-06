def numsup(lista):
    n = []
    m = 0

    for i in lista[1:]:
        if i > lista[m]:
            n.append(i)
        m += 1

    return n


print(numsup([2,6,9,4,8]))
