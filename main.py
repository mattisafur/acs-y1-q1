from datetime import timedelta as TimeDelta

from models import State
from rooms.east_corridor import east_corridor
from rooms.lab_2001 import lab_2001

state: State = State(
    current_room="main_menu",
    inventory=[],
    previous_room="",
    time_played=TimeDelta(),
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
        case "lab_2001":
            lab_2001(state)
        case "east_corridor":
            east_corridor(state)
