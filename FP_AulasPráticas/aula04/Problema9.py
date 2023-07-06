n = int(input('Enter number: '))


def fib(n):
    f0 = 0
    f1 = 1
    if n == 0 or n == 1:
        value = 0
    elif n == 2:
        value = 1
    else:
        for i in range(n-2):
            value = f0 + f1
            f0 = f1
            f1 = value
        return value


print(fib(n))
