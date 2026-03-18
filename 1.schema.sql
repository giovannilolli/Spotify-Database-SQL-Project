create database if not exists `spotify_most_streamed_songs`;

use `spotify_most_streamed_songs`;

-- ARTIST table
CREATE TABLE if not exists Artist (
    artist_id VARCHAR(255) PRIMARY KEY, 
    name VARCHAR(255) NOT NULL,        
    artist_count INT                   
);

-- TRACK table
CREATE TABLE if not exists Track (
    track_id VARCHAR(255) PRIMARY KEY,       
    track_name VARCHAR(255) NOT NULL, 
    release_date DATE NOT NULL,       
    stream_count BIGINT,              
    artist_id VARCHAR(255) NOT NULL,           
    FOREIGN KEY (artist_id) REFERENCES Artist(artist_id)
);

-- CHARACTERISTICS table
CREATE TABLE if not exists Characteristics (
    characteristic_id VARCHAR(255) PRIMARY KEY, 
    track_id VARCHAR(255) NOT NULL,               
    bpm INT,                             
    `key` VARCHAR(5),                      
    mode VARCHAR(10),                    
    danceability DECIMAL(5, 2),          
    valence DECIMAL(5, 2),               
    energy DECIMAL(5, 2),                
    acousticness DECIMAL(5, 2),          
    instrumentalness DECIMAL(5, 2),      
    liveness DECIMAL(5, 2),              
    speechiness DECIMAL(5, 2),           
    cover_url TEXT,                      
    FOREIGN KEY (track_id) REFERENCES Track(track_id)
);

-- PLAYLIST_CHART table
CREATE TABLE if not exists Playlist_Chart (
    playlist_chart_id VARCHAR(255) PRIMARY KEY, 
    in_spotify_playlists INT,            
    in_spotify_charts INT,               
    in_apple_playlists INT,              
    in_apple_charts INT,                 
    in_deezer_playlists INT,             
    in_deezer_charts INT,                
    in_shazam_charts INT,                
    track_id VARCHAR(255) NOT NULL,               
    FOREIGN KEY (track_id) REFERENCES Track(track_id)
);
