import sys
import calendar
from datetime import datetime

dt = datetime.today()
user_input = sys.argv
error = '\nThis calendar takes a maximum of two arguments: month and year.\nPlease enter them in numerical format eg: 01 2017\n'


def user_calendar(year, month):
    print(f'\n{calendar.month(year, month)}\n')
    sys.exit()


def isValid(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


if len(user_input) == 1:
    month = dt.month
    year = dt.year
elif len(user_input) == 2:
    if isValid(user_input[1]) and int(user_input[1]) < 13:
        month = int(user_input[1])
        year = dt.year
    else:
        print(error)
        sys.exit()
elif len(user_input) == 3:
    if isValid(user_input[1]) and isValid(user_input[2]):
        month = int(user_input[1])
        year = int(user_input[2])
    else:
        print(error)
        sys.exit()
else:
    print(error)
    sys.exit()

user_calendar(year, month)
