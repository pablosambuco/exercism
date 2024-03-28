from datetime import datetime, timedelta

GIGASECOND = 1_000_000_000


def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def get_months_days(month, year):
    if (month - 1) % 12 + 1 in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if (month - 1) % 12 + 1 in (4, 6, 9, 11):
        return 30
    if is_leap(year):
        return 29
    return 28

#boring add :(
def add(moment: datetime):
    return moment + timedelta(seconds=GIGASECOND)

#nice add :)
def cool_add(moment: datetime):
    second = GIGASECOND + moment.second

    minute, second = divmod(second, 60)
    minute += moment.minute

    hour, minute = divmod(minute, 60)
    hour += moment.hour

    day, hour = divmod(hour, 24)
    day += moment.day

    month = moment.month

    aux_year = moment.year
    while day > get_months_days(month, aux_year):
        day -= get_months_days(month, aux_year)
        month += 1
        aux_year = moment.year + month // 12

    year, month = divmod(month, 12)
    year += moment.year

    if not month:
        month = 12

    return datetime(year, month, day, hour, minute, second)
