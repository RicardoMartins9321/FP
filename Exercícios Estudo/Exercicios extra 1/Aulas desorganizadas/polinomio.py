#Function that calculates p(x) = x**2 + 2x + 3
n = int(input("Number: "))

def polinomio(n):
    px = n**2 + 2*n + 3
    return px

def f(x):
    f = polinomio(x)**2 + 2 * polinomio(x) + 3
    return f


print(polinomio(0))
print(polinomio(1))
print(polinomio(2))
print(f(1))
