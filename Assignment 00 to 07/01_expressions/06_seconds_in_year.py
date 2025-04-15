#Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this:
#There are ____ seconds in a year!

days_in_year: int = 365
hours_in_day: int = 24
min_in_hour: int = 60
sec_in_min: int = 60

def seconds_in_year():
    print(f"There are {days_in_year*hours_in_day*min_in_hour*sec_in_min} seconds in a year!")

if __name__ == '__main__':
    seconds_in_year()