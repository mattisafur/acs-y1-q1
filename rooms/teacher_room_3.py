from models import State
from util import get_user_input


def teacher_room_3(state: State):
    if "teacher_room_3" in state.visited_rooms:
        print("You have already seen this room")
    else:
        print("You enter a room for the first time")
        state.visited_rooms.append("teacher_room_3")

    print(
        "Possible commands:\n"
        "--- Look around\n"
        "--- Go to Lobby\n"
        "--- Quit\n",
    )

    while True:
        user_input = get_user_input()

        match " ".join(user_input).strip().lower():
            case "look around":
                print(
                    "You step into the teacher's lounge. Papers are scattered, coffee mugs still half full. "
                    "A bookshelf is tilted, blocking part of the exit. On the desk you see four folders labeled A, B, C, D with notes stuck to them. "
                    "A whiteboard says: 'Put knowledge in the right order. Only then the truth is revealed.'"
                )

                print(
                    "The teacher's lounge is a mess. The bookshelf looks unstable.\n"
                    "On the desk are four folders labeled A, B, C, D. Each has a note:\n"
                    "Folder A: 'Comes after B.'\n"
                    "Folder B: 'Must be first.'\n"
                    "Folder C: 'Is never next to A.'\n"
                    "Folder D: 'Always after C.'\n"
                    "A whiteboard reads: 'Put knowledge in the right order. Only then the truth is revealed.'\n"
                )

                while True:
                    userguess_input = get_user_input()
                    userguess = "".join(userguess_input).strip().upper()
                    
                    if userguess == "BCDA":
                        print("Correct, you solved this one!")
                        state.previous_room = "teacher_room_3"
                        state.current_room = "lobby"
                        return
                    else:
                        print("Incorrect, try again!")

            case "go to lobby":
                state.previous_room = "teacher_room_3"
                state.current_room = "lobby"
                return
            
            case "quit":
                print("Thanks for playing!")
                exit()
            
            case _:
                print("Invalid command. Try 'Look around', 'Go to Lobby', or 'Quit'.")


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
        current_room="teacher_room_3",
        previous_room="",
        visited_rooms=[],
        time_played=Time(),
        inventory=Inventory(),
    )
    
    teacher_room_3(test_state)
