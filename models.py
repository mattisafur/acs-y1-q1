from dataclasses import dataclass
from datetime import timedelta as TimeDelta
from enum import StrEnum, unique
from typing import Self


@dataclass
class State:
    player_name: str
    current_room: str
    previous_room: str
    visited_rooms: list[str]
    time_played: TimeDelta
    inventory: list[str]

    @classmethod
    def new_game(cls, player_name: str) -> Self:
        return cls(
            player_name=player_name,
            current_room="main_menu",
            previous_room=None,
            visited_rooms=[],
            time_played=TimeDelta(),
            inventory=[],
        )


@unique
class Commands(StrEnum):
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
