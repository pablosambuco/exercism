from datetime import datetime, timedelta

MORNING=7
NOON=13
AFTERNOON=17
EVENING=20


def hours(h):
    return timedelta(hours=h)

def days(d):
    return timedelta(days=d)

def at(dt, h):
    return dt.replace(hour=h, minute=0, second=0)

def begining(dt, m):
    return dt.replace(month=m, day=1, hour=0, minute=0, second=0)

def nextyear(dt):
    year = dt.year
    return dt.replace(year=year+1)

def next_workday(dt):
    weekday = dt.weekday()
    if weekday in (0,1,2,3,4):
        return dt
    return dt + days(7-weekday)

def prev_workday(dt):
    weekday = dt.weekday()
    if weekday in (0,1,2,3,4):
        return dt
    return dt - days(weekday-4)

def last_quarter_day(year, q):
    m = q * 3 + 1
    if m == 13:
        year += 1
        m = 1
    return datetime(year,m,1,MORNING,0,0) - days(1)

def calculate(dt, description):
    month = dt.month
    weekday = dt.weekday()
    hour = dt.hour
    year = dt.year

    if description == "NOW":
        return dt + hours(2)

    if description == "ASAP":
        if hour < 13:
            return at(dt,AFTERNOON)
        return at(dt + days(1),NOON)

    if description == "EOW":
        if weekday in (0,1,2):
            return at(dt + days(4-weekday),AFTERNOON)
        return at(dt + days(6-weekday),EVENING)
   
    if "M" in description:
        m = int(description[:len(description)-1])
        if dt < begining(dt, m):
            return at(next_workday(begining(dt, m)),8)
        return at(next_workday(begining(nextyear(dt), m)),8)

    if "Q" in description:
        q = int(description[1:])
        if dt <= last_quarter_day(year,q):
            return at(prev_workday(last_quarter_day(year,q)),8)
        return at(prev_workday(last_quarter_day(year+1,q)),8)

def delivery_date(start, description):
    
    startdt = datetime.fromisoformat(start)

    enddt = calculate(startdt, description)
    return enddt.isoformat()

