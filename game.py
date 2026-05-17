import sqlite3

def get_all_games():
    with sqlite3.connect("db/TopGamesDB.db") as connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, name, releaseYear
            FROM Game
            ORDER BY releaseYear;
        """)

        return cursor.fetchall()

def get_games_genres():
    with sqlite3.connect("db/TopGamesDB.db") as connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT Game.name, Genre.name
            FROM Game
            JOIN GenreInGame ON Game.id = GenreInGame.gameId
            JOIN Genre ON Genre.id = GenreInGame.genreId
            ORDER BY Game.name, Genre.name;
        """)

        return cursor.fetchall()
    
def search_games(keyword):
    with sqlite3.connect("db/TopGamesDB.db") as connection:
        cursor = connection.cursor()

        keyword_lower = keyword.lower()

        cursor.execute("""
            SELECT id, name, releaseYear
            FROM Game
            WHERE LOWER(name) LIKE ?
            ORDER BY name;
        """, (f"%{keyword_lower}%",))

        return cursor.fetchall()   # ← ÕIGE KOHT

games = search_games("zel")

for game in games:
    print(game)
