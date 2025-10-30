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
    display_map,
    display_items_list,
    display_where_am_i,
)


def lobby(state: State):
    if "lobby" not in state.visited_rooms:
        state.visited_rooms.append("lobby")
        print("You are in the Lobby")
    else:
        print("You are back in the Lobby.")

    display_go_list(["north_corridor", "east_corridor", "project_room_1", "main_stair_exit"])

    while True:
        command, *args = get_user_input()
        command = command.lower()
        args = [arg.lower() for arg in args]

        match command:
            case Command.help.value:
                display_help()
                continue
            case Command.go.value:
                if len(args) != 1:
                    display_invalid_syntax("go")
                    continue

                target = args[0]
                match target:
                    case "?":
                        display_go_help()
                    case "list":
                        display_go_list(["north_corridor", "east_corridor", "project_room_1", "main_stair_exit"])
                    case "north_corridor" | "east_corridor" | "project_room_1":
                        state.previous_room = "lobby"
                        state.current_room = target
                        return state
                    case "main_stair_exit":
                        print("Sorry, it could be a nice way to get out, only if it won't be closed, try other doors.")
                        continue
            case Command.look.value:
                print("The Lobby is empty, nothing to see here, go choose your next destination!")
                continue
            case Command.map.value:
                display_map()
                continue
            case Command.where.value:
                display_where_am_i(state)
                continue
            case Command.items.value:
                display_items_list()
                continue
            case Command.inventory.value:
                display_inventory(state)
                continue
            case Command.quit.value:
                quit_game()
            case Command.pause.value:
                pause_game(state)
            case Command.stats.value:
                display_stats(state)
                continue
            case Command.leaderboard.value:
                display_leaderboard()
                continue

        display_invalid_command()
