
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
    display_help,
)

def project_room_1(state: State):
    state_snapshot = deepcopy(state)

    # if "project_room_1" not in state.visited_rooms:
    #     state.visited_rooms.append("project_room_1")




    if "project_room_1" not in state.visited_rooms:
        state.visited_rooms.append("project_room_1")
    else:
        print("You already solved the puzzle in this room. You can look around, but there's nothing more to do.")
        state.current_room = state.previous_room
        return state

    # if state.project_room_1_solved:
    #     print("You already solved the puzzle in this room. You can look around, but there's nothing more to do.")
    #     state.current_room = state.previous_room
    #     return state

    # if "project_room_1" in getattr(state, "visited_rooms", []):
    #     print("You already solved the puzzle in this room. You can look around, but there's nothing more to do.")
    #     state.current_room = state.previous_room
    #     return state
    print("You enter the Project room 1\n"
        "Possible commands:\n"
        "Look\n"
        "Go to Lobby\n"
        "Quit")


    can_use_look = True
    can_choose_action = False
    pickable_items: list[str] = []

    while True:
        cmd, *args = get_user_input()

        match cmd:
            case Command.help:
                if len(args) == 1 and args[0] == "around":
                    display_help()
                    continue
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
                        state.project_room_1_solved = True
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
            # case Command.where:
            #     display_where_am_i(state)
                continue
            case Command.quit:
                quit_game()
            case Command.pause:
                pause_game(state)
            case Command.stats:
                display_stats(state)
                continue
            case Command.leaderboard:
                display_leaderboard()
                continue


        display_invalid_command()


# project_room_1(False)