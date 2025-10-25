from copy import deepcopy
from models import Command, State
from util import (
    display_invalid_syntax,
    display_go_help,
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
        print("You can hear zombies groaning in the room. Since you already obtained what you needed here, going back would be too risky.")
        state.current_room = state.previous_room
        return state

    if not hasattr(state, "visited_rooms"):
        state.visited_rooms = []
    state.visited_rooms.append("storage_room")

    print("You step into the storage room.\nThe air is dusty and the lights are out, leaving only thin beams of light cutting through the darkness. To the left, an overturned table blocks part of the way.\nTo the right, a tall cabinet looms, obscuring much of the corner.\nStraight ahead, a narrow path twists through fallen debris and chairs."
          "\nType 'look' to go around the room")

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
            case Command.help:
                print("Possible commands:\nlook    look around the room\nanswer  choose a path (left|right|forward)\ntake    pick up an item\ngo      go to another room\nstats   display your stats\nleaderboard view the leaderboard\npause   save and quit the game\nquit    quit the game without saving")
                continue
            case Command.look:
                if can_use_look:
                    print("Shadows stretch between shelves and toppled furniture.\nThe cabinet on the right looks reachable if careful, \nbut shifting the table to the left could be loud, and the narrow path ahead is littered with loose scrap.")
                    print("Use: answer left | answer right | answer forward")
                    can_choose_action = True
                    can_use_look = False
                else:
                    print("The cabinet on the right still stands where it is, and the room remains tense and quiet.")
                continue
            case Command.answer:
                if not can_choose_action or len(args) != 1:
                    display_invalid_syntax()
                    continue
                choice = args[0].strip().lower()
                if choice == "left":
                    print("You push against the overturned table.\nIt scrapes loudly across the floor, echoing through the room. Groans surge closer—zombies rush in.\nGame over. (You will be returned to the start of the room)")
                    return deepcopy(state_snapshot)
                if choice == "forward":
                    print("You squeeze into the debris path, but a metal rod clatters free and crashes to the floor.\nThe noise carries—zombies converge. Game over. (You will be returned to the start of the room)")
                    return deepcopy(state_snapshot)
                if choice == "right":
                    print("You edge over to the tall cabinet and feel along the top-left shelf.\nYour fingers close around a sturdy hammer hidden in the darkness.")
                    if "hammer" not in pickable_items:
                        pickable_items.append("hammer")
                    print("You can now take hammer with command: 'take hammer'")
                    continue
                print("Invalid choice. Try: left | right | forward.")
                continue
            case Command.take:
                if not pickable_items:
                    display_take_help()
                    continue
                if len(args) != 1:
                    display_invalid_syntax()
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
                    print("You pick up the hammer and hold it firmly.\nYou decide to go back to North Corridor.\n\n")
                    if not hasattr(state, "inventory"):
                        state.inventory = []
                    if "hammer" not in state.inventory:
                        state.inventory.append("hammer")
                    state.previous_room = "storage_room"
                    state.current_room = "north_corridor"
                    return state
                else:
                    display_invalid_command()
                continue
            case Command.go:
                if len(args) != 1:
                    display_invalid_syntax()
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
                    return state
                display_invalid_syntax()
                continue
            case Command.stats:
                display_stats()
                continue
            case Command.leaderboard:
                display_leaderboard()
                continue
            case Command.pause:
                pause_game(state)
                return state
            case Command.quit:
                quit_game()
                return state
            case _:
                display_invalid_command()
                continue

