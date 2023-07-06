# Face values of coins (in cents):
COINS = [200, 100, 50, 20, 10, 5, 2, 1]


def value(bag):
    value = 0
    for element in bag:
        value += element * bag[element]
    return value


def transfer1coin(bag1, c, bag2):
    if bag1.get(c, 0) == 0:
        return False
    else:
        bag1[c] -= 1
        bag2[c] = bag2.get(c, 0) + 1
    return True


def transfer(bag1, amount, bag2):
    if amount == 0:
        return True
    if value(bag1) < amount:
        return False
    to_transfer = {}
    for coin in COINS:
        to_transfer[coin] = amount // coin
        if bag1.get(coin, 0) < to_transfer[coin]:
            to_transfer[coin] = bag1.get(coin, 0)

        amount -= coin * to_transfer[coin]


def strbag(bag):
    string = ""
    b_list = sorted(list(bag.items()), reverse=True)
    for i in range(len(b_list)):
        if b_list[i][1] != 0:
            string += "{}x{}".format(b_list[i][1], b_list[i][0])
            if i != len(b_list) - 1:
                string += "+"
    string += "=" + str(value(bag))
    return string


def main():
    # A bag of coins is represented by a dict of {coin: number} items
    bag1 = {1: 4, 2: 0, 5: 1, 10: 0, 20: 5, 50: 4, 100: 2, 200: 1}
    bag2 = {}

    # Test the value function.
    assert value({}) == 0
    assert value({1: 7, 5: 2, 20: 4, 100: 1}) == 197

    # Test the strbag function.
    print(strbag({1: 7, 5: 2, 20: 4, 100: 1}))        # 1x100+4x20+2x5+7x1=197
    print(strbag({1: 7, 5: 2, 10: 0, 20: 4, 100: 1}))  # 1x100+4x20+2x5+7x1=197

    print("bag1:", strbag(bag1))    # bag1: 1x200+2x100+4x50+5x20+1x5+4x1=709
    print("bag2:", strbag(bag2))    # bag2: =0

    print(transfer1coin(bag1, 10, bag2))    # False!
    print("bag1:", strbag(bag1))    # bag1: 1x200+2x100+4x50+5x20+1x5+4x1=709
    print("bag2:", strbag(bag2))    # bag2: =0

    print(transfer1coin(bag1, 20, bag2))    # True
    print("bag1:", strbag(bag1))    # bag1: 1x200+2x100+4x50+4x20+1x5+4x1=689
    print("bag2:", strbag(bag2))    # bag2: 1x20=20

    print(transfer1coin(bag1, 20, bag2))    # True
    print("bag1:", strbag(bag1))    # bag1: 1x200+2x100+4x50+3x20+1x5+4x1=669
    print("bag2:", strbag(bag2))    # bag2: 2x20=40

    print(transfer(bag1, 157, bag2))        # True (should be easy)
    print("bag1:", strbag(bag1))    # bag1: 1x200+1x100+3x50+3x20+2x1=512
    print("bag2:", strbag(bag2))    # bag2: 1x100+1x50+2x20+1x5+2x1=197

    print(transfer(bag1, 60, bag2))  # not easy, but possible...
    print("bag1:", strbag(bag1))
    print("bag2:", strbag(bag2))

    return


if __name__ == "__main__":
    main()
