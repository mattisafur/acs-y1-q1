from copy import deepcopy

from models import Command, State
from rooms.east_corridor import east_corridor
from util import (
    display_go_help,
    display_where_am_i,
    display_go_list,
    display_invalid_command,
    display_invalid_syntax,
    display_leaderboard,
    display_stats,
    display_take_help,
    display_take_list,
    display_help,
    get_user_input,
    pause_game,
    quit_game,
)


def lab_2001(state: State):
    state_snapshot = deepcopy(state)

    if "lab_2001" not in state.visited_rooms:
        state.visited_rooms.append("lab_2001")
    else:
        print("There is a zombie inside, you don't want to go in.")
        state.current_room = "east_corridor"
        return state

    print(
        "Useful information:\nCommand 'look around' for exploring inside the rooms \n? for displaying available commands\n")

    can_use_look = True
    can_choose_action = False
    pickable_items: list[str] = []

    while True:
        cmd, *args = get_user_input()

        # Allow direct commands for actions (handle multi-word)
        if can_choose_action:
            action_cmd = " ".join([cmd] + args).strip().lower()
            if action_cmd == "sneak":
                print(
                    "You notice a keycard on one of the desks.\nYou imagine is from the door of the laboratory.\nSo you decided to take it\n\n"
                    "To pick up the keycard, you should use the command 'take keycard'"
                )
                pickable_items.append("keycard")
                can_use_look = False
                continue
            elif action_cmd == "fly away":
                print(
                    "You flap your arms desperately, hoping to take off like a bird.\n"
                    "The zombies glance at you with amusement as you wobble unsteadily.\n"
                    "You lift off for a split second... and crash straight into a desk.\n"
                    "Pain shoots through your body, and before you can recover, the zombies surround you.\n"
                    "Being human, flight was never an option. You have met a grim fate.\n"
                    "GAME OVER."
                )
                print("(You will be returned to the start of the room.)")
                state.visited_rooms.remove("lab_2001")
                state = state_snapshot
                return state
            elif action_cmd == "fight":
                print(
                    "You try to fight one of your classmates.\n"
                    "They barely react and soon more zombies surround you.\n"
                    "You struggle, but you are only human.\n"
                    "The zombies overpower you.\n"
                    "GAME OVER."
                )
                print("(You will be returned to the start of the room.)")
                state.visited_rooms.remove("lab_2001")
                state = state_snapshot
                return state
            elif action_cmd == "set building on fire":
                print(
                    "You try to set the building on fire with what you have.\n"
                    "The flames sputter and fail to catch.\n"
                    "One of the zombies notices you struggling.\n"
                    "Before you can react, it pushes you into a corner and sets you on fire instead.\n"
                    "You scream as the flames engulf you.\n"
                    "GAME OVER."
                )
                print("(You will be returned to the start of the room.)")
                state.visited_rooms.remove("lab_2001")
                state = state_snapshot
                return state

        # Command handling using if/elif/else for compatibility
        if cmd == Command.help:
            display_help()
            continue
        if cmd == Command.look:
            if can_use_look:
                print(
                    "You wake up to strange noises in the university’s computer lab.\nThe last thing you remember is falling asleep during math class.\nThe lights flicker, tables are overturned and your classmates walk and moan around like zombies.\nYou don’t know what’s happening, but you don't want to stay to find out."
                )
                print(
                    "A few things go through your mind, but you decide to:\n"
                    "fly away\nsneak\nfight\nset building on fire"
                )
                can_choose_action = True
                continue
        if cmd == Command.answer:
            if can_choose_action:
                if not args:
                    display_invalid_syntax("answer")
                    continue
                action = " ".join(args)
                if action == "sneak":
                    # Already handled above
                    continue
                if action == "fly away":
                    print(
                        "You flap your arms desperately, hoping to take off like a bird.\n"
                        "The zombies glance at you with amusement as you wobble unsteadily.\n"
                        "You lift off for a split second... and crash straight into a desk.\n"
                        "Pain shoots through your body, and before you can recover, the zombies surround you.\n"
                        "Being human, flight was never an option. You have met a grim fate.\n"
                        "GAME OVER."
                    )
                elif action == "fight":
                    print(
                        "You try to fight one of your classmates.\n"
                        "They barely react and soon more zombies surround you.\n"
                        "You struggle, but you are only human.\n"
                        "The zombies overpower you.\n"
                        "GAME OVER."
                    )
                elif action == "set building on fire":
                    print(
                        "You try to set the building on fire with what you have.\n"
                        "The flames sputter and fail to catch.\n"
                        "One of the zombies notices you struggling.\n"
                        "Before you can react, it pushes you into a corner and sets you on fire instead.\n"
                        "You scream as the flames engulf you.\n"
                        "GAME OVER."
                    )
                print("(You will be returned to the start of the room.)")
                state.visited_rooms.remove("lab_2001")
                state = state_snapshot
                return state
        if cmd == Command.take:
            if len(pickable_items) > 0:
                if len(args) != 1:
                    display_invalid_syntax("take")
                    continue
                if args[0] == "?":
                    display_take_help()
                    continue
                if args[0] == "list":
                    display_take_list(pickable_items)
                    continue
                if args[0] in pickable_items and args[0] == "keycard":
                    print(
                        "Keycard in hand, you sneak past the zombies and swipe the lab door.\nIt opens.\nYou slip into the corridor and quickly close it behind you.\n"
                    )
                    state.inventory.append("keycard")
                    state.current_room = "east_corridor"
                    return state
                continue
        if cmd == Command.go:
            if len(args) != 1:
                display_invalid_syntax("go")
                continue
            if args[0] == "?":
                display_go_help()
                continue
            if args[0] == "list":
                display_go_list(["east_corridor"])
                continue
            if args[0] == "east_corridor":
                if "keycard" in state.inventory:
                    print(
                        "You quickly run out of the room and barricade the door behind you."
                    )
                    state.current_room = "east_corridor"
                    return state
                else:
                    print("You carefully sneak past the zombies...")
                    continue
        if cmd == Command.where:
            display_where_am_i(state)
            continue
        if cmd == Command.quit:
            quit_game()
        if cmd == Command.pause:
            pause_game(state)
        if cmd == Command.stats:
            display_stats(state)
            continue
        if cmd == Command.leaderboard:
            display_leaderboard()
            continue
        # If no command matched
        if cmd not in [Command.help, Command.look, Command.answer, Command.take, Command.go, Command.where, Command.quit, Command.pause, Command.stats, Command.leaderboard, "sneak"]:
            display_invalid_command()


if __name__ == "__main__":
    from datetime import timedelta as TimeDelta

    mock_state = State(
        player_name="mock",
        current_room="lab_2001",
        previous_room="",
        visited_rooms=[],
        time_played=TimeDelta(),
        inventory=[],
    )

    lab_2001(mock_state)
