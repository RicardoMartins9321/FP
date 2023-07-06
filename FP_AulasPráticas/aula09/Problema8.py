import math


def findRoot(f, precision, start, end):
    dec = str(precision)
    if '.' in dec:
        dec = len(dec[dec.index('.') + 1:])
    else:
        dec = 0

    xx = []
    x = start
    while x <= end:
        xx.append(x)
        x = round(x + precision, dec)

    dif = end - start
    while dif > precision:
        xx1 = xx[:len(xx)//2 + 1]
        xx2 = xx[len(xx)//2 + 1:]
        if (f(xx1[0]) > 0 and f(xx1[-1]) < 0) or (f(xx1[0]) < 0 and f(xx1[-1]) > 0):
            xx = xx1.copy()
        elif (f(xx2[0]) > 0 and f(xx2[-1]) < 0) or (f(xx2[0]) < 0 and f(xx2[-1]) > 0):
            xx = xx2.copy()
        else:
            return xx[len(xx)//2]
        dif = xx[-1] - xx[0]

    return xx[len(xx)//2]


def f(x): return x + math.sin(10*x)


print(findRoot(f, 0.01, 0.2, 0.4))
print(findRoot(f, 0.0001, 0.2, 0.4))

print(findRoot(f, 0.01, 0.4, 0.6))
print(findRoot(f, 0.0001, 0.4, 0.6))
