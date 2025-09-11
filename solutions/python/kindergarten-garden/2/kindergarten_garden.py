SEEDS = {
    "G": "Grass",
    "C": "Clover",
    "R": "Radishes",
    "V": "Violets",
}

STUDENTS = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eve",
    "Fred",
    "Ginny",
    "Harriet",
    "Ileana",
    "Joseph",
    "Kincaid",
    "Larry",
]


class Garden:

    def __init__(self, diagram, students=STUDENTS):
        self.diagram = diagram.splitlines()
        garden_size = len(self.diagram[0]) // 2
        self.students = sorted(students[:garden_size])
        self.plants_dict = {}
        for i, student in enumerate(self.students):
            self.plants_dict[student] = [SEEDS[line[x]] for line in self.diagram for x in (i*2, i*2+1)]

    def plants(self, student):
        return self.plants_dict[student]
