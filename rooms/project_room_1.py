from models import State
from util import get_user_input
def project_room_1(state: State):
    ...

    # if state["rooms_visited"]["project_room_1"]:
    #     print("You already got the Computer passcode and see no reason to go back in.")
    #     state["current_room"] = "Lobby"
    #     return
    # else:
    #     print("you enter a room for the first time")
    #     state["rooms_visited"]["project_room_1"] = True

    print(
        "Possible commands:\n"
        "Look\n"
        "Go to lobby\n"
        "Quit"
    )

    while True:
        user_input = input("> ")

        match user_input.strip().lower():
            case "look":
                print(
                    "You see a barren classroom with something written on the whiteboard.\n"
                    "You take a closer look.\n"
                    "It seems to be a password to a computer, but it is encrypted.\n"
                    "On the whiteboard, it says:"
                )

                userguess = input(
                    "Dial 1 is a prime number greater than 5. \n "
                    "Dial 2 is the smallest prime number. \n "
                    "Dial 3 equals (Dial 1 + Dial 4 − Dial 2). \n "
                    "Dial 4 is a perfect square digit, it’s even, and it’s greater than 2. \n "
                    "Dial 5 shows a number that is exactly one less than Dial 1. \n "
                    "Self-check: The sum of all five digits should be 28. \n "
                    "What is your guess"
                )

                while userguess != "72946":
                    userguess = input("Incorrect, try again")
                    # state = state_snapshot

                print(
                    "Correct, You solved the puzzle and wrote down the combination on a piece of paper, and return to the lobby."
                )

                state["current_room"] = "lobby"
                return
            case "go to lobby":
                state["current_room"] = "lobby"
                return
            case "quit":
                exit()


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
        current_room="project_room_1",
        previous_room="",
        visited_rooms=[],
        time_played=Time(),
        inventory=Inventory(),
    )

    project_room_1(test_state)
