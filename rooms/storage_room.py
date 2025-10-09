from copy import deepcopy

from models import Commands, State
from util import (
    display_answer_invalid_syntax,
    display_go_help,
    display_go_invalid_syntax,
    display_go_list,
    display_invalid_command,
    display_leaderboard,
    display_stats,
    display_take_help,
    display_take_list,
    get_user_input,
    pause_game,
    quit_game,
)

def storage_room(state: State):
    state_snapshot = deepcopy(state)

    if "storage_room" in getattr(state, "visited_rooms", []):
        print(
            "You can hear zombies groaning in the room. Since you already obtained what you needed here, going back would be too risky."
        )
        state.current_room = state.previous_room
        return
    else:
        if not hasattr(state, "visited_rooms"):
            state.visited_rooms = []
        state.visited_rooms.append("storage_room")

    print(
        "You step into the storage room. The air is dusty and the lights are out, leaving only thin beams of light cutting through the darkness. "
        "To the left, an overturned table blocks part of the way. To the right, a tall cabinet looms, obscuring much of the corner. "
        "Straight ahead, a narrow path twists through fallen debris and chairs."
    )

    can_use_look = True
    can_choose_action = False
    pickable_items: list[str] = []

    while True:
        tokens = get_user_input()
        if not tokens:
            display_invalid_command()
            continue

        cmd, *args = tokens

        match cmd:
            case Commands.help:
                print(
                    "Possible commands:\n"
                    "look    look around the room\n"
                    "answer  choose a path (left|right|forward)\n"
                    "take    pick up an item\n"
                    "go      go to another room\n"
                    "stats   display your stats\n"
                    "leaderboard view the leaderboard\n"
                    "pause   save and quit the game\n"
                    "quit    quit the game without saving"
                )
                continue

            case Commands.look:
                if can_use_look:
                    print(
                        "Shadows stretch between shelves and toppled furniture. The cabinet on the right looks reachable if careful, "
                        "but shifting the table to the left could be loud, and the narrow path ahead is littered with loose scrap."
                    )
                    print("Use: answer left | answer right | answer forward")
                    can_choose_action = True
                    can_use_look = False
                else:
                    print(
                        "The cabinet on the right still stands where it is, and the room remains tense and quiet."
                    )
                continue

            case Commands.answer:
                if not can_choose_action or len(args) != 1:
                    display_answer_invalid_syntax()
                    continue

                choice = args[0].strip().lower()

                if choice == "left":
                    print(
                        "You push against the overturned table. It scrapes loudly across the floor, echoing through the room. "
                        "Groans surge closer—zombies rush in. Game over. (You will be returned to the start of the room)"
                    )
                    state = state_snapshot
                    return

                if choice == "forward":
                    print(
                        "You squeeze into the debris path, but a metal rod clatters free and crashes to the floor. "
                        "The noise carries—zombies converge. Game over. (You will be returned to the start of the room)"
                    )
                    state = state_snapshot
                    return

                if choice == "right":
                    print(
                        "You edge over to the tall cabinet and feel along the top-left shelf. "
                        "Your fingers close around a sturdy hammer hidden in the darkness."
                    )
                    if "hammer" not in pickable_items:
                        pickable_items.append("hammer")
                    print("You can now take: hammer")
                    continue

                print("Invalid choice. Try: left | right | forward.")
                continue

            case Commands.take:
                if not pickable_items:
                    display_take_help()
                    continue

                if len(args) != 1:
                    display_go_invalid_syntax()
                    continue

                match args[0]:
                    case "?":
                        display_take_help()
                        continue
                    case "list":
                        display_take_list(pickable_items)
                        continue

                item = args[0].strip().lower()
                if item in pickable_items and item == "hammer":
                    print("You pick up the hammer and hold it firmly.")
                    if not hasattr(state, "inventory"):
                        state.inventory = []
                    if "hammer" not in state.inventory:
                        state.inventory.append("hammer")
                else:
                    display_invalid_command()
                continue

            case Commands.go:
                if len(args) != 1:
                    display_go_invalid_syntax()
                    continue

                dest = args[0].strip().lower()
                if dest == "?":
                    display_go_help()
                    continue
                if dest == "list":
                    display_go_list(["north_corridor"])
                    continue
                if dest == "north_corridor":
                    print("You quietly retrace your steps and slip back into the corridor.")
                    state.previous_room = "storage_room"
                    state.current_room = "north_corridor"
                    return

                display_go_invalid_syntax()
                continue

            case Commands.stats:
                display_stats()
                continue

            case Commands.leaderboard:
                display_leaderboard()
                continue

            case Commands.pause:
                pause_game(state)
                continue

            case Commands.quit:
                quit_game()

            case _:
                display_invalid_command()
                continue
