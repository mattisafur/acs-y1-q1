from models import Commands, State
from util import (
    display_go_help,
    display_go_invalid_syntax,
    display_go_list,
    display_invalid_command,
    display_inventory,
    get_user_input,
    pause_game,
    display_leaderboard,
    display_stats,
    quit_game,
)


def west_corridor(state: State):
    if "west_corridor" not in state.visited_rooms:
        state.visited_rooms.append("west_corridor")

    print("You are in the west corridor")

    display_go_list(["stair_exit", "classroom_2.035", "classroom_2.031", "project_room_4"])

    while True:
        command, *args = get_user_input()

        match command:
            case Commands.help:
                raise NotImplementedError
            case Commands.go:
                if len(args) != 1:
                    display_go_invalid_syntax()
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
                        return
                    case "classroom_2.035":
                        state.current_room = "classroom_2.035"
                        return
                    case "classroom_2.031":
                        state.current_room = "classroom_2.031"
                        return
                    case "project_room_4":
                        state.current_room = "project_room_4"
                        return
                    
                continue
            case Commands.look:
                print(
                    "The corridor is empty, nothing to see here, go choose your next room!"
                )
            case Commands.inventory:
                display_inventory(state)
            case Commands.quit:
                quit_game()
            case Commands.pause:
                pause_game(state)
            case Commands.stats:
                display_stats()
            case Commands.leaderboard:
                display_leaderboard()

        display_invalid_command()
