# data from README.md
DATA = {
    1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
    2: ["D", "G"],
    3: ["B", "C", "M", "P"],
    4: ["F", "H", "V", "W", "Y"],
    5: ["K"],
    8: ["J", "X"],
    10: ["Q", "Z"],
}


# from ETL excercise
def transform(legacy_data):
    new_data = {}
    for key, value in legacy_data.items():
        for uniq in value:
            new_data[uniq.lower()] = key
    return new_data


def score(word):
    scores = transform(DATA)
    return sum(scores[letter.lower()] for letter in word)
