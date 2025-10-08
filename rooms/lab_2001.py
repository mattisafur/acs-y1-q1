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


def lab_2001(state: State):
    state_snapshot = deepcopy(state)

    if "lab_2001" not in state.visited_rooms:
        # set room as visited
        state.visited_rooms.append("lab_2001")
    else:
        # print that you don't want to be in this room and return to the previous room
        print("There is a zombie inside this room, you don't want to go in.")
        state.current_room = state.previous_room
        return

    # prologue. will only show up once as re-entering the room is not possible
    print(
        "A loud bang can be heard and a door opens. You wake up suddenly and slowly remember where you are, the University. You were in class falling asleep when you woke up and no one was around you, well that's not true. There is a zombie coming into this room. Reacting fast you hide behind some of the tables. There must have been a zombie outbreak. You theorize that maybe the biology students have accidentally created a virus. However it is not the time to ponder the origin of the zombie. You have to get out of this room and also grab the keycard to open the door in the corridor."
    )

    can_use_look = True
    can_choose_action = False
    pickable_items: list[str] = []

    while True:
        # split the user input to the command (string) and the arguments (list of strings)
        cmd, *args = get_user_input()

        match cmd:
            case Commands.help:
                raise NotImplementedError
            case Commands.look:
                if can_use_look:
                    print(
                        "The lights flicker on and off, making strange shadows on the walls. Tables are overturned, and zombies shuffle between them, their groans filling in the silence. On a nearby desk, you spot a Keycard that could unlock electronic doors in the corridor. The zombies are too close for comfort, though. You'll have to be careful if you want to grab it without being noticed."
                    )
            case Commands.answer:
                if can_choose_action:
                    if len(args) != 1:
                        display_answer_invalid_syntax()

                    match args[0]:
                        case "sneak":
                            # TODO print missing text from flowchart
                            print("You notice a keycard on one of the desks")
                            pickable_items.append("keycard")
                            continue
                        case "fly away":
                            print("You have no wings, so the zombies get you")
                        case "fight":
                            print(
                                "You set the building on fire, but you can’t escape. Zombies vanish, but you die."
                            )
                        case "set building on fire":
                            print(
                                "The zombies are stronger than you are, you get bitten. Game over."
                            )

                    print("(You will be returned to the start of the room)")
                    state = state_snapshot
                    return
            case Commands.take:
                if len(pickable_items) > 0:
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

                    if args[0] in pickable_items and args[0] == "keycard":
                        print(
                            "You picked up the keycard You want to get out of this room to the east corridor as quickly as possible"
                        )
                        state.inventory.append("keycard")
            case Commands.go:
                if len(args) != 1:
                    display_go_invalid_syntax()
                    continue

                match args[0]:
                    case "?":
                        display_go_help()
                        continue
                    case "list":
                        display_go_list(["east_corridor"])
                        continue
                    case "east_corridor":
                        if "keycard" in state.inventory:
                            print(
                                "You quickly run out of the room and barricade the door behind you"
                            )
                            state.current_room = "east_corridor"
                            return
                        else:
                            print("You carefully sneak past the zombies...")
            case Commands.quit:
                quit_game()
            case Commands.pause:
                pause_game(state)
            case Commands.stats:
                display_stats()
            case Commands.leaderboard:
                display_leaderboard()

        display_invalid_command()
