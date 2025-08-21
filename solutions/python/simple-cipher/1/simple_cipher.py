class Cipher:
    def __init__(self, key=None):
        self.key = key or "aaaaaaaaaaaaaaaa"
        self.transformer = [ord(letter) - ord("a") for letter in self.key]
        self.len = len(self.key)
        self.a = ord("a")
        self.z = ord("z")

    def encode(self, text):
        return "".join(
            [
                chr(
                    (ord(text[i]) + self.transformer[i % self.len] - self.a) % 26
                    + self.a
                )
                for i in range(len(text))
            ]
        )

    def decode(self, text):
        return "".join(
            [
                chr(
                    (ord(text[i]) - self.transformer[i % self.len] - self.a) % 26
                    + self.a
                )
                for i in range(len(text))
            ]
        )
