file = open("dados.txt")

for line in file:
    res = line[-3:]
    print(res)
