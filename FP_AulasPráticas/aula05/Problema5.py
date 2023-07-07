list = []
equipa = '0'

while equipa != '' or len(list) < 2:
    equipa = input('Equipa: ')
    if equipa != '' and equipa not in list:
        list.append(equipa)


def allMatches(list):
    matches = []
    for i in list:
        for x in list:
            if i != x:
                matches.append((i, x))
    return matches


print("Jogos:", allMatches(list))

