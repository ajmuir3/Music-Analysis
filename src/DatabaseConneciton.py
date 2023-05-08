import sqlite3
import os

from Song import Song

# Define the function to insert data from a list of Song objects
def insert_data(songs):
    # Connect to the database
    conn = sqlite3.connect('music_database.db')

    # Create a cursor object
    c = conn.cursor()

    # Create a table for the data
    c.execute('''CREATE TABLE IF NOT EXISTS music_data
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 song_name TEXT,
                 artist TEXT,
                 genre TEXT,
                 plays INTEGER,
                 date_added TEXT,
                 year_released INTEGER)''')

    # Insert the data from the list of Song objects
    for song in songs:
        c.execute("INSERT INTO music_data (song_name, artist, genre, plays, date_added, year_released) VALUES (?, ?, ?, ?, ?, ?)", (song.name, song.artist, song.genre, song.plays, song.date_added, song.year_released))

    # Commit the changes to the database
    conn.commit()

    # Close the connection
    conn.close()

# Define the function to display the data
def display_data():
    # Connect to the database
    conn = sqlite3.connect('music_database.db')

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

def clear_data():
    # Remove the database file if it exists
    if os.path.exists('music_database.db'):
        os.remove('music_database.db')
        print("Database dropped successfully.")
    else:
        print("Database does not exist.")

# Create a list of Song objects
songs = [
    Song('Song 1', 'Artist 1', 'Genre1', 20, 'Today', 1990)
    # Add more songs here
]

# Insert the data into the database
insert_data(songs)

# Display the data from the database
display_data()

# Clear the data from the datadabe
clear_data()


