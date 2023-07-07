def calcular_divisores(N):
    divisores = []
    for i in range(1, N):
        if N % i == 0:
            divisores.append(i)
    return divisores

def classificar_numero(N):
    divisores = calcular_divisores(N)
    soma_divisores = sum(divisores)
    if soma_divisores < N:
        return "Número deficiente"
    elif soma_divisores == N:
        return "Número perfeito"
    else:
        return "Número abundante"

# Ler o número do teclado
N = int(input("Digite um número inteiro positivo: "))

# Calcular e imprimir os divisores próprios
divisores = calcular_divisores(N)
print("Divisores próprios:", divisores)

# Classificar o número
classificacao = classificar_numero(N)
print(classificacao)

