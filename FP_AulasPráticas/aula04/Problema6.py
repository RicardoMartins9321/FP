def leibnizPi4():
    n = int(input("Soma de n primeiros termos? "))-1
    soma = 0
    while n >= 0:
        termo = ((-1)**n)/(2*n+1)
        soma += termo
        n -= 1
    return soma


print(leibnizPi4())
