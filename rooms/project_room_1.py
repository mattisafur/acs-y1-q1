# from models import State
# from util import get_user_input
# def project_room_1(state: State):
#     ...
#
#     # if state["rooms_visited"]["project_room_1"]:
#     #     print("You already got the Computer passcode and see no reason to go back in.")
#     #     state["current_room"] = "Lobby"
#     #     return
#     # else:
#     #     print("you enter a room for the first time")
#     #     state["rooms_visited"]["project_room_1"] = True
#
#     print(
#         "Possible commands:\n"
#         "Look\n"
#         "Go to lobby\n"
#         "Quit"
#     )
#
#     while True:
#         user_input = input("> ")
#
#         match user_input.strip().lower():
#             case "look":
#                 print(
#                     "You see a barren classroom with something written on the whiteboard.\n"
#                     "You take a closer look.\n"
#                     "It seems to be a password to a computer, but it is encrypted.\n"
#                     "On the whiteboard, it says:"
#                 )
#
#                 userguess = input(
#                     "Dial 1 is a prime number greater than 5. \n "
#                     "Dial 2 is the smallest prime number. \n "
#                     "Dial 3 equals (Dial 1 + Dial 4 − Dial 2). \n "
#                     "Dial 4 is a perfect square digit, it’s even, and it’s greater than 2. \n "
#                     "Dial 5 shows a number that is exactly one less than Dial 1. \n "
#                     "Self-check: The sum of all five digits should be 28. \n "
#                     "What is your guess"
#                 )
#
#                 while userguess != "72946":
#                     userguess = input("Incorrect, try again")
#                     # state = state_snapshot
#
#                 print(
#                     "Correct, You solved the puzzle and wrote down the combination on a piece of paper, and return to the lobby."
#                 )
#
#                 state["current_room"] = "lobby"
#                 return
#             case "go to lobby":
#                 state["current_room"] = "lobby"
#                 return
#             case "quit":
#                 exit()
#
#
# if __name__ == "__main__":
#     # This runs only when testing the room standalone
#     import sys
#     from pathlib import Path
#     from datetime import timedelta as TimeDelta
#
#     # Add parent directory to Python path so we can import from main folder
#     parent_dir = Path(__file__).parent.parent
#     sys.path.insert(0, str(parent_dir))
#
#     # Create test state
#     test_state = State(
#         player_name="TestPlayer",
#         current_room="project_room_1",
#         previous_room="",
#         visited_rooms=[],
#         time_played=TimeDelta(),
#         inventory=[],
#     )
#
#     project_room_1(test_state)

from copy import deepcopy
from models import Command, State
from util import (
    display_invalid_syntax,
    display_go_help,
    display_go_list,
    display_invalid_command,
    display_leaderboard,
    display_stats,
    display_take_help,
    display_take_list,
    get_user_input,
    pause_game,
    quit_game,
)

def project_room_1(state: State):
    state_snapshot = deepcopy(state)

    if "project_room_1" not in state.visited_rooms:
        state.visited_rooms.append("project_room_1")
    else:
        print("You already got the Computer passcode and see no reason to go back in..")
        state.current_room = state.previous_room
        return state

    can_use_look = True
    can_choose_action = False
    pickable_items: list[str] = []

    while True:
        cmd, *args = get_user_input()

        match cmd:
            case Command.help:
                raise NotImplementedError
            case Command.look:
                if can_use_look:
                    print(
                        "You see a barren classroom with something written on the whiteboard. You take a closer look. It seems to be a password to a computer, but it is encrypted. On the whiteboard, it say."
                    )
                    print(
                        "Dial 1 is a prime number greater than 5.\n"
                        "Dial 2 is the smallest prime number.\n"
                        "Dial 3 equals (Dial 1 + Dial 4 − Dial 2).\n"
                        "Dial 4 is a perfect square digit, it’s even, and it’s greater than 2.\n"
                        "Dial 5 shows a number that is exactly one less than Dial 1.\n"
                        "Self-check: The sum of all five digits should be 28."
                    )
                    can_choose_action = True
                    continue
            case Command.answer:
                if can_choose_action:
                    if not args:
                        display_invalid_syntax("answer")
                        continue

                    answer = " ".join(args)
                    if answer == "72946":
                        print(
                            "Correct, You solved the puzzle and wrote down the combination on a piece of paper, and return to the lobby."
                        )
                        can_use_look = False
                        state.current_room = "lobby"
                        return state
                    else:
                        print("Wrong answer. Try again.")
                        continue
            case Command.take:
                if len(pickable_items) > 0:
                    if len(args) != 1:
                        display_invalid_syntax("take")
                        continue
                    match " ".join(args):
                        case "?":
                            display_take_help()
                            continue
                        case "list":
                            display_take_list(pickable_items)
                            continue
            case Command.go:
                if len(args) != 1:
                    display_invalid_syntax("go")
                    continue
                match " ".join(args):
                    case "?":
                        display_go_help()
                        continue
                    case "list":
                        display_go_list(["east_corridor"])
                        continue
            case Command.quit:
                quit_game()
            case Command.pause:
                pause_game(state)
            case Command.stats:
                display_stats()
                continue
            case Command.leaderboard:
                display_leaderboard()
                continue

        display_invalid_command()
