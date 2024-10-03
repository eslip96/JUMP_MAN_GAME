# DYNAMIC CALENDER


def is_leap_year(year):
    if year < 1752:
        raise ValueError("Please provide a year after 1752.")
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def print_month_calendar(month, year, start_day_of_week, days_in_month):

    print(f"{' ' * 6}{month} {year}\n")

    days_of_the_week = (' ' * 2) + "S" + (' ' * 2) + "M" + (' ' * 2) + "T" + (' ' * 2) + "W" + (' ' * 2) + "T" + (' ' * 2) + "F" + (' ' * 2) + "S\n"
    print(days_of_the_week)

    print(" " * (start_day_of_week * 5), end='')

    for x in range(1, days_in_month + 1):
        print(f"{x:3}", end='')

        if (x + start_day_of_week) % 7 == 0:
            print("\n")

    print("\n")


months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}


def get_starting_day_of_week(month, year):
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if month < 3:
        year -= 1
    return (year + int(year / 4) - int(year / 100) + int(year / 400) +
            t[month - 1] + 1) % 7


def get_days_in_month(month, year):
    global months
    days_in_month = {
        "January": 31,
        "February": 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }

    if is_leap_year(year):
        days_in_month["February"] = 29

    return days_in_month[months[month]]


while True:
    month = int(input("What month would you like to pick (1-12)? "))
    year = int(input("What Year? "))

    days_in_month = get_days_in_month(month, year)
    start_day_of_week = get_starting_day_of_week(month, year)

    print_month_calendar(month, year, start_day_of_week, days_in_month)
