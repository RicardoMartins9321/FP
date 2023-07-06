n = int(input('Enter a positive number: '))
list = []


def div(n):
    divs = 0
    if n <= 0:
        print('Not a valid number')
    for i in range(1, n):
        if n % i == 0:
            list.append(i)
        value = sum(list)
    if value < n:
        print(f'{list} são divisores de n e é um número deficiente')
    elif value == n:
        print(f'{list} são divisores de n e é um número perfeito')
    else:
        print(f'{list} são divisores de n e é um número abundante')


div(n)
