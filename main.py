from datetime import timedelta as TimeDelta
from models import State

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
