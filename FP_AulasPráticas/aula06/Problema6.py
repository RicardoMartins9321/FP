def CompareFiles(file1, file2):
    file1 = open(file1, "rb")
    file2 = open(file2, "rb")

    texto1 = file1.read(1024)
    texto2 = file2.read(1024)

    while texto1 or texto2:
        if texto1 != texto2:
            file1.close()
            file2.close()
            return "Os ficheiros são diferentes"
        else:
            texto1 = file1.read(1024)
            texto2 = file2.read(1024)

    file1.close()
    file2.close()
    return "Os ficheiros são iguais"


print(CompareFiles("nums.txt", "nums.txt"))
print(CompareFiles("nums.txt", "pg3333.txt"))
