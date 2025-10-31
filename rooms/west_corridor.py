from models import Command, State
from util import (
    display_go_help,
    display_go_list,
    display_invalid_command,
    display_invalid_syntax,
    display_inventory,
    display_leaderboard,
    display_stats,
    display_help,
    get_user_input,
    pause_game,
    quit_game,
    display_map,
    display_where_am_i,
    display_items_list,
)


def west_corridor(state: State):
    if "west_corridor" not in state.visited_rooms:
        state.visited_rooms.append("west_corridor")

    print("You are in the west corridor")

    display_go_list(
        ["stair_exit", "classroom_2035", "classroom_2031", "project_room_4", "north_corridor"]
    )

    while True:
        command, *args = get_user_input()

        command = command.lower() if command else ""
        args = [a.lower() for a in args]

        match command:
            case "help":
                display_help()
                continue

            case "go":
                if len(args) != 1:
                    display_invalid_syntax("go")
                    continue

                match args[0]:
                    case "?":
                        display_go_help()
                        continue
                    case "list":
                        display_go_list(
                            [
                                "stair_exit",
                                "classroom_2035",
                                "classroom_2031",
                                "project_room_4",
                                "north_corridor",
                            ]
                        )
                        continue
                    case "stair_exit":
                        state.current_room = "stair_exit"
                        return state
                    case "classroom_2035" | "classroom_2031":
                        print("The door is locked.")
                        continue
                    case "project_room_4":
                        state.current_room = "project_room_4"
                        return state
                    case "north_corridor":
                        state.current_room = "north_corridor"
                        return state
                    case _:
                        display_invalid_command()
                        continue

            case "look":
                print(
                    "The corridor is empty, nothing to see here, go choose your next room!"
                )
                continue
            case "where":
                display_where_am_i(state)
                continue
            case "map":
                display_map()
                continue
            case "items":
                display_items_list()
                continue
            case "inventory":
                display_inventory(state)
                continue
            case "quit":
                quit_game()
                return state
            case "pause":
                pause_game(state)
                return state
            case "stats":
                display_stats(state)
                continue
            case "leaderboard":
                display_leaderboard()
                continue
            case _:
                display_invalid_command()
                continue


if __name__ == "__main__":
    from datetime import datetime, timedelta as TimeDelta

    mock_state = State(
        player_name="mock",
        current_room="west_corridor",
        previous_room="",
        visited_rooms=[],
        time_played=TimeDelta(),
        inventory=[],
        session_start_time=datetime.now(),
    )

    west_corridor(mock_state)