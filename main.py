from models import State
from rooms.east_corridor import east_corridor
from rooms.lab_2001 import lab_2001

state = State.new_game("dummy_state")

def main_menu():
    # TODO implement main menu
    global state
    state = State.new_game("test")

main_menu()

while True:
    match state.current_room:
        case "main_menu":
            main_menu()
        case "lab_2001":
            lab_2001(state)
        case "east_corridor":
            east_corridor(state)
