import pymysql
import pandas as pd
import numpy as np


connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="spotify_most_streamed_songs"
)

try:
    file_path = "Spotify Most Streamed Songs.csv"
    data = pd.read_csv(file_path, sep=",")
    data = data.replace({np.nan: None})

    
    with connection.cursor() as cursor:
        for index, row in data.iterrows():
            cursor.execute("""
                INSERT INTO Artist (artist_id, name, artist_count)
                VALUES (%s, %s, %s)
                ON DUPLICATE KEY UPDATE name=name;
            """, (index, row['artist(s)_name'], row['artist_count']))
    connection.commit()

    
    with connection.cursor() as cursor:
        for index, row in data.iterrows():
            try:
                stream_value = int(row['streams'])  
            except ValueError:
                print(f"Skipping entire row {index}: invalid stream value →", row['streams'])
                continue

            release_date = None
            if pd.notnull(row['released_year']) and pd.notnull(row['released_month']) and pd.notnull(row['released_day']):
                release_date = f"{int(row['released_year'])}-{int(row['released_month'])}-{int(row['released_day'])}"
            
            cursor.execute("""
                INSERT INTO Track (track_id, track_name, release_date, stream_count, artist_id)
                VALUES (%s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE track_name=track_name;
            """, (
                index,
                row['track_name'],
                release_date,
                stream_value,
                index
            ))
    connection.commit()

    
    with connection.cursor() as cursor:
        for index, row in data.iterrows():
            try:
                int(row['streams'])  
            except ValueError:
                continue

            cursor.execute("""
                INSERT INTO Characteristics (
                    characteristic_id, track_id, bpm, `key`, mode, danceability, valence, energy,
                    acousticness, instrumentalness, liveness, speechiness, cover_url
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE bpm=bpm;
            """, (
                index,
                index,
                row['bpm'],
                row['key'],
                row['mode'],
                row['danceability_%'],
                row['valence_%'],
                row['energy_%'],
                row['acousticness_%'],
                row['instrumentalness_%'],
                row['liveness_%'],
                row['speechiness_%'],
                row['cover_url']
            ))
    connection.commit()

    
    with connection.cursor() as cursor:
        for index, row in data.iterrows():
            try:
                int(row['streams'])
            except ValueError:
                print(f"Skipping entire row {index}: invalid stream value →", row['streams'])
                continue

            cursor.execute("""
                INSERT INTO Playlist_Chart (
                    playlist_chart_id,
                    in_spotify_playlists,
                    in_spotify_charts,
                    in_apple_playlists,
                    in_apple_charts,
                    in_deezer_playlists,
                    in_deezer_charts,
                    in_shazam_charts,
                    track_id
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE in_spotify_playlists=in_spotify_playlists;
            """, (
                index,
                int(str(row['in_spotify_playlists']).replace(',', '')) if pd.notnull(row['in_spotify_playlists']) else 0,
                int(str(row['in_spotify_charts']).replace(',', '')) if pd.notnull(row['in_spotify_charts']) else 0,
                int(str(row['in_apple_playlists']).replace(',', '')) if pd.notnull(row['in_apple_playlists']) else 0,
                int(str(row['in_apple_charts']).replace(',', '')) if pd.notnull(row['in_apple_charts']) else 0,
                int(str(row['in_deezer_playlists']).replace(',', '')) if pd.notnull(row['in_deezer_playlists']) else 0,
                int(str(row['in_deezer_charts']).replace(',', '')) if pd.notnull(row['in_deezer_charts']) else 0,
                int(str(row['in_shazam_charts']).replace(',', '')) if pd.notnull(row['in_shazam_charts']) else 0,
                index
            ))
    connection.commit()

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    connection.close()
