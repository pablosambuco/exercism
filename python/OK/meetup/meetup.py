import calendar
from datetime import date


# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """

    def __init__(self, message):
        self.message = message


teens = [13, 14, 15, 16, 17, 18, 19]

number = {
    "Sunday": 0,
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
}


def meetup(year, month, week, day_of_week):
    cal = calendar.Calendar(firstweekday=6)
    weeks = cal.monthdayscalendar(year, month)
    day_number = number[day_of_week]
    days = [week[day_number] for week in weeks if week[day_number] > 0]
    day = None
    if week == "first":
        day = days[0]
    elif week == "second":
        day = days[1]
    elif week == "third":
        day = days[2]
    elif week == "fourth":
        day = days[3]
    elif week == "fifth" and len(days) == 5:
        day = days[4]
    elif week == "last":
        day = days[-1]
    elif week == "teenth":
        day = [teen for teen in teens if teen in days][0]
    if not day:
        raise MeetupDayException("That day does not exist.")
    return date(year, month, day)
