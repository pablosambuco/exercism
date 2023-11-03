def leap_year(year):
    return False if year % 4 != 0 else year % 100 != 0 or year % 400 == 0
