from dataclasses import dataclass
from datetime import timedelta as TimeDelta
from enum import StrEnum, unique
from typing import Any, Self
from datetime import datetime as DateTime

@dataclass
class State:
    player_name: str
    current_room: str
    previous_room: str
    visited_rooms: list[str]
    time_played: TimeDelta
    inventory: list[str]
    session_start_time: DateTime = None

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
            visited_rooms = data[3].split(", ")
            time_played = TimeDelta(seconds=data[4])
            inventory = data[5].split(", ")
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
        return f"'{self.player_name}','{self.current_room}','{self.previous_room}','{','.join(self.visited_rooms)}','{self.time_played.total_seconds()}','{','.join(self.inventory)}"


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
