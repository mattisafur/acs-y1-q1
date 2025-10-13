import copy
from models import Command, State
from util import get_user_input, display_invalid_syntax, display_take_list, display_take_help, display_invalid_command

def front_desk_office(state):
    state_snapshot = copy.deepcopy(state)
    pickable_items = []

    print(
        "You step into the room\n"
        "Possible commands:\n"
        "Look\n"
        "Go to North Corridor\n"
        "Quit"
    )

    while True:
        cmd, *args = get_user_input()

        match cmd:
            case Command.help:
                raise NotImplementedError

            case Command.look:
                print(
                    "You enter the Front Desk office. A zombie is slumped in a chair, seemingly asleep.\n"
                    "The room is filled with clutter, and you notice a glint of metal under the zombie.\n"
                    "It is the Master Key and you’ll have to retrieve it carefully without waking the zombie."
                )
                continue

            case Command.answer:
                if not can_choose_action:
                    display_invalid_syntax("answer")
                    continue
                if not args:
                    display_invalid_syntax("answer")
                    continue

                choice = " ".join(args).strip().lower()
                if choice == "look":
                    print("You see a jacket left behind by a student. Maybe it could help.")
                    pickable_items.append("jacket")
                    continue
                elif choice == "fight":
                    print("You died")
                    state = state_snapshot
                    return
                elif choice == "sneak around":
                    print("You carefully try to retrieve the key.")
                    continue
                else:
                    print("Invalid choice")
                    continue

            case Command.take:
                if not pickable_items:
                    display_take_help()
                    continue
                if len(args) != 1:
                    display_invalid_syntax("take")
                    continue
                item = args[0].strip().lower()
                if item == "list":
                    display_take_list(pickable_items)
                    continue
                if item in pickable_items:
                    print(f"You pick up the {item}.")
                    if not hasattr(state, "inventory"):
                        state.inventory = []
                    if item not in state.inventory:
                        state.inventory.append(item)
                    continue
                display_invalid_command()
                continue

            case _:
                display_invalid_command()

if __name__ == "__main__":
    if __name__ == "__main__":
        from datetime import timedelta as TimeDelta

        mock_state = State(
            player_name="mock",
            current_room="front_desk_office",
            previous_room="",
            visited_rooms=[],
            time_played=TimeDelta(),
            inventory=[],
        )

        front_desk_office(mock_state)
