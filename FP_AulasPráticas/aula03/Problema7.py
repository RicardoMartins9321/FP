def tax(x):
    if x <= 1000:
        y = 0.1 * x
    elif 1000 < x <= 2000:
        y = 0.2 * x-100
    elif 2000 < x:
        y = 0.3 * x - 300
    return y


print(tax(1000))
print(tax(2000))
print(tax(999.99))
print(tax(3504))
