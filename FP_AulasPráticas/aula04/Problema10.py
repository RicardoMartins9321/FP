n = int(input('Enter the number: '))


def isPrime(n):
    if n == 0 or n == 1:
        return False
    elif n == 2 or n == 3 or n == 5 or n == 7 or n == 9:
        return True
    for x in [2, 3, 5, 7, 9]:
        if n % x == 0:
            return False
        else:
            return True


value = isPrime(n)

print(f'{n} is prime: {value}')
