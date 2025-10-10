import sqlite3

import config
from models import State


def initialize_database() -> None:
    with sqlite3.connect(config.DATABASE_FILE_PATH) as conn:
        conn.execute(
            "CRAETE TABLE IF NOT EXISTS saves (player_name TEXT PRIMARY KEY, current_room TEXT, previous_room TEXT, visited_rooms TEXT, time_played REAL, inventory TEXT);"
        )


def load_save(name: str) -> State | None:
    with sqlite3.connect(config.DATABASE_FILE_PATH) as conn:
        cur = conn.execute(f"SELECT * FROM saves WHERE name = '{name}'")
        results = cur.fetchall()

        match len(results):
            case 0:
                return None
            case 1:
                return State(
                    results[0][0],
                    results[0][1],
                    results[0][2],
                    results[0][3],
                    results[0][4],
                    results[0][5],
                )
            case _:
                raise Exception("got more than one entry from db")


def save_state(save: State) -> None:
    raise NotImplementedError


def delete_save(name: str) -> None:
    with sqlite3.connect(config.DATABASE_FILE_PATH) as conn:
        conn.execute(f"DELETE FROM saves WHERE player_name = '{name}'")
