from copy import deepcopy

from models import Command, State
from rooms.east_corridor import east_corridor
from util import (
    display_go_help,
    display_go_list,
    display_invalid_command,
    display_invalid_syntax,
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
        state.current_room = "east_corridor"
        return
    print(
        "You step into the room\n"
        "Possible commands:\n"
        "Look\n"
        "Take\n"
        "Go to East Corridor\n"
        "Quit" )
    # prologue. will only show up once as re-entering the room is not possible

    can_use_look = True
    can_choose_action = False
    pickable_items: list[str] = []

    while True:
        # split the user input to the command (string) and the arguments (list of strings)
        cmd, *args = get_user_input()

        # match on the command (e.g. take)
        match cmd:
            case Command.help:
                # the help command is not implemented yet so we raising "not implemented" error
                raise NotImplementedError
            case Command.look:
                # only let the user run the look command if the look command is allowed to be run, if not the command will be skipped so the code will print "invalid command"
                if can_use_look:
                    print(
                        "You wake up to strange noises in the university’s computer lab.\nThe last thing you remember is falling asleep during math class.\nThe lights flicker, tables are overturned and your classmates walk and moan around like zombies.\nYou don’t know what’s happening, but you don't want to stay to find out."
                    )
                    print(
                        "A few things go through your mind, but you decide to:\n"
                        "fly away\nsneak\nfight\nset building on fire"
                    )  # TODO enter the correct text here, missing from flowchart
                    can_choose_action = True
                    continue
            case Command.answer:
                # only let the user run the answer command if if they have a challenge they need to answer, if not the command will be skipped so the code will print "invalid command"
                if can_choose_action:
                    # if no arguments are given, print "invalid syntax"
                    if not args:
                        display_invalid_syntax("answer")
                        continue  # skip the "invalid command" functon call at end of loop

                    # when matching, join all the arguments together to reconstruct the player's answer (for exmample ["fly", "away"] will become "fly away")
                    match " ".join(args):
                        case "sneak":
                            print("You notice a keycard on one of the desks.\nYou imagine is from the door of the laboratory.\nSo you decided to take it\n\n"
                            "To pick up the keycard, you should use the command 'take keycard'")
                            pickable_items.append(
                                "keycard"
                            )  # make keycard possible to pick up by adding it to the list of items we can pick up in the room
                            can_use_look = False  # make "look" no longer available
                            continue  # skip the "invalid command" functon call at end of loop

                        # all cases under here result in death, we only print the text that's not the same between the commands here, and under the match statement we reset the room because we want it to happen in all of these cases
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

                    print("(You will be returned to the start of the room.)")
                    state.visited_rooms.remove("lab_2001")  # HACK fix the issue of not letting user back in after dying
                    state = state_snapshot  # reset the game state
                    return
            case Command.take:
                # if there are no items you can pick up, skip the commands logic and continue with the code so it will print "invalid command"
                if len(pickable_items) > 0:
                    # make sure only one argument was passed to the command
                    if len(args) != 1:
                        display_invalid_syntax("take")
                        continue  # skip the "invalid command" functon call at end of loop

                    # match on the first argument, which is also the only argument because of the check we did above
                    match args[0]:
                        case "?":
                            display_take_help()
                            continue  # skip the "invalid command" functon call at end of loop
                        case "list":
                            display_take_list(pickable_items)
                            continue  # skip the "invalid command" functon call at end of loop

                    # check if the item the user entered is in the list of possible items to pick up AND that this item the user entered is the keycard
                    # checking both of these is pretty redundant because there is only one item in this room but I am checking both just so it will be easier to understand
                    if args[0] in pickable_items and args[0] == "keycard":
                        print(
                            "Keycard in hand, you sneak past the zombies and swipe the lab door.\n It opens.\n You slip into the corridor and quickly close it behind you.\n")
                        state.inventory.append(
                            "keycard"
                        )  # add the keycard to the inventory
                        state.current_room = "east_corridor"
                        return

                    continue
            case Command.go:
                # make sure only one argument was passed to the command
                if len(args) != 1:
                    display_invalid_syntax("go")
                    continue  # skip the "invalid command" functon call at end of loop

                # match on the first argument, which is also the only argument because of the check we did above
                match args[0]:
                    case "?":
                        display_go_help()
                        continue  # skip the "invalid command" functon call at end of loop
                    case "list":
                        display_go_list(["east_corridor"])
                        continue  # skip the "invalid command" functon call at end of loop
                    case "east_corridor":
                        # if player has the keycard, let them exit the room, if not, print something and stay in the room
                        if "keycard" in state.inventory:
                            print(
                                "You quickly run out of the room and barricade the door behind you."
                            )
                            state.current_room = "east_corridor"
                            return
                        else:
                            print("You carefully sneak past the zombies...")
                            continue

            case Command.quit:
                # function will quit the game, no need to add continue
                quit_game()
            case Command.pause:
                # function will pause the game
                pause_game(state)
            case Command.stats:
                display_stats()
                continue  # skip the "invalid command" functon call at end of loop
            case Command.leaderboard:
                display_leaderboard()
                continue  # skip the "invalid command" functon call at end of loop

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