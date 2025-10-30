from copy import deepcopy

from models import Command, State
from util import (
    display_delete_help,
    display_go_list,
    display_help,
    display_invalid_command,
    display_invalid_syntax,
    display_inventory,
    display_leaderboard,
    display_stats,
    display_take_help,
    display_take_list,
    display_where_am_i,
    get_user_input,
    pause_game,
    quit_game,
)


def project_room_1(state: State):
    state_snapshot = deepcopy(state)

    if "project_room_1" not in state.visited_rooms:
        state.visited_rooms.append("project_room_1")
        print("You enter the Project room 1\nUse 'look' around to explore the room.")
    else:
        print("You already solved the puzzle in this room. You can look around, but there's nothing more to do.")
        state.current_room = state.previous_room
        return state


    can_use_look = True
    can_choose_action = False
    pickable_items: list[str] = []

    while True:
        cmd, *args = get_user_input()

        match cmd:
            case Command.help:
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
                        "Self-check: The sum of all five digits should be 28.\n"
                        "Type 'answer' before your number"
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
                            "Correct! You solved the puzzle and wrote down the combination on a piece of paper.\n"
                            "You return now to the lobby."
                        )
                        can_use_look = False
                        state.inventory.append("Code 72946, from project room")
                        state.current_room = "lobby"
                        return state
                    else:
                        print("Wrong answer. Try again.")
                        continue
            case Command.take:
                if len(args) != 1:
                    display_invalid_syntax("take")
                    continue

                match args[0]:
                    case "?":
                        display_take_help()
                        continue
                    case "list":
                        display_take_list(pickable_items)
                        continue
                    case "Code 72946, from project room":
                        if "Code 72946, from project room" in pickable_items:
                            state.inventory.append("Code 72946, from project room")
                            state.current_room = "lobby"
                            return state
                        else:
                            print("You can't take this. Try again")
                            continue
                    case _:
                        print("You can't take this. Try again")
                        continue

            case Command.delete:
                if len(args) != 1:
                    display_invalid_syntax("delete")
                    continue

                match args[0]:
                    case "?":
                        display_delete_help()
                        continue
                    case _:
                        print("delete ?")
                        display_delete_help()
                        continue
            case Command.go:
                if len(args) != 1:
                    display_invalid_syntax("go")
                    continue
                match args[0]:
                    case "?":
                        print("go <room name>\n"
                              "'go' should be typed before room name\n")
                        continue
                    case "list":
                        display_go_list(["east_corridor"])
                        continue
            case Command.where:
                display_where_am_i(state)
                continue
            case Command.quit:
                quit_game()
            case Command.pause:
                pause_game(state)
            case Command.stats:
                display_stats(state)
                continue
            case Command.inventory:
                display_inventory(state)
            case Command.leaderboard:
                display_leaderboard()
                continue
            case _:
                display_invalid_command()
        continue

if __name__ == "__main__":
    from datetime import datetime as DateTime
    from datetime import timedelta as TimeDelta

    test_state = State(
        player_name="TestPlayer",
        current_room="project_room_1",
        previous_room="",
        visited_rooms=[],
        time_played=TimeDelta(),
        inventory=[],
        session_start_time=DateTime.now(),
    )
    project_room_1(test_state)
