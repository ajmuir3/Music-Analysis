import sqlite3
import os
from Song import Song

def readCSV(filename):
    song_list = []
    errors = []
    with open(filename,"r") as file:
        for line in file:
            try:
                entry = line.split(",")
                song_list.append(Song(entry[0], entry[1], entry[2], int(entry[3]), int(entry[4].split("\n")[0])))
            except ValueError as e:
                errors.append("{entry} cannot be added due to {error}".format(entry = line, error = e))
        # for entry in errors:
        #     print(entry)
    return song_list

# Define the function to insert data from a list of Song objects
def insert_data(database,songs):
    # Connect to the database
    conn = sqlite3.connect(database)

    # Create a cursor object
    c = conn.cursor()

    # Create a table for the data
    c.execute('''CREATE TABLE IF NOT EXISTS music_data
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 song_name TEXT,
                 artist TEXT,
                 genre TEXT,
                 plays INTEGER,
                 year_released INTEGER)''')

    # Insert the data from the list of Song objects
    for song in songs:
        c.execute("INSERT INTO music_data (song_name, artist, genre, plays, year_released) VALUES (?, ?, ?, ?, ?)", (song.name, song.artist, song.genre, song.plays, song.year_released))

    # Commit the changes to the database
    conn.commit()

    # Close the connection
    conn.close()

# Define the function to display the data
def display_data(database):
    # Connect to the database
    conn = sqlite3.connect(database)

    # Create a cursor object
    c = conn.cursor()

    # Select all the data from the table
    c.execute("SELECT * FROM music_data")

    # Fetch and display the data
    data = c.fetchall()
    for row in data:
        print(row)

    # Close the connection
    conn.close()

def return_data(database):
    # Connect to the database
    conn = sqlite3.connect(database)

    # Create a cursor object
    c = conn.cursor()

    # Select all the data from the table
    c.execute("SELECT * FROM music_data")

    # Fetch and display the data
    data = []
    for entry in c.fetchall():
        data.append(entry)
    
    # Close the connection
    conn.close()

    # Return Data
    return data

def clear_data(database):
    # Remove the database file if it exists
    if os.path.exists(database):
        os.remove(database)
        print("Database dropped successfully.")
    else:
        print("Database does not exist.")

# def main():
#     # Create a list of Song objects
#     songs = [
#         Song('Song 1', 'Artist 1', 'Genre1', 20, 'Today', 1990)
#         # Add more songs here
#     ]

#     database = "music_database.db"

#     # Insert the data into the database
#     insert_data(database, songs)

#     # Display the data from the database
#     display_data(database)

#     # Clear the data from the datadabe
#     clear_data(database)

# main()

