from dataclasses import dataclass
from datetime import time as Time


@dataclass
class Inventory: ...


@dataclass
class State:
    user_name: str
    previous_room: str
    visited_rooms: list[str]
    time_played: Time
    current_room: str
    inventory: Inventory
