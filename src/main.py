import math
import os
from src.Song import Song
import matplotlib.pyplot as plt
import numpy as np

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

def findAvgYear(song_list):
    total = 0
    for song in song_list:
        total+=song.year
    return round(total/len(song_list))

def findMedYear(song_list):
    return song_list[len(song_list)//2].year

def findRangeYear(song_list):
    return song_list[-1].year - song_list [0].year

def songsByYear(song_list):
    year_to_numSongs = {}
    for song in song_list:
        if(song.year not in year_to_numSongs):
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

def plotSongsbyYear(songs_dict):
    fig = plt.figure()
    plt.plot(songs_dict.keys(), songs_dict.values(),"go:")
    plt.xlabel("Year Released")
    plt.ylabel("Number of Songs")
    plt.title("Number of Songs by Year Released")
    plt.grid()
    fig.savefig(os.path.join("data", "music_by_year_line_scatter.png"))

def plotSongsbyDecade(songs_dict):
    fig = plt.figure()
    plt.bar(songs_dict.keys(), songs_dict.values())
    plt.xlabel("Decade Released")
    plt.ylabel("Number of Songs")
    plt.title("Number of Songs by Decade Released")
    fig.savefig(os.path.join("data", "music_by_decade_bar.png"))


def main():
    filename = "data/Music.txt"
    songs = sorted(readFile(filename))

    for song in songs:
        print(song)
    print()

    print(f"There are a total of {len(songs)} songs you listen to:\n")
    print(f"The range of your music spans {findRangeYear(songs)} years")
    print(f"The average year of your music is {findAvgYear(songs)}")
    print(f"The median year of your music is {findMedYear(songs)}")

    # print(songsByYear(songs).keys())
    # print(songsByYear(songs).values())
    # plotSongsbyYear(songsByYear(songs))

    # print(songsByYear(songs))
    # print(songsByDecade(songs))

    plotSongsbyDecade(songsByDecade(songs))



main()