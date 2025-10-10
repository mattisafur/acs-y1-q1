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
    get_user_input,
    pause_game,
    quit_game,
)


def teacher_room_3(state: State):
    state_snapshot = deepcopy(state)

    if "teacher_room_3" not in state.visited_rooms:
        # set room as visited
        state.visited_rooms.append("teacher_room_3")
    else:
        # allow re-entry but notify player
        print("You have already visited this room before.")
        state.current_room = state.previous_room
        return

    # prologue
    print(
        "You step into the teacher's lounge. Papers are scattered everywhere, coffee mugs still half full as if abandoned in a hurry. \n"
        "A bookshelf is tilted precariously, blocking part of the exit. The room feels eerie in its stillness, \n"
        "as though the teachers left in the middle of their day.\n"
    )

    puzzle_solved = False

    while True:
        # split the user input to the command (string) and the arguments (list of strings)
        cmd, *args = get_user_input()

        match cmd:
            case Command.help:
                raise NotImplementedError
            case Command.look:
                if not puzzle_solved:
                    print(
                        "The teacher's lounge is a mess. The bookshelf looks unstable and could fall at any moment.\n"
                        "On the desk are four folders labeled A, B, C, D. Each has a note stuck to it:\n"
                        "  Folder A: 'Comes after B.'\n"
                        "  Folder B: 'Must be first.'\n"
                        "  Folder C: 'Is never next to A.'\n"
                        "  Folder D: 'Always after C.'\n"
                        "A whiteboard reads: 'Put knowledge in the right order. Only then the truth is revealed.'\n"
                    )

                    # Now ask for the answer directly
                    while True:
                        print("Enter the correct order (e.g., ABCD):")
                        user_answer = get_user_input()
                        answer = "".join(user_answer).strip().upper()

                        if answer == "BCDA":
                            print(
                                "Correct! The folders click into place.\n"
                                "You hear a soft mechanical sound as the bookshelf slowly rights itself,\n"
                                "revealing a clear path to the exit. You feel a sense of accomplishment."
                            )
                            puzzle_solved = True
                            break
                        else:
                            print(
                                "Incorrect! The bookshelf groans ominously. That doesn't seem right."
                            )
                            print("(You will be returned to the start of the room)")
                            state = state_snapshot
                            return
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
                            return
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
