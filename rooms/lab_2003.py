from copy import deepcopy
from datetime import timedelta as TimeDelta

from models import Command, State
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


def lab_2003(state: State):
    state_snapshot = deepcopy(state)

    if "lab_2003" not in state.visited_rooms:
        state.visited_rooms.append("lab_2003")
    else:
        print("You forgot the door opened last time you were here.\n"
              "The zombies got in and are throwing a party.\n"
              "No humans are invited.\n"
              "Too bad....\n"
              "CHOOSE ANOTHER ROOM!!!")
        state.current_room = state.previous_room
        return

    print("You are in the Computer lab 2.003.")

can_use_look = True
can_choose_action = False
pickable_items: list[str] = []

while True:
    cmd, *args = get_user_input()

    match cmd:
        case Command.help:
        # the help command is not implemented yet so we raising "not implemented" error
            raise NotImplementedError
        case Command.look:
            if can_use_look:
                print("There is just one computer on. On the screen it displays:\n"
                      "“Login required – Insert authorized password.\n”"
                      "You must insert something. \n")
                print(
                    "Type code from Project room\n"
                    "Write a goodbye letter\n"
                    "Type your mom's number\n"
                    "Write positive affirmations"
                )
        case Command.answer:
            if can_choose_action:
                if not args:
                    display_invalid_syntax("answer")
                    continue
                match " ".join(args):
                    case "Type code from Project room":
                        print("You carefully type in\n")
                        code = input("  ")
                        if code == "72946":
                            print(
                                "After a short pause, the screen unlocks. The computer has a document opened.\n"
                                "One line sparks your attention:\n"
                                "'Tools can be found at the top left of the cabinet'\n"
                                "You start to look for it, and find a knife" )
                            pickable_items.append(
                                "knife"
                            )
                            can_use_look = False
                            state.current_room = "east_corridor"
                            continue
                        else:
                            print("Computer displays: 'Incorrect password!'\n")
                            state.current_room = "lab_2003"
                    case "Goodbye letter":
                        print(
                            "Your hands are shaking, you breath roughly you feel sweat over your face.\n"
                            "You are so afraid of the zombies, that you decide to save your last words on earth in the school's computer.\n"
                        )
                        last_words = input("  ")
                        print (
                            "You leave the room desperate and anxious, and without thinking, decides to bite up a zombie from behind\n"
                            "The zombie bites you back, and you bleed to death in East Corridor\n"
                            f"{last_words} you may rest in peace"
                        )
                    #return?
                    case "Type mom's number":
                        print(
                            "As a instinct, you decide to type your mom's number:"
                        )
                        mom_number = input("  ")
                        print(
                            "The screen displays 'Incorrect password' and you cry a lot.\n"
                            "You start to feel thirsty from so many water you lost on your tears, so you start to look for something to drink\n"
                            "You spot a glass on the table and decide to drink it.\n"
                            "It is not water.\n"
                            "\n Oopss.... \n"
                            "It is the potion that transformed all the students in zombies.\n"
                            "Now, you are one of them.\n\n"
                            "It is not allowed to become a zombie.")
                    case "Positive affirmations":
                        print(
                            "Not thinking the computer would be useful, you start to write positive affirmations as a manifestation to the universe.\n"
                            "You believe this way, things will get better.\n"
                            "Things don't get better, so you just leave the room, but now with a optimistic mindset."
                        )
                        state.current_room = "east_corridor"
                    case _:
                        print("Invalid choice.")
        case Command.take:
            if len(pickable_items) > 0:
                if len(args) != 1:
                    display_invalid_syntax("go")
                    continue
                match args[0]:
                    case "?":
                        display_take_help()
                        continue
                    case "list":
                        display_take_list(pickable_items)
                        continue
                if args[0] in pickable_items and args[0] == "Knive":
                    print(
                        "You picked up a knive You want to get out of this room to the east corridor as quickly as possible"
                    )
                    state.inventory.append(
                        "Knive"
                    )
        case Command.go:
            if len(args) != 1:
                display_invalid_syntax("go")
                continue
            match args[0]:
                case "?":
                    display_go_help()
                    continue
                case "list":
                    display_go_list(["east_corridor"])
                    continue
                case "east_corridor":
                    if "knife" in state.inventory:
                        print(
                            "You hide the knife and runs quickly out of the room"
                        )
                        state.current_room = "east_corridor"
                    else:
                        print("You go back to East Corridor precautiously..")
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
# Create test state
    test_state = State(
        player_name="TestPlayer",
        current_room="lab_2003",
        previous_room="",
        visited_rooms=[],
        time_played=TimeDelta(),
        inventory=[],
    )

    lab_2003(test_state)
# PLEASE MAKE IT RUN :(((((((((