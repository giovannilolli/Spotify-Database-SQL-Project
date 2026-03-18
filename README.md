# Spotify-Database-SQL-Project


This project includes a Python script called 4.query_app.py, which lets you run a few simple queries on a database of the most streamed songs on Spotify. It works together with three other files: schema.sql, which creates the database tables; data_loader.py,
which loads all the data from the CSV file into the database; and queries.sql, where the queries were first written and tested.

At the start of the script, a connection is made to a MySQL database called spotify_most_streamed_songs. This is the same database that was created in schema.sql, and where all the Spotify data was inserted using data_loader.py.

Inside the script, there’s a menu with 4 numbered options. Each option matches one query, with a short description to help the user know what it does. When the user picks a number, the program runs that query on the database and prints out the results.
If something goes wrong (for example, no results or a database issue), a message is shown.

This makes the script useful to check information from the dataset without needing to know SQL. The menu keeps repeating until the user decides to exit by entering 0.

At the end, the connection to the database is closed.

The Queries Included

All the queries were first written and tested in the file queries.sql, and then added to the Python app. Here’s what each one does:
	1.	Tracks with Highest Instrumentalness from 2000
This one looks for the most instrumental songs — meaning the ones with very little singing or speech — released from the year 2000 onwards. It shows the top 5.
	2.	Most Popular Artists
This query finds the 5 artists with the most total streams across all their songs. It gives a good idea of which artists were the most successful overall.
	3.	Most Danceable Tracks After 2020
This one shows the top 5 most danceable songs released after 2020. It can help spot the catchiest or most upbeat recent tracks.
	4.	Tracks by Release Year
This counts how many tracks were released in each year. The result gives a quick sense of which years had the most releases in the dataset.
