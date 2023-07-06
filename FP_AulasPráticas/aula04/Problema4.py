n = int(input('Enter n value: '))

def fatorial(n):
    if n < 0:
        return 'Não definido'
    else:
        while n > 1:
            value = n * (n-1)
            n -= 1
            return value

print(fatorial(n))