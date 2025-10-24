from models import Command, State
from util import (
    display_go_help,
    display_go_list,
    display_invalid_command,
    display_invalid_syntax,
    display_inventory,
    display_leaderboard,
    display_stats,
    get_user_input,
    pause_game,
    quit_game,
)


def lobby(state: State):
    # Check if this is the first time visiting the lobby
    if "lobby" not in state.visited_rooms:
        state.visited_rooms.append("lobby")
        print("You are in the Lobby")
    else:
        print("You are back in the Lobby.")

    display_go_list(["north_corridor", "east_corridor", "project_room_1", "main_stair_exit"])

    while True:
        # split the user input to the command (string) and the arguments (list of strings)
        command, *args = get_user_input()

        match command:
            case Command.help:
                raise NotImplementedError
            case Command.go:
                if len(args) != 1:
                    display_invalid_syntax("go")
                    continue

                match args[0]:
                    case "?":
                        display_go_help()
                    case "list":
                        display_go_list(["north_corridor", "east_corridor", "project_room_1", "main_stair_exit"])
                    case "north_corridor":
                        # Check if user has item (based on flowchart)
                        if len(state.inventory) > 0:
                            state.current_room = "north_corridor"
                            return
                        else:
                            print("")
                            continue
                    case "east_corridor":
                        state.current_room = "east_corridor"
                        return state
                    case "project_room_1":
                        state.current_room = "project_room_1"
                        return state
                    case "main_stair_exit":
                        print("Sorry, it could be a nice way to get out, only if it won't be closed, try other doors.")
                        continue

                continue
            case Command.look:
                print(
                    "The Lobby is empty, nothing to see here, go choose your next destination!"
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
    from datetime import timedelta as TimeDelta

    mock_state = State(
        player_name="TestPlayer",
        current_room="lobby",
        previous_room="",
        visited_rooms=[],
        time_played=TimeDelta(),
        inventory=[],
    )

    lobby(mock_state)
