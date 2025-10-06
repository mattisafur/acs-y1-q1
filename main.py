from datetime import time as Time

from models import Inventory, State

state: State = State(
    current_room="main_menu",
    inventory=Inventory(),
    previous_room="",
    time_played=Time(),
    user_name="",
    visited_rooms=[],
)


def main_menu():
    # load state into global variable
    ...


while True:
    match state.current_room:
        case "main_menu":
            main_menu()
