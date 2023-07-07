import csv

def validar_jornada(jornada):
    with open('Exercícios estudo/Exercicios extra 2/Jornadas.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == jornada:
                return True
        return False

def validar_aposta(aposta):
    return aposta in ['1', 'X', '2']

def preencher_boletim(jornada):
    boletim = []
    for jogo in jornada:
        print(jogo[1], "vs", jogo[2])
        aposta = input("Aposta (1, X, 2): ")
        while not validar_aposta(aposta):
            print("Aposta inválida!")
            aposta = input("Aposta (1, X, 2): ")
        boletim.append((jogo[0], aposta))
    return boletim

def gerar_ficheiro_boletim(jornada, boletim):
    nome_ficheiro = "jornada" + jornada + ".csv"
    with open(nome_ficheiro, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(boletim)

def ler_jornada(jornada):
    with open('Exercícios estudo/Exercicios extra 2/Jogos.csv', 'r') as f:
        reader = csv.reader(f)
        jogos = [row for row in reader if row[0] == jornada]
    return jogos

def mostrar_resultados(jornada, boletim, resultados):
    print("\nJornada", jornada)
    acertos = 0
    for jogo, resultado, aposta in zip(jornada, resultados, boletim):
        acertou = resultado == aposta[1]
        acertos += int(acertou)
        print(jogo[0], jogo[1], resultado[3], "-", resultado[4], ":", aposta[1],
              "(" + ("CERTO" if acertou else "ERRADO") + ")")
    premio = "SEM PRÉMIO."
    if acertos == 9:
        premio = "1º PRÉMIO (5000€)."
    elif acertos == 8:
        premio = "2º PRÉMIO (1000€)."
    elif acertos == 7:
        premio = "3º PRÉMIO (100€)."
    print("\nTEM", acertos, "CERTAS.", premio)

def calcular_saldo(acertos):
    custo_boletim = 0.40
    saldo = -custo_boletim * (2 ** (acertos - 9))
    return saldo

def main():
    saldo = 0.0
    while True:
        jornada = input("Jornada? ")
        if jornada == '0':
            break
        if not validar_jornada(jornada):
            print("Jornada inválida!")
            continue
        jogos = ler_jornada(jornada)
        boletim = preencher_boletim(jogos)
        gerar_ficheiro_boletim(jornada, boletim)
        resultados = jogos
        mostrar_resultados(jogos, boletim, resultados)
        acertos = sum([1 for resultado, aposta in zip(resultados, boletim) if resultado[3] == aposta[1]])
        saldo += calcular_saldo(acertos)
        print("\nSaldo:", saldo, "euro")

if __name__ == "__main__":
    main()
