from dataclasses import dataclass
from datetime import datetime as DateTime
from datetime import timedelta as TimeDelta
from enum import StrEnum, unique
from typing import Any, Self


@dataclass
class State:
    player_name: str
    current_room: str
    previous_room: str
    visited_rooms: list[str]
    time_played: TimeDelta
    inventory: list[str]
    session_start_time: DateTime

    @classmethod
    def new_game(cls, player_name: str) -> Self:
        return cls(
            player_name=player_name,
            current_room="lab_2001",
            previous_room="",
            visited_rooms=[],
            time_played=TimeDelta(),
            inventory=[],
            session_start_time=DateTime.now(),
        )

    @classmethod
    def from_db_tuple(cls, data: tuple[Any]) -> Self:
        if len(data) != 6:
            raise ValueError("data is not in correct format")

        try:
            player_name = data[0]
            current_room = data[1]
            previous_room = data[2]
            # Data is saved with comma (no space) separators in the DB
            visited_rooms_raw = data[3] or ""
            visited_rooms = [r for r in visited_rooms_raw.split(",") if r]
            time_played = TimeDelta(seconds=data[4])
            inventory_raw = data[5] or ""
            inventory = [i for i in inventory_raw.split(",") if i]
        except Exception as e:
            e.add_note("failed to parse value from database")
            raise e

        return cls(
            player_name,
            current_room,
            previous_room,
            visited_rooms,
            time_played,
            inventory,
            DateTime.now(),  # session_start_time - reset when loading
        )

    def to_sql_value_string(self) -> str:
        # Keep delimiter consistent with DB save format (comma, no spaces)
        visited_rooms_str = ",".join(self.visited_rooms) if self.visited_rooms else ""
        inventory_str = ",".join(self.inventory) if self.inventory else ""
        return f"'{self.player_name}','{self.current_room}','{self.previous_room}','{visited_rooms_str}',{self.time_played.total_seconds()},'{inventory_str}'"


@dataclass
class LeaderboardEntry:
    player_name: str
    play_time: TimeDelta

    @classmethod
    def from_db_tuple(cls, data: tuple[Any]) -> Self:
        if len(data) != 2:
            raise ValueError("data is not in correct format")

        try:
            player_name = data[0]
            play_time = TimeDelta(seconds=data[1])
        except Exception as e:
            e.add_note("failed to parse value from database")
            raise e

        return cls(player_name=player_name, play_time=play_time)


@unique
class Command(StrEnum):
    help = "?"
    go = "go"
    take = "take"
    answer = "answer"
    look = "look"
    inventory = "inventory"
    quit = "quit"
    pause = "pause"
    stats = "stats"
    leaderboard = "leaderboard"
    new = "new"  # for starting a new game in the main menu
    load = "load"  # for loading a game save in the main menu
    delete = "delete"  # for deleting a game save in the main menu
    where = "where"
    items = "items"
    map = "map"
