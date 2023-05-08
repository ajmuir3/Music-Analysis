class Song:
    def __init__(self, n, a, g, p, yR):
        self.name = n
        self.artist = a
        self.genre = g
        self.plays = p
        self.year_released = yR

    def __lt__(self,other):
        return self.year<other.year

    def __str__(self):
        return f"{self.name}, {self.artist} ({self.year_released})"
