def fact(n):
    assert n > 0
    if n == 1:
        return 1
    else:
        return n*fact(n-1)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def main():
    print(fact(4))    # 24
    print(fact(5))    # 120

    x = 2*27*53*61
    y = 2*2*17*23*53
    print(x, y, gcd(x, y))
    assert gcd(x, y) == 2*53


if __name__ == "__main__":
    main()
