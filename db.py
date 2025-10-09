import sqlite3

import config
from models import State


def initialize_database() -> None:
    with sqlite3.connect(config.DATABASE_FILE_PATH) as conn:
        conn.execute(
            "CRAETE TABLE IF NOT EXISTS saves (player_name TEXT PRIMARY KEY, current_room TEXT, previous_room TEXT, visited_rooms TEXT, time_played REAL, inventory TEXT);"
        )


def load_save(name: str) -> State | None:
    raise NotImplementedError


def delete_save(name: str) -> None:
    with sqlite3.connect(config.DATABASE_FILE_PATH) as conn:
        conn.execute(f"DELETE FROM saves WHERE player_name = '{name}'")
