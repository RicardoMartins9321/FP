# a)
def loadFile(fname, lst):
    with open(fname, 'r', encoding="utf-8") as notas:
        for line in notas:
            if line[0].isnumeric():
                value_list = line.split('\t')
                value_list[0] = int(value_list[0])
                lst.append(tuple(value_list))
    return lst


# b)
def notaFinal(reg):
    nota1 = float(reg[-3])
    nota2 = float(reg[-2])
    nota3 = float(reg[-1])
    media = (nota1 + nota2 + nota3)/3
    return media


# c)
def printPauta(lst):
    # print("Número{:^110}Nome".format("Nota"))
    print('{:6s}\t{:^55s}\t{:2s}\t'.format('Número', 'Nome', 'Nota'))
    for reg in lst:
        print("{:<6}{:^60}{:^4.1f}".format(
            reg[0], reg[1], notaFinal(reg)))


# d)
def main():
    lst = []
    loadFile("school1.csv", lst)
    loadFile("school2.csv", lst)
    loadFile("school3.csv", lst)

    lst.sort()

    printPauta(lst)


if __name__ == "__main__":
    main()
