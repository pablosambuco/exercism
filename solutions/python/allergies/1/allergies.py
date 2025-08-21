class Allergies:
    ALLERGENS = {
        1: "eggs",
        2: "peanuts",
        4: "shellfish",
        8: "strawberries",
        16: "tomatoes",
        32: "chocolate",
        64: "pollen",
        128: "cats",
    }

    def __init__(self, score):
        self.items = [
            allergen
            for value, allergen in self.ALLERGENS.items()
            if value & score
        ]

    def allergic_to(self, item):
        return item in self.items

    @property
    def lst(self):
        return list(self.items)
