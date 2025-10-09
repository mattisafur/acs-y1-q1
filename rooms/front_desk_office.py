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


def front_desk_office(state: State):
    state_snapshot = deepcopy(state)

    if "front_desk_office" not in state.visited_rooms:
        # set room as visited
        state.visited_rooms.append("front_desk_office")
    else:
        # print that you don't want to be in this room and return to the previous room
        print("There is a zombie inside this room, you don't want to go in.")
        state.current_room = state.previous_room
        return

    can_use_look = True
    can_choose_action = False
    pickable_items: list[str] = []
    challenge1 = True
    challenge2 = True

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
                          "look\nfight\nsneak around"
                    )
                    can_choose_action = True
                    continue

            case Command.answer:
                if can_choose_action:
                    if not args:
                        display_invalid_syntax("answer")

                    match " ".join(args):
                        case "look":
                            print(
                                "You look around the room for anything useful in this situation.\n"
                                "you see a jacket left behind by a student on a chair. you pick it up\n"
                                "Maybe it could be helpful to tie the zombie up.\n"
                                "fight\n"
                                "tie his face\n"
                                "tie his body")

                            cmd, *args = get_user_input()

                            match cmd:
                                case Command.answer:
                                    if challenge1:
                                        if not args:
                                            display_invalid_syntax("answer")

                                        match " ".join(args):
                                            case "fight":
                                                print("you died")
                                                print("(You will be returned to the start of the room)")
                                                state = state_snapshot
                                                return
                                            case "tie his face":
                                                print("You tie the zombie up and approach the key.\n"
                                                      "However, the zombie smells you and attacks.\n"
                                                      "you die")
                                                print("(You will be returned to the start of the room)")
                                                state = state_snapshot
                                                return
                                            case "tie his body":
                                                print("You tie the zombie up and approach the key\n"
                                                      "The zombie wakes up but is unable to move.\n")
                                                print("you take the key and immediately leave the room"
                                                      )
                                                pickable_items.append(
                                                    "master_key")
                                                state.current_room = "north_corridor"
                                                return

                                            case "Go to north corridor":
                                                print("you died")
                                                print("(You will be returned to the start of the room)")
                                                state = state_snapshot
                                                return
                            continue
                        case "sneak around":
                            print("You sneak around the room. Every action you do from now on needs to be done in lower case to not wake up the zombie.")
                            print("move the zombie\ndig the key from under the zombie")
                            if challenge2:
                                # if any(char.isupper() for char in cmd):
                                if not args:
                                    display_invalid_syntax("answer")

                                cmd, *args = get_user_input()
                                match " ".join(args):
                                    case "move the zombie":
                                        print("you died")
                                        print("(You will be returned to the start of the room)")
                                        state = state_snapshot
                                        return
                                match " ".join(args):
                                    case "dig the key out from under the zombie":
                                        print("you take the key and immediately leave the room")
                                        pickable_items.append("master_key")
                                        state.current_room = "north_corridor"


                        case "fight":
                            print("you died")
                            print("(You will be returned to the start of the room)")
                            state = state_snapshot
                            return

            case Command.take:
                if len(pickable_items) > 0:
                    if len(args) != 1:
                        display_invalid_syntax("go")
                        continue

                    match args[0]:
                        case "?":
                            display_take_help()
                            continue
                        case "list":
                            display_take_list(pickable_items)
                            continue

        display_invalid_command()




if __name__ == "__main__":
    # This runs only when testing the room standalone
    import sys
    from datetime import timedelta as TimeDelta
    from pathlib import Path

    # Add parent directory to Python path so we can import from main folder
    parent_dir = Path(__file__).parent.parent
    sys.path.insert(0, str(parent_dir))

    # Create test state
    test_state = State(
        player_name="TestPlayer",
        current_room="front_desk_office",
        previous_room="",
        visited_rooms=[],
        time_played=TimeDelta(),
        inventory=[],
    )

    front_desk_office(test_state)