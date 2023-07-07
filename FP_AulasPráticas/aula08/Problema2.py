with open("FP_AulasPráticas/aula08/names.txt", "r", encoding="utf-8") as names:
    name_dic = {}
    names.readline()
    for line in names:
        name = line.split(" ")
        name[-1] = name[-1].strip()
        if name[-1] not in name_dic:
            name_dic[name[-1]] = set()
        name_dic[name[-1]].add(name[0])

for e in name_dic:
    print(e, ":", name_dic[e])
