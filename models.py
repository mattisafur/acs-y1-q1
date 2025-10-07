from dataclasses import dataclass
from datetime import time as Time
from enum import StrEnum, unique


@dataclass
class Inventory: ...


@dataclass
class State:
    user_name: str
    current_room: str
    previous_room: str
    visited_rooms: list[str]
    time_played: Time
    inventory: Inventory


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
