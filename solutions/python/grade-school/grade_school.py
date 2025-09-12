class School:
    def __init__(self):
        self.grades = {}
        self.additions = []

    def add_student(self, name, grade):
        if name in self.roster():
            self.additions.append(False)
            return
        if grade not in self.grades:
            self.grades[grade] = []
        self.grades[grade] = sorted(self.grades[grade] + [name])
        self.additions.append(True)

    def roster(self):
        return [s for g in sorted(self.grades.keys()) for s in self.grades[g]]

    def grade(self, grade_number):
        return self.grades.get(grade_number,[])

    def added(self):
        return self.additions

