from copy import deepcopy

from models import Command, State
from util import (
    display_help,
    display_invalid_command,
    display_invalid_syntax,
    display_leaderboard,
    display_stats,
    get_user_input,
    pause_game,
    quit_game,
)


def front_desk_office(state):
    state_snapshot = deepcopy(state)

    print(
        "You step into the room\n"
        "Possible commands:\n"
        "Look\n"
        "Quit"
    )
    can_use_look = True
    can_choose_action = False
    pickable_items: list[str] = []
    challenge1 = True

    while True:
        cmd, *args = get_user_input()

        match cmd:
            case Command.help:
                if len(args) == 1 and args[0] == "around":
                    display_help()
                else:
                    display_invalid_command()
                continue

            case Command.go:
                if len(args) != 1:
                    display_invalid_syntax("go")
                else:
                    display_invalid_command()
                continue

            case Command.look:
                if can_use_look:
                    print(
                        "You enter the Front Desk office. A zombie is slumped in a chair, seemingly asleep.\n"
                        "The room is filled with clutter, and you notice a glint of metal under the zombie.\n"
                        "It is the Master Key and you’ll have to retrieve it carefully without waking the zombie."
                    )
                    print(
                        "Possible commands:\n"
                        "1.look\n"
                        "2.fight\n"
                        "3.sneak around"
                    )
                    can_choose_action = True

                    choice = input("> ").strip().lower()
                    match choice:
                        case "1" | "look":
                            print(
                                "You look around the room for anything useful in this situation.\n"
                                "You see a jacket left behind by a student on a chair. You pick it up.\n"
                                "Maybe it could be helpful to tie the zombie up.\n"
                                "Possible commands:\n"
                                "1.fight\n"
                                "2.tie his face\n"
                                "3.tie his body"
                            )
                            choice = input("> ").strip().lower()
                            match choice:
                                case "1":
                                    print("You died.\n(You will be returned to the start of the room)")
                                    state = deepcopy(state_snapshot)
                                    return state
                                case "2":
                                    print(
                                        "You tie the zombie up and approach the key.\n"
                                        "However, the zombie smells you and attacks.\n"
                                        "You die."
                                    )
                                    print("(You will be returned to the start of the room)")
                                    state = deepcopy(state_snapshot)
                                    return state
                                case "3":
                                    print(
                                        "You tie the zombie up and approach the key.\n"
                                        "The zombie wakes up but is unable to move.\n"
                                        "You take the key and immediately leave the room."
                                    )
                                    pickable_items.append("master_key")
                                    state.inventory.append("master_key")
                                    state.current_room = "north_corridor"
                                    return state
                                case _:
                                    print("Invalid option.")
                                    continue

                        case "2" | "fight":
                            print("You died.\n(You will be returned to the start of the room)")
                            state = deepcopy(state_snapshot)
                            return state

                        case "3" | "sneak around":
                            print(
                                "You immediately become silent and approach the zombie carefully.\n"
                                "Possible commands:\n"
                                "1.Move the zombie\n"
                                "2.Dig the key out from under the zombie"
                            )
                            choice = input("> ").strip().lower()
                            match choice:
                                case "1" | "move the zombie":
                                    print("You wake up the zombie. You have died.")
                                    print("(You will be returned to the start of the room)")
                                    state = deepcopy(state_snapshot)
                                    return state
                                case "2" | "dig the key out from under the zombie":
                                    print("You take the key and immediately leave the room.")
                                    pickable_items.append("master_key")
                                    state.inventory.append("master_key")
                                    state.current_room = "north_corridor"
                                    return state
                                case _:
                                    print("Invalid option.")
                                    continue
                        case _:
                            print("Invalid option.")
                            continue

                continue

            case Command.take:
                if len(pickable_items) > 0:
                    if len(args) != 1:
                        display_invalid_syntax("take")
                    else:
                        display_invalid_command()
                continue
            # case Command.where:
            #     display_where_am_i(state)
            #     continue
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

if __name__ == "__main__":
    from datetime import datetime as DateTime
    from datetime import timedelta as TimeDelta

    mock_state = State(
        player_name="mock",
        current_room="front_desk_office",
        previous_room="",
        visited_rooms=[],
        time_played=TimeDelta(),
        inventory=[],
        session_start_time=DateTime.now()
    )
    front_desk_office(mock_state)
