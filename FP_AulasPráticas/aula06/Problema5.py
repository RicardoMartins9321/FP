import math


def floatInput(prompt, min=-math.inf, max=math.inf):
    assert min < max
    while True:
        try:
            res = float(input(prompt))
            if min <= res <= max:
                break
            else:
                print("ERROR: Value should be in [{},{}]!".format(min, max))
        except:
            print("ERROR: Not a float!")
    return res


def main():
    print("a) Try entering invalid values such as 1/2 or 3,1416.")
    v = floatInput("Value? ")
    print("v:", v)

    print("b) Try entering invalid values such as 15%, 110 or -1.")
    h = floatInput("Humidity (%)? ", 0, 100)
    print("h:", h)

    print("c) Try entering invalid values such as 23C or -274.")
    t = floatInput("Temperature (Celsius)? ", min=-273.15)
    print("t:", t)

    return


if __name__ == "__main__":
    main()
