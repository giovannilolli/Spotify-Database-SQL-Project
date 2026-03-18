
-- Query 1: Tracks with Highest Instrumentalness from 2000
SELECT 
    Track.track_name,
    Track.release_date,
    ROUND(Characteristics.instrumentalness / 100, 3) AS instrumental_score
FROM 
    Track
JOIN 
    Characteristics ON Track.track_id = Characteristics.track_id
WHERE 
    Track.release_date >= '2000-01-01'
ORDER BY 
    instrumental_score DESC
LIMIT 5;


-- Query 2: Most Popular Artists

SELECT Artist.name, SUM(Track.stream_count) AS total_streams
FROM Artist
JOIN Track ON Artist.artist_id = Track.artist_id
GROUP BY Artist.name
ORDER BY total_streams DESC
LIMIT 5;



-- query 3: Most Danceable Tracks After 2020
SELECT 
    Track.track_name,
    Track.release_date,
    Characteristics.danceability
FROM 
    Track
JOIN 
    Characteristics ON Track.track_id = Characteristics.track_id
WHERE 
    Track.release_date >= '2021-01-01'
ORDER BY 
    Characteristics.danceability DESC
LIMIT 5;



-- Query 4: Tracks by Release Year

SELECT YEAR(release_date) AS release_year, COUNT(*) AS track_count
FROM Track
GROUP BY release_year
ORDER BY release_year DESC;