from copy import deepcopy
import time

from models import Command, State
from util import (
    display_go_help,
    display_go_list,
    display_help,
    display_invalid_command,
    display_invalid_syntax,
    display_inventory,
    display_items_list,
    display_leaderboard,
    display_stats,
    display_take_help,
    display_take_list,
    display_where_am_i,
    display_map,
    get_user_input,
    pause_game,
    quit_game,
)


def front_desk_office(state):
    state_snapshot = deepcopy(state)

    print(
        "You enter the Front Desk office. Use look around to explore further"
    )
    can_use_look = True
    can_choose_action = False
    pickable_items: list[str] = []

    while True:
        cmd, *args = get_user_input()
        cmd = cmd.lower() if cmd else ""
        args = [a.lower() for a in args]

        match cmd:
            case Command.help:
                display_help()
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
                        "A zombie is slumped in a chair, seemingly asleep.\n"
                        "The room is filled with clutter, and you notice a glint of metal under the zombie.\n"
                        "It is the Master Key and you’ll have to retrieve it carefully without waking the zombie."
                    )
                    print(
                        "Possible commands:\n"
                        "1.go around the room\n"
                        "2.sneak around the zombie"
                    )
                    can_choose_action = True  # NOTE unused variable

                    choice = input("> ").strip().lower()
                    match choice:
                        case "1" | "go around the room" | "go around":
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
                                case "1" | "fight":
                                    print("You try to kick the zombie and he wakes up\n"
                                          "He is not happy\n"
                                          "'I have never waken you up while you were sleeping in class, bastard'\n"
                                          "he says as he has his hand around your neck and throws you against the wall\n"
                                          "You are dead")
                                    state = deepcopy(state_snapshot)
                                    return state
                                case "2" | "tie his face":
                                    print(
                                        "You carefully tie the zombie up and inch closer to the glinting key.\n"
                                        "Suddenly, the zombie twitches and sniffs the air, noticing you there\n"
                                        "It lunges at you with a terrifying roar.\n"
                                        "You’re overwhelmed, and the struggle ends here…\n"
                                        "You will be returned to the start of the room")
                                    state = deepcopy(state_snapshot)
                                    return state
                                case "3" | "tie his body":
                                    print(
                                        "You skillfully tie the zombie's body, rendering it completely immobile.\n"
                                        "You reach under it and spot the  Master Key.\n"
                                        "Type 'take master_key' to take the Master Key.\n"

                                    )
                                    pickable_items.append("master_key")
                                    state.inventory.append("master_key")
                                    state.current_room = "north_corridor"
                                    return state
                                case _:
                                    print("Invalid option.")
                                    continue

                        case "2" | "sneak around" | "sneak around the zombie":
                            print(
                                "You immediately become silent and approach the zombie carefully.\n"
                                "Possible commands:\n"
                                "1.Move the zombie\n"
                                "2.Dig the key out from under the zombie"
                            )
                            choice = input("> ").strip().lower()
                            match choice:
                                case "1" | "move the zombie":
                                    print(
                                        "You accidentally jostle the zombie awake!\n"
                                        "Its eyes snap open, and it lunges at you with terrifying speed!\n"
                                        "You struggle, but there’s no escape this time.\n"
                                        "(Returning you to the start of the room…)"
                                    )
                                    state = deepcopy(state_snapshot)
                                    return state
                                case "2" | "dig the key out from under the zombie":
                                    print(
                                        "You carefully reach under the zombie, holding your breath.\n"
                                        "Your fingers brush against something cold and metallic...\n"
                                        "It's the Master Key! You snatch it up quietly.\n"
                                        "To pick up the Master Key, type 'take master_key'"
                                    )
                                    pickable_items.append("master_key")
                                    can_use_look = False
                                case _:
                                    print("Invalid option.")
                                    continue
                        case _:
                            print("Invalid option.")
                            continue
                continue

            case "take":
                if len(pickable_items) > 0:
                    if len(args) != 1:
                        display_invalid_syntax("take")
                        continue
                    arg = args[0].lower()
                    match arg:
                        case "?":
                            display_take_help()
                        case "list":
                            display_take_list(pickable_items)
                        case "master_key":
                            print("You picked up the master_key and head back to North Corridor")
                            time.sleep(1.5)
                            state.inventory.append("master_key")
                            state.current_room = "north_corridor"
                            return state
                        case _:
                            print("You can't take that.")
                    continue

            case Command.go:
                if len(args) != 1:
                    display_invalid_syntax("go")
                    continue
                match args[0].lower():
                    case "?":
                        display_go_help()
                        continue
            case Command.items:
                display_items_list()
                continue

            case Command.map:
                display_map()
                continue

            case Command.inventory:
                display_inventory(state)
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

            case Command.where:
                display_where_am_i(state)
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
