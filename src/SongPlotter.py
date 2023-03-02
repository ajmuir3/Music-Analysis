import os
import matplotlib.pyplot as plt
from src.SongAnalyzer import SongAnalyzer

class SongPlotter:
    def __init__(self, sl):
        self.song_list = sl

    def plotSongsByYearScatter(self,output_name):
        song_dict = SongAnalyzer(self.song_list).songsByYear()
        fig = plt.figure()
        plt.scatter(song_dict.keys(), song_dict.values(), "bo")
        plt.xlabel("Year Released")
        plt.ylabel("Number of Songs")
        plt.title("Number of Songs by Year Released")
        plt.grid()
        fig.savefig(os.path.join("data", output_name))

    def plotSongsByYearLine(self,output_name):
        song_dict = SongAnalyzer(self.song_list).songsByYear()
        fig = plt.figure()
        plt.plot(song_dict.keys(), song_dict.values(), "go:")
        plt.xlabel("Year Released")
        plt.ylabel("Number of Songs")
        plt.title("Number of Songs by Year Released")
        plt.grid()
        fig.savefig(os.path.join("data", output_name))

    def plotSongsByDecadeBar(self, output_name):
        song_dict = SongAnalyzer(self.song_list).songsByDecade()
        fig = plt.figure()
        plt.bar(song_dict.keys(), song_dict.values())
        plt.xlabel("Decade Released")
        plt.ylabel("Number of Songs")
        plt.title("Number of Songs by Decade Released")
        fig.savefig(os.path.join("data", output_name))