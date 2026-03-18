import pymysql


connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="spotify_most_streamed_songs"
)


queries = {
    1: {
        "description": "Top Instrumental Tracks from 2000",
        "query": """
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
            
        """
    },
    2: {
        "description": "Most Popular Artists",
        "query": """
            SELECT Artist.name, SUM(Track.stream_count) AS total_streams
            FROM Artist
            JOIN Track ON Artist.artist_id = Track.artist_id
            GROUP BY Artist.name
            ORDER BY total_streams DESC
            LIMIT 5;
        """
    },
    3: {
        "description": "Most Danceable Tracks After 2020",
        "query": """
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
        """
    },
    4: {
        "description": "Tracks by Release Year",
        "query": """
            SELECT YEAR(release_date) AS release_year, COUNT(*) AS track_count
            FROM Track
            GROUP BY release_year
            ORDER BY release_year DESC;
        """
    }
}

def execute_query(choice):
    """Run a selected query and print results."""
    try:
        with connection.cursor() as cursor:
            cursor.execute(queries[choice]["query"])
            results = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]

            print("\nResults:")
            if results:
                for row in results:
                    formatted = ", ".join(f"{col}: {val}" for col, val in zip(columns, row))
                    print(formatted)
            else:
                print("No results found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """Simple menu interface."""
    while True:
        print("\nAvailable Queries:")
        for key in queries:
            print(f"{key}. {queries[key]['description']}")

        try:
            choice = int(input("\nEnter query number (0 to exit): "))
            if choice == 0:
                print("Goodbye")
                break
            elif choice in queries:
                execute_query(choice)
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a number.")

if __name__ == "__main__":
    main()

connection.close()
