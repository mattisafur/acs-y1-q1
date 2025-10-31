import time
from copy import deepcopy
from rooms.north_corridor import north_corridor

from models import Command, State

from util import (
    display_go_help,
    display_go_list,
    display_help,
    display_invalid_command,
    display_invalid_syntax,
    display_leaderboard,
    display_stats,
    display_take_help,
    display_take_list,
    get_user_input,
    pause_game,
    quit_game,
    display_map,
    display_inventory,
    display_where_am_i,
    display_items_list,
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

    print("You step into the storage room.\nThe air is dusty and the lights are out, leaving only thin beams of light cutting through the darkness.\n To the left, an overturned table blocks part of the way.\nTo the right, a tall cabinet looms, obscuring much of the corner.\nStraight ahead, a narrow path twists through fallen debris and chairs.\n\nType 'look' to explore around the room")

    can_use_look = True
    can_choose_action = False
    pickable_items: list[str] = []

    while True:
        tokens = get_user_input()

        if not tokens:
            display_invalid_command()
            continue

        tokens_lower = [t.lower() for t in tokens]
        user_input = " ".join(tokens_lower).strip()
        cmd_lower, *args_lower = tokens_lower

        matched_command = None

        for c in Command:
            if cmd_lower == c.value.lower():
                matched_command = c
                break

        if matched_command:
            cmd = matched_command
            args = args_lower

            match cmd:
                case Command.where:
                    display_where_am_i(state)
                    continue

                case Command.items:
                    display_items_list()
                    continue

                case Command.inventory:
                    display_inventory(state)
                    continue

                case Command.map:
                    display_map()
                    continue

                case Command.help:
                    display_help()
                    continue

                case Command.look:
                    if can_use_look:
                        print("Shadows stretch between shelves and toppled furniture.\nThe cabinet on the right looks reachable if careful, \nbut shifting the table to the left could be loud, and the narrow path ahead is littered with loose scrap.")
                        print("Choose: left | right | forward")
                        can_choose_action = True
                        can_use_look = False
                    else:
                        print("To explore more, try: left | right | forward")
                    continue

                    # if len(args) == 1 and args[0] == "around":
                    #     if can_use_look:
                    #         print("Shadows stretch between shelves and toppled furniture.\nThe cabinet on the right looks reachable if careful, \nbut shifting the table to the left could be loud, and the narrow path ahead is littered with loose scrap.")
                    #         print("Choose: left | right | forward")
                    #         can_choose_action = True
                    #         can_use_look = False
                    #     else:
                    #         print("To explore more, try: left | right | forward")
                    #     continue
                case Command.take:
                    if not pickable_items:
                        display_take_help()
                        continue

                    if len(args) != 1:
                        display_invalid_syntax("take")
                        continue

                    item = args[0].lower()

                    if item == "?":
                        display_take_help()
                        continue

                    if item == "list":
                        display_take_list(pickable_items)
                        continue

                    if item in pickable_items:
                        print(f"You pick up the {item} and hold it firmly.\nYou decide to go back to North Corridor.\n\n")

                        if not hasattr(state, "inventory"):
                            state.inventory = []

                        if item not in state.inventory:
                            state.inventory.append(item)

                        state.previous_room = "storage_room"
                        state.current_room = "north_corridor"
                        return north_corridor(state)
                    else:
                        display_invalid_command()
                    continue

                case Command.go:
                    if len(args) != 1:
                        display_invalid_syntax("go")
                        continue

                    dest = args[0].lower()

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

                    display_invalid_syntax("go")
                    continue

                case Command.stats:
                    display_stats(state)
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

        if can_choose_action:
            choice = user_input.split()[0] if user_input.split() else ""

            if choice == "left":
                print("You push against the overturned table.\nIt scrapes loudly across the floor, echoing through the room. Groans surge closer—zombies rush in.\nGame over.\n(You will be returned to the start of the room)")
                time.sleep(1)
                return deepcopy(state_snapshot)

            elif choice == "forward":
                print("You squeeze into the debris path, but a metal rod clatters free and crashes to the floor.\nThe noise carries—zombies converge. Game over.\n(You will be returned to the start of the room)")
                time.sleep(1)
                return deepcopy(state_snapshot)

            elif choice == "right":
                print("You edge over to the tall cabinet and feel along the top-left shelf.\nYour fingers close around a sturdy hammer hidden in the darkness.")

                if "hammer" not in pickable_items:
                    pickable_items.append("hammer")

                print("You can now take hammer with command: 'take hammer'")
                can_choose_action = False
                can_use_look = True
                continue

            else:
                print("Invalid choice. Try: left | right | forward.")
                continue


if __name__ == "__main__":
    from datetime import datetime
    from models import State
    from datetime import timedelta as TimeDelta

    test_state = State(
        player_name="TestPlayer",
        current_room="storage_room",
        previous_room="north_corridor",
        visited_rooms=[],
        time_played=TimeDelta(),
        inventory=[],
        session_start_time=datetime.now(),
    )

    storage_room(test_state)