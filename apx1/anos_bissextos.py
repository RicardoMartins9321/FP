# Function that calculates whether or not a given year is a common year(365 days) or if it is a leap year(366 days)
def isLeapYear(year):
    if (year % 4 == 0 and ((year % 400 == 0 and year % 100 == 0) or (year % 100 != 0))):
        return True
    else:
        return False


# Function that chooses the correct set of days depending if it is a common year or not
def monthDays(year, month):
    MONTHDAYS_COMMON = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    MONTHDAYS_LEAP = (0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    if isLeapYear(year) == True:
        days = MONTHDAYS_LEAP[month]
    else:
        days = MONTHDAYS_COMMON[month]
    return days


# Function that given a date(year/month/day) will return the date of the following day
def nextDay(year, month, day):
    n_days = monthDays(year, month)
    if day == 31 and month == 12:
        month = 1
        day = 1
        year += 1
    elif day == n_days and month < 12:
        day = 1
        month += 1
    else:
        day += 1
    return year, month, day


# Function that given a date(year/month/day) will return the date of the previous day
def previousDay(year, month, day):
    if day == 1 and month == 1:
        year -= 1
        month = 12
        day = 31
    elif day == 1 and month > 1:
        month -= 1
        n_days = monthDays(year, month)
        day = n_days
    else:
        day -= 1
    return year, month, day


# Function that returns True if the input values are valid, else return False
def dateIsValid(year, month, day):
    n_days = monthDays(year, month)
    if month <= 12 and day <= n_days:
        return True
    else:
        return False
