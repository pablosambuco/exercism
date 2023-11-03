"""Markdown Parser"""
import re

NOT_EXPR = "^(?!<h|<ul|<p|<li).*$"
BOLD_EXPR = "(.*)__(.*)__(.*)"
ITAL_EXPR = "(.*)_(.*)_(.*)"
BULLET_EXPR = r"\* (.*)"

BOLD = "strong"
ITAL = "em"

NEWLINE = "\n"


def format_headers(line):
    for l in range(6, 0, -1):
        if re.match(f"{'#'*l} (.*)", line) is not None:
            line = f"<h{l}>" + line[l + 1 :] + f"</h{l}>"
            break
    return line


def text_format(m, f):
    return m.group(1) + f"<{f}>" + m.group(2) + f"</{f}>" + m.group(3)


def bold(m):
    return text_format(m, BOLD)


def italic(m):
    return text_format(m, ITAL)


def new_line(x):
    return "<p>" + x + "</p>"


def list_start(x):
    return "<ul>" + x


def list_end(x=""):
    return "</ul>" + x


def list_item(x):
    return "<li>" + x + "</li>"


def parse(markdown):
    lines = markdown.split(NEWLINE)
    res = []
    in_list = False
    in_list_append = False
    for i in lines:
        i = format_headers(i)

        m = re.match(BULLET_EXPR, i)
        if m:
            curr = m.group(1)
            i = list_item(curr)
            if not in_list:
                in_list = True
                i = list_start(i)
        elif in_list:
            in_list_append = True
            in_list = False

        m = re.match(NOT_EXPR, i)
        if m:
            i = new_line(i)

        m = re.match(BOLD_EXPR, i)
        if m:
            i = bold(m)

        m = re.match(ITAL_EXPR, i)
        if m:
            i = italic(m)

        if in_list_append:
            i = list_end(i)
            in_list_append = False

        res.append(i)

    if in_list:
        res.append(list_end())

    return "".join(res)
