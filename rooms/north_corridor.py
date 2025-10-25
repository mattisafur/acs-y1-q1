from models import Command, State
from util import  (
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


def north_corridor(state: State):
    if "north_corridor" not in state.visited_rooms:
        state.visited_rooms.append("north_corridor")

    print("You are in the north corridor. Choose where you would like to go: ")

    available_rooms = [
        "lobby",
        "front_desk_office",
        "classroom_2_021",
        "classroom_2_015",
        "equinox_students_society",
        "storage_room",
        "project_room_3",
        "teachers_room_3",
        "teachers_room_2",
        "teachers_room_1",
        "west_corridor",
    ]

    display_go_list(available_rooms)

    while True:
        command, *args = get_user_input()

        match command:
            case Command.help:
                raise NotImplementedError

            case Command.go:
                if len(args) != 1:
                    display_invalid_syntax("go")
                    continue

                match args[0].lower():
                    case "?":
                        display_go_help()
                    case "list":
                        display_go_list(available_rooms)
                    case "lobby":
                        state.current_room = "lobby"
                        return state
                    case "front_desk_office":
                        state.current_room = "front_desk_office"
                        return state
                    case "storage_room":
                        state.current_room = "storage_room"
                        return state
                    case "project_room_1":
                        state.current_room = "project_room_1"
                        return state
                    case "teacher_room_3":
                        state.current_room = "teacher_room_3"
                        return state
                    case "west_corridor":
                        state.current_room = "west_corridor"
                        return state
                    case "classroom_2_021" | "classroom_2_015" | "equinox_students_society" | "project_room_3" | "teacher_room_1" | "teacher_room_2":
                        print("The door is locked.")
                        return state
                    case _:
                        print("Invalid destination.")
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

if __name__ == "__main__":
    import sys
    from pathlib import Path
    from datetime import timedelta as TimeDelta

    parent_dir = Path(__file__).parent.parent
    sys.path.insert(0, str(parent_dir))

    test_state = State(
        player_name="TestPlayer",
        current_room="north_corridor",
        previous_room="",
        visited_rooms=[],
        time_played=TimeDelta(),
        inventory=[],
    )

    north_corridor(test_state)
