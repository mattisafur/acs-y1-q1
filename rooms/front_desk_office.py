# import copy
#
# from models import State
# from util import get_user_input
#

from copy import deepcopy

from models import Command, State
from util import (
    display_go_help,
    display_go_list,
    display_invalid_command,
    display_invalid_syntax,
    display_leaderboard,
    display_stats,
    display_take_help,
    display_take_list,
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
        "Go to North Corridor\n"
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
                raise NotImplementedError

            case Command.look:
                if can_use_look:
                    print(
                        "You enter the Front Desk office. A zombie is slumped in a chair, seemingly asleep.\n"
                        "The room is filled with clutter, and you notice a glint of metal under the zombie.\n"
                        "It is the Master Key and you’ll have to retrieve it carefully without waking the zombie."
                    )
                    print(
                        "Possible commands:\n"
                        "look\nfight\nsneak around"
                    )
                    can_choose_action = True
                continue

            case Command.answer:
                if can_choose_action:
                    if not args:
                        display_invalid_syntax("answer")
                        continue

                    match " ".join(args):
                        case "look":
                            print(
                                "You look around the room for anything useful in this situation.\n"
                                "You see a jacket left behind by a student on a chair. You pick it up.\n"
                                "Maybe it could be helpful to tie the zombie up.\n"
                                "Possible commands:\n"
                                "fight\n"
                                "tie his face\n"
                                "tie his body"
                            )

                            cmd, *args = get_user_input()

                            match cmd:
                                case Command.answer:
                                    if challenge1:
                                        if not args:
                                            display_invalid_syntax("answer")
                                            continue

                                        match " ".join(args):
                                            case "fight":
                                                print("You died.\n(You will be returned to the start of the room)")
                                                state = deepcopy(state_snapshot)
                                                return state
                                            case "tie his face":
                                                print(
                                                    "You tie the zombie up and approach the key.\n"
                                                    "However, the zombie smells you and attacks.\n"
                                                    "You die."
                                                )
                                                print("(You will be returned to the start of the room)")
                                                state = deepcopy(state_snapshot)
                                                return state
                                            case "tie his body":
                                                print(
                                                    "You tie the zombie up and approach the key.\n"
                                                    "The zombie wakes up but is unable to move.\n"
                                                    "You take the key and immediately leave the room."
                                                )
                                                pickable_items.append("master_key")
                                                state.inventory.append("master_key")
                                                state.current_room = "north_corridor"
                                                return state
                                            case "Go to north corridor":
                                                print("You died.\n(You will be returned to the start of the room)")
                                                state = deepcopy(state_snapshot)
                                                return state
                            continue

                        case "sneak around":
                            print(
                                "You immediately become silent and approach the zombie carefully.\n"
                                "Any action from here on out has to be very quiet. You have to type\n"
                                "out every action with lowercase letters to not wake the zombie up."
                            )
                            print(
                                "Possible commands:\n"
                                "Move the zombie\n"
                                "Dig the key out from under the zombie"
                            )

                            cmd, *args = get_user_input()

                            match cmd:
                                case Command.answer:
                                    if challenge1:
                                        if not args:
                                            display_invalid_syntax("answer")
                                            continue

                                        match " ".join(args):
                                            case "move the zombie":
                                                print("You wake up the zombie. You have died.")
                                                print("(You will be returned to the start of the room)")
                                                state = deepcopy(state_snapshot)
                                                return state
                                            case "dig the key out from under the zombie":
                                                print("You take the key and immediately leave the room.")
                                                pickable_items.append("master_key")
                                                state.inventory.append("master_key")
                                                state.current_room = "north_corridor"
                                                return state
                            continue

                        case "fight":
                            print("You died.\n(You will be returned to the start of the room)")
                            state = deepcopy(state_snapshot)
                            return state

            case Command.take:
                if len(pickable_items) > 0:
                    if len(args) != 1:
                        display_invalid_syntax("take")

