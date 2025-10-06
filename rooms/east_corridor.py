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


def east_corridor(state: State):
    if "east_corridor" not in state.visited_rooms:
        state.visited_rooms.append("east_corridor")

    print("You are in the east corridor")

    display_go_list(["lab_2001", "lab_2003", "lobby"])

    while True:
        user_input = get_user_input()

        match user_input.pop(0):
            case Commands.help:
                ...
            case Commands.go:
                args = user_input

                if len(args) != 1:
                    display_go_invalid_syntax()
                    continue

                match args[0]:
                    case "?":
                        display_go_help()
                    case "list":
                        display_go_list(["lab_2001", "lab_2003", "lobby"])
                    case "lab_2001":
                        state.current_room = "lab_2001"
                        return
                    case "lab_2003":
                        state.current_room = "lab_2003"
                        return
                    case "lobby":
                        state.current_room = "lobby"
                        return

                continue
            case Commands.look:
                print(
                    "The corridor is empty, nothing to see here, go choose your next room!"
                )
                continue
            case Commands.inventory:
                display_inventory(state)
                continue
            case Commands.quit:
                quit_game()
            case Commands.pause:
                pause_game(state)
            case Commands.stats:
                display_stats()
                continue
            case Commands.leaderboard:
                display_leaderboard()
                continue

        display_invalid_command()
