import math

class SongAnalyzer:

    def __init__(self, sl):
        self.song_list = sl

    def findAvgYear(self):
        total = 0
        for song in self.song_list:
            total += song.year
        return round(total / len(self.song_list))

    def findMedYear(self):
        return self.song_list[len(self.song_list) // 2].year

    def findRangeYear(self):
        return self.song_list[-1].year - self.song_list[0].year

    def songsByYear(self):
        year_to_numSongs = {}
        for song in self.song_list:
            if (song.year not in year_to_numSongs):
                year_to_numSongs[song.year] = 1
            else:
                year_to_numSongs[song.year] += 1
        return year_to_numSongs

    def songsByDecade(self):

        decade_to_numSongs = {}
        for song in self.song_list:
            decade = math.floor(song.year / 10) * 10
            if (decade not in decade_to_numSongs):
                decade_to_numSongs[decade] = 1
            else:
                decade_to_numSongs[decade] += 1
        return decade_to_numSongs

    def __str__(self):
        return_str = f"Total Songs in the List: {len(self.song_list)}"
        for song in self.song_list:
            return_str += f"{str(song)}\n"
        return return_str
