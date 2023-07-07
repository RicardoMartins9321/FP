import calendar


# Fucntion that calculates whether or not a given year is a common year(365 days) or if it is a leap year(366 days)
def isLeapYear(year):
    return(year % 4 == 0 and ((year % 400 == 0 and year % 100 == 0) or (year % 100 != 0)))


# Function that chooses the correct set of days depending if it is a common year or not 
def monthDays(year, month):
    MONTHDAYS_COMMON = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    MONTHDAYS_LEAP = (0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    if isLeapYear(year) == True:
        days = MONTHDAYS_LEAP[month]
    else:
        days = MONTHDAYS_COMMON[month]
    return days

    #if isLeapYear(year):
    #    MONTHDAYS = (0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    #else:
    #    MONTHDAYS = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    #days = MONTHDAYS[month]
    #return days

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
        day = monthDays(year, month)
    else:
        day -= 1
    return year, month, day


# Function that returns True if the input values are valid, else return False
def dateIsValid(year, month, day):
    return 0 < month <= 12 and 0 < day <= monthDays(year,month)


def main1():
    year = int(input("Choose the year: "))
    month = int(input("Choose the month: "))
    day = int(input("Choose the day: "))
    print("----------------------------------------")
    try:
        print(year, "is a leap year?", isLeapYear(year))
        print(calendar.month_name[month], "has a total of", monthDays(year, month), "days")
        print("The date after", day,month,year, "will be", nextDay(year, month, day))
        print("The date before ", end="")
        print(day,month,year,sep="/", end="") 
        print(" will be", previousDay(year, month, day))
        print("The date given is", dateIsValid(year, month, day))
    except:
        ValueError
        IndexError
        print("Oops, something went wrong!")
        print("Please give some valid input! ")
    
main1()
    
