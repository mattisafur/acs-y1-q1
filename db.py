import sqlite3

import config
from models import LeaderboardEntry, State


def initialize_database() -> None:
    with sqlite3.connect(config.DATABASE_FILE_PATH) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS progress (
                player_name TEXT PRIMARY KEY,
                current_room TEXT,
                previous_room TEXT,
                visited_rooms TEXT,
                time_played REAL,
                inventory TEXT
            );
            """
        )
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS leadeerboard (
                player_name TEXT PRIMARY_KEY,
                play_time REAL
            )
            """
        )


def load_state(player_name: str) -> State | None:
    with sqlite3.connect(config.DATABASE_FILE_PATH) as conn:
        cur = conn.execute(
            f"""
            SELECT * FROM progress
            WHERE player_name = '{player_name}'
            """
        )

        results = cur.fetchall()
        match len(results):
            case 0:
                return None
            case 1:
                return State.from_db_tuple(results[0])
            case _:
                raise Exception("got more than one entry from db")


def save_state(state: State) -> None:
    with sqlite3.connect(config.DATABASE_FILE_PATH) as conn:
        conn.execute(
            f"INSERT OR REPLACE INTO progress VALUES ({state.to_sql_value_string()})"
        )


def delete_state(state: State):
    with sqlite3.connect(config.DATABASE_FILE_PATH) as conn:
        conn.execute(f"DELETE FROM progress WHERE player_name = '{state.player_name}'")


def get_top_leaderboard(count: int) -> list[LeaderboardEntry]:
    with sqlite3.connect(config.DATABASE_FILE_PATH) as conn:
        cur = conn.execute(
            f"SELECT * FROM leaderboard ORDER BY play_time LIMIT {count}"
        )
        results = cur.fetchall()
        return [LeaderboardEntry.from_db_tuple(result) for result in results]


def save_leaderboard(leaderboard_entry: LeaderboardEntry) -> None:
    with sqlite3.connect(config.DATABASE_FILE_PATH) as conn:
        conn.execute(
            f"INSERT INTO leaderboard VALUES ({leaderboard_entry.to_sql_value_string()})"
        )
