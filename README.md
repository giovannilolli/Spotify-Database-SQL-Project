# Spotify Most Streamed Songs - SQL Database Project

# Project Overview
The goal of this group project was to take a raw CSV dataset of Spotify's most streamed songs and build a functioning MySQL database. We designed the tables, wrote a Python script to load the data, and built a simple interactive menu to check information from the dataset without needing to know SQL.

# Tools Used

Database: MySQL

Programming: Python (pandas, pymysql)

# Database Structure
The database (spotify_most_streamed_songs) is divided into four connected tables to organize the data efficiently:

Artist: Stores the artist's name and total global streams.

Track: Stores basic song information (release date, track name) and links to the Artist table.

Characteristics: Stores audio features for each track, like BPM, danceability, and energy.

Playlist_Chart: Stores data on how often the song appeared on platform charts (Spotify, Apple, Deezer).

<img width="1393" height="414" alt="image" src="https://github.com/user-attachments/assets/935fae39-095f-48bf-be6e-6b47bf8fbede" />


# How the Code Works

Our project runs using four main files working together:

schema.sql: This file creates the database and sets up the four tables.

data_loader.py: This script reads the raw CSV file, handles the missing values, and automatically loads all the data into the MySQL database.

queries.sql: This is where we first wrote and tested all of our SQL queries to make sure they worked.

4.query_app.py: This is the main interactive script. It connects to the database and opens a menu with 4 numbered options. The menu keeps repeating, allowing the user to run different queries and see the results printed on the screen, until they decide to exit by entering 0.

# The Queries Included
When using the Python app, the user can choose from these four queries:

1. Tracks with Highest Instrumentalness from 2000
This looks for the most instrumental songs—meaning the ones with very little singing or speech—released from the year 2000 onwards. It shows the top 5.

2. Most Popular Artists
This query finds the 5 artists with the most total streams across all their songs. It gives a good idea of which artists were the most successful overall in the dataset.

3. Most Danceable Tracks After 2020
This shows the top 5 most danceable songs released after 2020. It helps spot the catchiest or most upbeat recent tracks.

4. Tracks by Release Year
This counts how many tracks were released in each year. The result gives a quick sense of which years had the most releases in our database.

# How to Run This Project

Run schema.sql in your MySQL environment to create the tables.

Run data_loader.py to populate the database with the CSV data. (Note: Update the database password in the script to match your local environment).

Run 4.query_app.py in your terminal to open the interactive query menu.k sense of which years had the most releases in the dataset.
