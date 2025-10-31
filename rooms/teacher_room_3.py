from copy import deepcopy

from models import Command, State
from util import (
    display_go_help,
    display_go_list,
    display_help,
    display_invalid_command,
    display_invalid_syntax,
    display_inventory,
    display_leaderboard,
    display_stats,
    get_user_input,
    pause_game,
    quit_game,
    display_items_list,
    display_map,
    display_where_am_i
)


def teacher_room_3(state: State):
    state_snapshot = deepcopy(state)

    if "teacher_room_3" not in state.visited_rooms:
        state.visited_rooms.append("teacher_room_3")
    else:
        print("You have already visited this room before.")
        state.current_room = state.previous_room
        return state

    print(
        "You step into the teacher's lounge.\n"
        "The place is a mess—papers everywhere, coffee stains on the floor, and a bookshelf knocked over, partially blocking the exit.\n"
        "A low groan comes from behind the shelf. A zombie teacher slumps in a chair, half-asleep.\n"
        "On the desk, four folders labeled A, B, C, D catch your eye. Each has a note:\n"
        "  Folder A: 'Comes after D.'\n"
        "  Folder B: 'Must be first.'\n"
        "  Folder C: 'Is never next to A.'\n"
        "  Folder D: 'Always after C.'\n"
        "It looks like a puzzle. Solving it might trigger something… you wonder what."
    )

    puzzle_solved = False

    while True:
        user_input_list = get_user_input()
        if not user_input_list:
            continue

        cmd_str, *args = user_input_list
        cmd_str = cmd_str.lower()

        try:
            cmd_enum = Command(cmd_str)
        except ValueError:
            cmd_enum = None

        if (not puzzle_solved) and ("".join(user_input_list).strip().upper() == "BCDA"):
            print(
                "You arrange the folders correctly. Suddenly, a fire alarm blares loudly!\n"
                "Sprinklers activate and water cascades down from the ceiling, soaking you completely.\n"
                "The zombie teacher stirs but doesn’t notice you amid the chaos.\n"
                "Sputtering and dripping, you back away from the bookshelf and head back to the corridor, completely drenched."
            )
            puzzle_solved = True
            state.current_room = "north_corridor"
            return state

        match cmd_enum:
            case Command.help:
                display_help()
                continue
            case Command.look:
                print(
                    "The bookshelf still blocks the exit, and the zombie teacher hasn’t moved.\n"
                    "You examine the folders again, trying to figure out the right order."
                )
                if not puzzle_solved:
                    print("Enter the folder order (e.g., BCDA) to test it.")
                continue
            case Command.go:
                if len(args) != 1:
                    display_invalid_syntax("go")
                    continue
                direction = args[0].lower()
                match direction:
                    case "?":
                        display_go_help()
                        continue
                    case "list":
                        display_go_list(["north_corridor"])
                        continue
                    case "north_corridor":
                        if puzzle_solved:
                            print(
                                "Sopping wet but safe, you carefully exit the teacher's lounge\n"
                                "and return to the north corridor. What a chaotic detour!"
                            )
                            state.current_room = "north_corridor"
                            return state
                        else:
                            print(
                                "The bookshelf blocks your path. Maybe you should solve the folder puzzle first…"
                            )
                            continue
                    case _:
                        display_invalid_command()
                        continue
            case Command.items:
                display_items_list()
                continue
            case Command.map:
                display_map()
                continue
            case Command.where:
                display_where_am_i(state)
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
            case _:
                if "".join(user_input_list).strip().upper() != "BCDA":
                    display_invalid_command()
                continue

    return state


if __name__ == "__main__":
    from datetime import datetime as DateTime
    from datetime import timedelta as TimeDelta

    mock_state = State(
        player_name="mock",
        current_room="teacher_room_3",
        previous_room="",
        visited_rooms=[],
        time_played=TimeDelta(),
        inventory=[],
        session_start_time=DateTime.now()
    )

    teacher_room_3(mock_state)
