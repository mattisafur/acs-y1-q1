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

    if "project_room_1" not in state.visited_rooms:
        print(
            "Apparently, you are not ready to come into this room.\n"
            "Go explore the rooms in the lobby and come back here."
        )
        state.current_room = "east_corridor"
        return state
    elif "lab_2003" in state.visited_rooms and "lab_2003_affirmations" not in state.visited_rooms:
        print(
            "You forgot the door opened last time you were here.\n"
            "The zombies got in and are throwing a party.\n"
            "No humans are invited.\n"
            "Too bad....\n"
            "CHOOSE ANOTHER ROOM!!!"
        )
        state.current_room = "east_corridor"
        return state
    elif "lab_2003" not in state.visited_rooms:
        state.visited_rooms.append("lab_2003")
        print("You are in the Computer lab 2.003.")
    else:
        print("You are in the Computer lab 2.003 again. The computer is still on.")

    print(
        "Possible commands:\n"
        "Look\n"
        "Take\n"
        "Quit"
    )

    can_use_look = True
    can_choose_action = True
    pickable_items: list[str] = []
    attempts = 0
    max_attempts = 3

    while True:
        cmd, *args = get_user_input()

        match cmd:
            case Command.help:
                raise NotImplementedError

            case Command.look:
                if can_use_look:
                    print(
                        "There is just one computer on. On the screen it displays:\n"
                        "“Login required – Insert authorized password.”\n"
                        "You must insert something.\n"
                    )
                    print(
                        "Type code from Project room\n"
                        "Write a goodbye letter\n"
                        "Type your mom's number\n"
                        "Write positive affirmations"
                    )
                    can_choose_action = True

            case Command.answer:
                if can_choose_action:
                    if not args:
                        print("Invalid syntax! You need to provide an answer.")
                        continue
                    choice = " ".join(args)

                    if choice == "Type code from Project room":
                        print("You carefully type in\n")
                        while attempts < max_attempts:
                            code = input("  ")
                            if code == "72946":
                                print(
                                    "After a short pause, the screen unlocks. The computer has a document opened.\n"
                                    "One line sparks your attention:\n"
                                    "'Tools can be found at the top left of the cabinet'\n"
                                    "You start to look for it, and find a knife.\n"
                                    "\nTo pick up the knife, you should use the command 'take knife'"
                                )
                                pickable_items.append("knife")
                                can_use_look = False
                                break
                            else:
                                attempts += 1
                                if attempts < max_attempts:
                                    print(
                                        f"Computer displays: 'Incorrect password! You have {max_attempts - attempts} chances left.'\n"
                                    )
                                else:
                                    print("You failed 3 times. Room will restart.")
                                    state = deepcopy(state_snapshot)
                                    state.current_room = "lab_2003"
                                    return state

                    elif choice == "Write a goodbye letter":
                        print(
                            "Your hands are shaking, you breathe roughly, sweat covers your face.\n"
                            "You decide to save your last words on the school's computer.\n"
                        )
                        last_words = input("  ")
                        print(
                            "\nYou leave the room desperate and anxious.\n"
                            "You bite a zombie from behind.\n"
                            "The zombie bites you back.\n"
                            "You bleed to death in the East Corridor.\n"
                            f"{last_words} — you may rest in peace.\n"
                            "Room will be restarted"
                        )
                        state = deepcopy(state_snapshot)
                        return state

                    elif choice == "Type your mom's number":
                        print("As an instinct, you decide to type your mom's number:")
                        mom_number = input("  ")
                        print(
                            "\nThe screen displays 'Incorrect password' and you cry a lot.\n"
                            "You drink something from a glass — it was the zombie potion.\n"
                            "You are now one of them. It is not allowed to become a zombie.\n"
                            "Room will be restarted"
                        )
                        state = deepcopy(state_snapshot)
                        return state

                    elif choice == "Write positive affirmations":
                        print(
                            "You write some positive affirmations.\n"
                            "Things don't get better, but at least you're leaving laboratory 2.003 optimistic now."
                        )
                        if "lab_2003_affirmations" not in state.visited_rooms:
                            state.visited_rooms.append("lab_2003_affirmations")
                        state.current_room = "east_corridor"
                        return state

                    else:
                        print("Invalid choice.")

            case Command.take:
                if len(pickable_items) > 0:
                    if len(args) != 1:
                        display_invalid_syntax("take")
                        continue
                    match args[0]:
                        case "?":
                            display_take_help()
                        case "list":
                            display_take_list(pickable_items)
                        case "knife":
                            print("You picked up the knife and head back to East Corridor")
                            state.inventory.append("knife")
                            state.current_room = "east_corridor"
                            return state
                        case _:
                            print("You can't take that.")

            case Command.go:
                if len(args) != 1:
                    display_invalid_syntax("go")
                    continue
                match args[0]:
                    case "?":
                        display_go_help()
                    case "list":
                        display_take_list(pickable_items)

            case Command.quit:
                quit_game()

            case Command.pause:
                pause_game(state)

            case Command.stats:
                display_stats()

            case Command.leaderboard:
                display_leaderboard()

    return state


if __name__ == "__main__":
    test_state = State(
        player_name="TestPlayer",
        current_room="lab_2003",
        previous_room="",
        visited_rooms=[],
        time_played=TimeDelta(),
        inventory=[],
    )
    lab_2003(test_state)
