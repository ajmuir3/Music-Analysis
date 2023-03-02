
import os
from src.Song import Song
from src.SongAnalyzer import SongAnalyzer
from src.SongPlotter import SongPlotter

def readFile(filename):
    song_list = []
    errors = []
    with open(filename,"r") as file:
        for line in file:
            try:
                entry = line.split("	")
                song_list.append(Song(entry[0], entry[1], int(entry[16])))
            except ValueError as e:
                errors.append(e)
    return song_list

def main():
    songs = sorted(readFile("/Users/ajmuir/Documents/MusicAnalysis/Music-Analysis/data/Music.txt"))

    anal = SongAnalyzer(songs)
    plotter = SongPlotter(songs)

    print(f"There are a total of {len(songs)} songs you listen to:\n")
    print(f"The range of your music spans {anal.findRangeYear()} years")
    print(f"The average year of your music is {anal.findAvgYear()}")
    print(f"The median year of your music is {anal.findMedYear()}")

    # print(anal) this works

    plotter.plotSongsByYearLine("testing1")
    plotter.plotSongsByDecadeBar("testing2")

    #plotSongsbyYear(songsByYear(songs))

    # print(songsByYear(songs))
    # print(songsByDecade(songs))

    #plotSongsbyDecade(songsByDecade(songs))



main()