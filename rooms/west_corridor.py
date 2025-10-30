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
)


def west_corridor(state: State):
    if "west_corridor" not in state.visited_rooms:
        state.visited_rooms.append("west_corridor")

    print("You are in the west corridor")

    display_go_list(
        ["stair_exit", "classroom_2.035", "classroom_2.031", "project_room_4"]
    )

    while True:
        command, *args = get_user_input()

        match command:
            case Command.help:
                if len(args) == 1 and args[0] == "around":
                    display_help()
                    continue

            case Command.go:
                if len(args) != 1:
                    display_invalid_syntax("go")
                    continue

                match args[0]:
                    case "?":
                        display_go_help()
                    case "list":
                        display_go_list(
                            [
                                "stair_exit",
                                "classroom_2.035",
                                "classroom_2.031",
                                "project_room_4",
                            ]
                        )
                    case "stair_exit":
                        state.current_room = "stair_exit"
                        return state
                    case "classroom_2.035":
                        state.current_room = "classroom_2.035"
                        return state
                    case "classroom_2.031":
                        state.current_room = "classroom_2.031"
                        return state
                    case "project_room_4":
                        state.current_room = "project_room_4"
                        return state

                continue

            case Command.look:
                print(
                    "The corridor is empty, nothing to see here, go choose your next room!"
                )
                continue
            case Command.inventory:
                display_inventory(state)
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


if __name__ == "__main__":
    from datetime import datetime as DateTime
    from datetime import timedelta as TimeDelta

    mock_state = State(
        player_name="mock",
        current_room="west_corridor",
        previous_room="",
        visited_rooms=[],
        time_played=TimeDelta(),
        inventory=[],
        session_start_time=DateTime.now()
    )

    west_corridor(mock_state)
