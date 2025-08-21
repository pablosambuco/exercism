"""Tournament"""

reverse = {"win": "loss", "draw": "draw", "loss": "win"}

points = {"win": 3, "draw": 1, "loss": 0}


class Table:
    """Class Table"""

    def __init__(self) -> None:
        self.table = {}

    def add_event(self, team, event) -> None:
        if team not in self.table:
            self.table[team] = {
                "played": 0,
                "win": 0,
                "draw": 0,
                "loss": 0,
                "points": 0,
            }
        self.table[team]["played"] += 1
        self.table[team][event] += 1
        self.table[team]["points"] += points[event]

    def format(self):
        sorted_table = sorted(
            self.table.items(), key=lambda x: (-1 * x[1]["points"], x[0])
        )
        string_pattern = "{:<30} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2}"
        output = [string_pattern.format("Team", "MP", "W", "D", "L", "P")]
        output.extend(
            string_pattern.format(
                team,
                values["played"],
                values["win"],
                values["draw"],
                values["loss"],
                values["points"],
            )
            for team, values in sorted_table
        )
        return output


def tally(rows):
    table = Table()
    for row in rows:
        local, visitor, result = row.split(";")
        table.add_event(local, result)
        table.add_event(visitor, reverse[result])
    return table.format()
