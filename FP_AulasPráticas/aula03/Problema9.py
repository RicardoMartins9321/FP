def isLeapYear(year):
    if (year % 4 == 0 and ((year % 400 == 0 and year % 100 == 0) or (year % 100 != 0))):
        return True
    else:
        return False


def monthDays(year, month):
    MONTHDAYS_COMMON = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    MONTHDAYS_LEAP = (0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    if isLeapYear(year) == True:
        days = MONTHDAYS_LEAP[month]
    else:
        days = MONTHDAYS_COMMON[month]
    return days


def nextDay(year, month, day):
    nr_days = monthDays(year, month)
    if day == nr_days and month < 12:
        day = 1
        month += 1
    elif month == 12:
        month = 1
        day = 1
        year += 1
    else:
        day += 1
    return year, month, day


def main():
    print("Was", 2017, "a leap year?", isLeapYear(2017))
    print("Was", 2016, "a leap year?", isLeapYear(2016))
    print("Was", 2000, "a leap year?", isLeapYear(2000))
    print("Was", 1900, "a leap year?", isLeapYear(1900))

    print("January 2017 had", monthDays(2017, 1), "days")
    print("February 2017 had", monthDays(2017, 2), "days")
    print("February 2016 had", monthDays(2016, 2), "days")
    print("February 2000 had", monthDays(2000, 2), "days")
    print("February 1900 had", monthDays(1900, 2), "days")

    y, m, d = nextDay(2017, 1, 30)
    print(y, m, d)
    y, m, d = nextDay(2017, 1, 31)
    print(y, m, d)
    y, m, d = nextDay(2017, 2, 28)
    print(y, m, d)
    y, m, d = nextDay(2016, 2, 29)
    print(y, m, d)
    y, m, d = nextDay(2017, 12, 31)
    print(y, m, d)


main()
