# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.guesses = []
        self.word = word

    def guess(self, char):
        if self.get_status() in (STATUS_WIN, STATUS_LOSE):
            raise ValueError("The game has already ended.")
        if char not in self.word or char in self.guesses:
            self.remaining_guesses -= 1
        self.guesses.append(char)

    def get_masked_word(self):
        return "".join(
            letter if letter in self.guesses else "_" for letter in self.word
        )

    def get_status(self):
        if self.get_masked_word() == self.word:
            return STATUS_WIN
        if self.remaining_guesses < 0 and self.get_masked_word() != self.word:
            return STATUS_LOSE
        return STATUS_ONGOING
