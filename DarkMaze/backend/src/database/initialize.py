import sqlite3


def initialize():
    """Initialize the database and create necessary tables if they don't exist."""
    conn = sqlite3.connect("game.db")
    cursor = conn.cursor()

    # Create game_state table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS game_state (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        current_level_name TEXT NOT NULL,
        map_size TEXT NOT NULL,
        health INTEGER NOT NULL,
        path TEXT NOT NULL,
        current_position TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()