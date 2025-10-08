from models import State
from util import get_user_input

def north_corridor(state):
    ...
    # if not state["rooms_visited"]["north_corridor"]:
    #     state["rooms_visited"]["north_corridor"] = True
    #     print(
    #         "You step into the North Corridor for the first time. You see a bunch of rooms in the corridor. You check which room you can visit"
    #     )
    # else:
    #     print("You are back in the North Corridor.")

    while True:
        print(
            "Possible commands:\n"
            "Go to Lobby\n"
            "Go to Front Desk Office\n"
            "Go to Classroom 2021\n"
            "Go to Classroom 2015\n"
            "Go to Equinox Student's Society\n"
            "Go to Storage Room\n"
            "Go to Project room 3\n"
            "Go to Teachers room 3\n"
            "Go to Teachers room 2\n"
            "Go to Teachers room 1\n"
            "Go to West Corridor\n"
            "Quit"
        )

        choice = input("> ")
        match choice.strip().lower():
            case "go to lobby":
                state["current_room"] = "lobby"
                return
            case "go to front desk office":
                state["current_room"] = "front_desk_office"
                return
            case "go to classroom 2021":
                print("You go to Classroom 2021. The door is locked. You go back to North Corridor.")

            case "go to classroom 2015":
                print("You go to Classroom 2015. The door is locked. You go back to North Corridor.")

            case "go to equinox student's society":
                print("You go to Equinox Student's Society. The door is locked. You go back to North Corridor.")

            case "go to storage room":
                state["current_room"] = "storage_room"
                return
            case "go to project room 3":
                print("You go to Project Room 3. The door is locked. You go back to North Corridor.")

            case "go to teachers room 2":
                print("You go to Teachers Room 2. The door is locked. You go back to North Corridor.")

            case "go to teachers room 1":
                print("You go to Teachers Room 1. The door is locked. You go back to North Corridor.")

            case "go to west corridor":
                state["current_room"] = "west_corridor"
                return
            case "quit":
                exit()
            case _:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    # This runs only when testing the room standalone
    import sys
    from pathlib import Path
    from datetime import time as Time

    # Add parent directory to Python path so we can import from main folder
    parent_dir = Path(__file__).parent.parent
    sys.path.insert(0, str(parent_dir))

    from models import Inventory

    # Create test state
    test_state = State(
        user_name="TestPlayer",
        current_room="north_corridor",
        previous_room="",
        visited_rooms=[],
        time_played=Time(),
        inventory=Inventory(),
    )

    north_corridor(test_state)