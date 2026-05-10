#!/usr/bin/env python3

# This file file is in charge of Song Class

# Represents a song in the music library
class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    # Contructor
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Call all class methods in order to update global tracking when a song is created
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artists)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)
    
    # Class method to increment song count
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
    
    # Class method to add artist list if it is not there
    @classmethod
    def add_to_artists(cls, artist):
        cls.artists.append(artist)
    
    # Class method to update the genre_count
    @classmethod
    def add_to_genre_count(cls, genre):
        # Perform error handling to check if the genre is already there
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
    
    # Class method to update artist_count
    @classmethod
    def add_to_artist_count(cls, artist):
        # Perform error handling to see if the artist is already there
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
