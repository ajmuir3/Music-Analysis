import math

class SongAnalyzer:

    def __init__(self, sl):
        self.song_list = sl

    def findAvgYear(song_list):
        total = 0
        for song in song_list:
            total += song.year
        return round(total / len(song_list))

    def findMedYear(song_list):
        return song_list[len(song_list) // 2].year

    def findRangeYear(song_list):
        return song_list[-1].year - song_list[0].year

    def songsByYear(song_list):
        year_to_numSongs = {}
        for song in song_list:
            if (song.year not in year_to_numSongs):
                year_to_numSongs[song.year] = 1
            else:
                year_to_numSongs[song.year] += 1
        return year_to_numSongs

    def songsByDecade(song_list):

        decade_to_numSongs = {}
        for song in song_list:
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
