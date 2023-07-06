# p0= 3; p1=6; p2=11; p(p1)=51
x = int(input('Enter x value for p(x): '))


def p(x):
    p = x**2 + 2*x + 3
    return p


def f(x):
    f = p(x)**2 + 2 * p(x) + 3
    return f


print(p(0))
print(p(1))
print(p(2))
print(f(1))
