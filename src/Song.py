class Song:
    def __init__(self, n, a, y):
        self.name = n
        self.artist = a
        self.year = y

    def __lt__(self, other):
        return self.year < other.year

    def __str__(self):
        return f"{self.name}, {self.artist} ({self.year})"
