from copy import deepcopy

from models import Command, State
from util import (
    display_go_help,
    display_go_list,
    display_invalid_command,
    display_invalid_syntax,
    display_inventory,
    display_leaderboard,
    display_stats,
    display_take_help,
    display_take_list,
    display_help,
    get_user_input,
    pause_game,
    quit_game,
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
        "You step into the teacher's lounge. The place is a mess—papers everywhere, coffee stains on the floor, and a bookshelf knocked over, blocking the exit."
        " It's quiet, but you notice a low groan from behind the shelf. There's a zombie teacher slumped there, clutching a ring of keys."
        " If you want to get out, you'll need to move the shelf, but the teacher is in the way."
        " On the desk, you spot four folders labeled A, B, C, D. Each has a note:"
        " Look at the notes to figure out the correct order to unlock the exit."
    )

    puzzle_solved = False

    while True:
        cmd, *args = get_user_input()

        match cmd:
            case Command.help:
                if len(args) == 1 and args[0] == "around":
                    display_help()
                    continue

            case Command.look:
                if not puzzle_solved:
                    print(
                        "The shelf is blocking the exit, and the zombie teacher is still out cold."
                        " You look at the folders and the notes again."
                        "\n  Folder A: 'Comes after D.'"
                        "\n  Folder B: 'Must be first.'"
                        "\n  Folder C: 'Is never next to A.'"
                        "\n  Folder D: 'Always after C.'"
                        "\nFigure out the right order (e.g., BCDA) to unlock the exit."
                    )

                    while True:
                        print("Enter the folder order (e.g., BCDA):")
                        user_answer = get_user_input()
                        answer = "".join(user_answer).strip().upper()

                        if answer == "BCDA":
                            print(
                                "Nice! You got it. The shelf slides aside, and you grab the keys from the teacher before he wakes up."
                                " You slip out through the exit, heart pounding."
                            )
                            puzzle_solved = True
                            break
                        else:
                            print(
                                "Nope, that's not it. The shelf rattles, and the zombie teacher starts to stir. Better get out before he wakes up!"
                            )
                            print("You hurry back to the previous room.")
                            state = deepcopy(state_snapshot)
                            return state
                else:
                    print(
                        "You've already solved this puzzle. The bookshelf is no longer blocking the exit."
                    )
                continue

            case Command.go:
                if len(args) != 1:
                    display_invalid_syntax("go")
                    continue

                match args[0]:
                    case "?":
                        display_go_help()
                        continue
                    case "list":
                        display_go_list(["north_corridor"])
                        continue
                    case "north_corridor":
                        if puzzle_solved:
                            print(
                                "With the bookshelf out of the way,\n"
                                "you carefully navigate through the scattered papers and exit the teacher's lounge."
                            )
                            state.current_room = "north_corridor"
                            return state
                        else:
                            print(
                                "The tilted bookshelf is blocking your path. You need to solve the puzzle to clear the way."
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
            case _:
                display_invalid_command()

    return state


if __name__ == "__main__":
    from datetime import timedelta as TimeDelta

    mock_state = State(
        player_name="mock",
        current_room="teacher_room_3",
        previous_room="",
        visited_rooms=[],
        time_played=TimeDelta(),
        inventory=[],
    )

    teacher_room_3(mock_state)

