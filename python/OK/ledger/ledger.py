# -*- coding: utf-8 -*-
from datetime import datetime


class LedgerEntry:
    def __init__(self, date, desc, chng):
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.desc = desc
        self.chng = chng

    def __lt__(self, obj):
        return (self.date, self.chng, self.desc) < (obj.date, obj.chng, obj.desc)


def create_entry(date, desc, chng):
    return LedgerEntry(date, desc, chng)


def format_date(lformat, date):
    return date.strftime(lformat["date format"])


def format_string(string, length, justify):
    if len(string) > length:
        string = string[: length - 3] + "..."
    return f"{string:{justify}{length}}"


def format_change(lformat, value, symbol):
    cformat = lformat["positive" if value >= 0 else "negative"]
    cvalue = abs(value)
    cmain = f"{cvalue // 100}"
    ccents = f"{cvalue % 100:02}"
    cstring = ""
    cthousands = lformat["thousands"]
    cdecimal = lformat["decimal"]

    # reverses string, cuts 3 chars at a time, reverse items, then reverse list
    cstring = cthousands.join(
        [cmain[::-1][i : i + 3][::-1] for i in range(0, len(cmain), 3)][::-1]
    )
    cstring += cdecimal + ccents

    return format_string(cformat.format(symbol, cstring), 13, ">")


def get_format(locale):
    formats = {
        "en_US": {
            "header": [
                format_string("Date", 10, "<"),
                format_string("Description", 25, "<"),
                format_string("Change", 13, "<"),
            ],
            "date format": "%m/%d/%Y",
            "negative": "({}{})",
            "positive": " {}{} ",
            "thousands": ",",
            "decimal": ".",
        },
        "nl_NL": {
            "header": [
                format_string("Datum", 10, "<"),
                format_string("Omschrijving", 25, "<"),
                format_string("Verandering", 13, "<"),
            ],
            "date format": "%d-%m-%Y",
            "negative": "{} -{} ",
            "positive": "{} {} ",
            "thousands": ".",
            "decimal": ",",
        },
    }
    return formats[locale]


def format_entries(currency, locale, entries):
    lformat = get_format(locale)
    symbols = {"USD": "$", "EUR": "€"}

    entries.sort()
    rtable = [lformat["header"]]
    for entry in entries:
        date_str = format_date(lformat, entry.date)
        description_str = format_string(entry.desc, 25, "<")
        change_str = format_change(lformat, entry.chng, symbols[currency])
        rtable.append([date_str, description_str, change_str])
    return "\n".join([" | ".join(row) for row in rtable])
