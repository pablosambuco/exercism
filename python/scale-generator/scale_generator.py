sharp = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
flat = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
step = {"m": 1, "M": 2, "A": 3}

scales = {
    "A": sharp,
    "a": sharp,
    "Ab": flat,
    "B": sharp,
    "b": sharp,
    "Bb": flat,
    "bb": flat,
    "c": flat,
    "C": sharp,
    "c#": sharp,
    "d": flat,
    "D": sharp,
    "d#": sharp,
    "Db": flat,
    "E": sharp,
    "e": sharp,
    "Eb": flat,
    "eb": flat,
    "F": flat,
    "f": flat,
    "F#": sharp,
    "f#": sharp,
    "g": flat,
    "G": sharp,
    "g#": sharp,
    "Gb": flat,
}


class Scale:
    def __init__(self, tonic):
        scale = scales[tonic]
        tonic_index = scale.index(tonic.capitalize())
        self.scale = scale[tonic_index:] + scale[:tonic_index]

    def chromatic(self):
        return self.scale

    def interval(self, intervals):
        position = 0
        interval_list = [self.scale[position]]
        for interval in intervals:
            position += step[interval]
            if position > 11:
                position -= 12
            interval_list.append(self.scale[position])
        return interval_list
