import sqlite3

def get_games_by_genre(genre_name):
    with sqlite3.connect("db/TopGamesDB.db") as connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT Game.name, Game.releaseYear, Genre.name
            FROM Game
            JOIN GenreInGame ON Game.id = GenreInGame.gameId
            JOIN Genre ON Genre.id = GenreInGame.genreId
            WHERE LOWER(Genre.name) = LOWER(?)
            ORDER BY Game.name;
        """, (genre_name,))
        
        return cursor.fetchall()


games = get_games_by_genre("adventure")

for game in games:
    print(f"{game[0]}, {game[1]}, {game[2]}")
