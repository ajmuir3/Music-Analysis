
import os

import DatabaseConneciton as data_conn
from SongAnalyzer import SongAnalyzer as song_anal

    
def main():
    
    csv_file = os.path.join("data","music.csv")

    database = "music_database_1.db"
    dc = data_conn

    dc.clear_data(database)
    dc.insert_data(database, dc.readCSV(csv_file))

    # Initiating the class needs work
    list = dc.return_data(database)
    sa = song_anal

    sa(list)

    print(sa.findAvgYear(sa))
    
    
    #sa = SongAnalyzer(list)

    #print(sa)

    #data_conn.display_data(database)

    # anal = SongAnalyzer(songs)
    # plotter = SongPlotter(songs)

    # print(f"There are a total of {len(songs)} songs you listen to:\n")
    # print(f"The range of your music spans {anal.findRangeYear()} years")
    # print(f"The average year of your music is {anal.findAvgYear()}")
    # print(f"The median year of your music is {anal.findMedYear()}")

    # # print(anal) this works

    # plotter.plotSongsByYearLine("testing1")
    # plotter.plotSongsByDecadeBar("testing2")

    #plotSongsbyYear(songsByYear(songs))

    # print(songsByYear(songs))
    # print(songsByDecade(songs))

    #plotSongsbyDecade(songsByDecade(songs))



main()