from models import State
from util import get_user_input

def north_corridor(state):
    if "north_corridor" not in state.visited_rooms:
        state.visited_rooms.append("north_corridor")

    print("You are in the north corridor")

    display_go_list(["Lobby", "Front Desk Office", "Classroom 2.021", "Classroom 2.015", "Equinox Student's Society", "Storage Room", "Project room 3", "Teachers room 3", "Teachers room 2", "Teachers room 1" ])

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
    from datetime import timedelta as TimeDelta

    # Add parent directory to Python path so we can import from main folder
    parent_dir = Path(__file__).parent.parent
    sys.path.insert(0, str(parent_dir))

    # Create test state
    test_state = State(
        player_name="TestPlayer",
        current_room="north_corridor",
        previous_room="",
        visited_rooms=[],
        time_played=TimeDelta(),
        inventory=[],
    )

    north_corridor(test_state)