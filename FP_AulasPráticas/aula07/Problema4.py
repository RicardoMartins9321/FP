def setTeams():
    teams = []
    print("Introduza uma equipa de cada vez, ou uma linha em branco para terminar")
    while True:
        team = input('Equipa: ')
        if team == '':
            break
        else:
            teams.append(team)
    return teams


def jogos(teams):
    jogos = []
    for equipa1 in teams:
        for equipa2 in teams:
            if equipa1 != equipa2:
                jogos.append((equipa1, equipa2))
    return jogos


teams = setTeams()
jogos = jogos(teams)
results = {}
table = {}

for team in teams:
    table[team] = [0, 0, 0, 0, 0, 0]

for jogo in jogos:
    print()
    print("Resultado do jogo", jogo, "?")
    x = int(input("{} : ".format(jogo[0])))
    y = int(input("{} : ".format(jogo[1])))
    results[jogo] = (x, y)

    table[jogo[0]][3] += x
    table[jogo[0]][4] += y
    table[jogo[1]][3] += y
    table[jogo[1]][4] += x

    if x > y:
        table[jogo[0]][0] += 1
        table[jogo[0]][5] += 3
        table[jogo[1]][2] += 1
    elif x < y:
        table[jogo[1]][0] += 1
        table[jogo[1]][5] += 3
        table[jogo[0]][2] += 1
    else:
        table[jogo[0]][1] += 1
        table[jogo[0]][5] += 1
        table[jogo[1]][1] += 1
        table[jogo[1]][5] += 1


def setChampion(dic):
    champion = list(dic)[0]
    for team in dic:
        if dic[team][5] > dic[champion][5]:
            champion = team
        elif dic[team][5] == dic[champion][5] and dic[team][3] - dic[team][4] > dic[champion][3] - dic[champion][4]:
            champion = team
    return champion


def printTable(dic):
    print("{:10} | {} | {} | {} | {} | {} | {}".format("Equipa", "Vitórias",
          "Empates", "Derrotas", "Golos Marcados", "Golos Sofridos", "Pontos"))
    for team in dic:
        print("{:10} | {:^8} | {:^7} | {:^8} | {:^14} | {:^14} | {:^6}".format(
            team, dic[team][0], dic[team][1], dic[team][2], dic[team][3], dic[team][4], dic[team][5]))


print()
printTable(table)
print()
print("A equipa vencedora é:", setChampion(table))
