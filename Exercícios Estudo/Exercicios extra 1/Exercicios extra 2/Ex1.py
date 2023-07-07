import os

# Função para validar um número de telefone
def validarNumeroTelefone(numero):
    # Verificar se o número tem pelo menos 3 dígitos
    if len(numero) < 3:
        return False

    # Verificar se o número contém apenas dígitos ou o símbolo '+'
    for char in numero:
        if not (char.isdigit() or char == '+'):
            return False

    return True

# Função para registrar uma chamada
def registrarChamada(registro):
    origem = input("Telefone de origem? ")
    while not validarNumeroTelefone(origem):
        print("Número de origem inválido. Tente novamente.")
        origem = input("Telefone de origem? ")

    destino = input("Telefone de destino? ")
    while not validarNumeroTelefone(destino):
        print("Número de destino inválido. Tente novamente.")
        destino = input("Telefone de destino? ")

    duracao = int(input("Duração (s)? "))

    registro.append((origem, destino, duracao))

# Função para ler um arquivo de chamadas
def lerArquivoChamadas(registro):
    nome_arquivo = input("Nome do arquivo? ")
    if not os.path.isfile(nome_arquivo):
        print("Arquivo não encontrado.")
        return

    with open(nome_arquivo, "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split()
            if len(dados) == 3:
                origem, destino, duracao = dados
                registro.append((origem, destino, int(duracao)))

# Função para listar os clientes que fizeram chamadas
def listarClientes(registro):
    clientes = set()
    for chamada in registro:
        clientes.add(chamada[0])

    print("Clientes:", " ".join(sorted(clientes)))

# Função para calcular o valor total da fatura de um cliente
def calcularFatura(registro, cliente):
    total = 0
    for chamada in registro:
        if chamada[0] == cliente:
            total += chamada[2] * TARIFA_CHAMADA
    return total

# Função para gerar uma fatura detalhada para um cliente
def gerarFaturaDetalhada(registro, cliente):
    tarifario = {
        "fixa": 0.02,
        "internacional": 0.80,
        "mesma_rede": 0.04,
        "outros_destinos": 0.10
    }

    print("Fatura do cliente", cliente + ":")
    print("Destino\tDuração\tCusto")

    custo_total = 0

    for chamada in registro:
        if chamada[0] == cliente:
            origem = chamada[0]
            destino = chamada[1]
            duracao = chamada[2]

            custo = 0

            if destino[0] == "+":
                custo = tarifario["internacional"] * (duracao / 60)
            elif destino[0] == "2":
                custo = tarifario["fixa"] * (duracao / 60)
            elif origem[:2] == destino[:2]:
                custo = tarifario["mesma_rede"] * (duracao / 60)
            else:
                custo = tarifario["outros_destinos"] * (duracao / 60)

            custo_total += custo

            print(destino + "\t" + str(duracao) + "\t" + "{:.2f}".format(custo))

    print("Total:", "{:.2f}".format(custo_total))

# Função principal
def main():
    registro = []

    while True:
        print("\n1) Registar chamada")
        print("2) Ler ficheiro")
        print("3) Listar clientes")
        print("4) Fatura")
        print("5) Terminar")
        opcao = input("Opção? ")

        if opcao == "1":
            registrarChamada(registro)
        elif opcao == "2":
            lerArquivoChamadas(registro)
        elif opcao == "3":
            listarClientes(registro)
        elif opcao == "4":
            cliente = input("Cliente? ")
            gerarFaturaDetalhada(registro, cliente)
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

