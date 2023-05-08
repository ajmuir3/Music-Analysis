class Song:
    def __init__(self, n, a, g, p, dA, yR):
        self.name = n
        self.artist = a
        self.genre = g
        self.plays = p
        self.date_added = dA
        self.year_released = yR

    def __str__(self):
        return f"{self.name}, {self.artist} ({self.year_released})"
