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
    quit_game, display_take_help, display_where_am_i,
)


def east_corridor(state: State):
    # mark east corridor as visited if it has not yet been
    if "east_corridor" not in state.visited_rooms:
        state.visited_rooms.append("east_corridor")

    print("You are in the east corridor")

    display_go_list(["lab_2001", "lab_2003", "lobby"])

    while True:
        command, *args = get_user_input()

        match command:
            case Command.help:

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
                        display_go_list(["lab_2001", "lab_2003", "lobby"])
                    case "lab_2001":
                        state.current_room = "lab_2001"
                        return state
                    case "lab_2003":
                        state.current_room = "lab_2003"
                        return state
                    case "lobby":
                        state.current_room = "lobby"
                        return state

                continue
            case Command.look:
                print(
                    "The corridor is empty, nothing to see here, go choose your next room!"
                )
                continue
            case Command.take:
                display_take_help()
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

        display_invalid_command()
