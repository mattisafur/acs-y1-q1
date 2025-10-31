import time
from copy import deepcopy
from datetime import datetime
from datetime import timedelta as TimeDelta

from models import Command, State
from util import (
    display_go_help,
    display_go_list,
    display_help,
    display_invalid_command,
    display_invalid_syntax,
    display_inventory,
    display_leaderboard,
    display_stats,
    display_take_help,
    display_take_list,
    display_where_am_i,
    display_map,
    get_user_input,
    pause_game,
    quit_game,
    display_items_list
)


def lab_2003(state: State):
    state_snapshot = deepcopy(state)

    if "project_room_1" not in state.visited_rooms:
        print("You are not ready for this room. Explore lobby rooms first.")
        state.current_room = "east_corridor"
        return state

    if "lab_2003" in state.visited_rooms and "lab_2003_affirmations" not in state.visited_rooms:
        print(
            "You forgot the door opened last time you were here.\n"
            "The zombies got in and are throwing a party.\n"
            "No humans are invited.\n"
            "Too bad....\n"
            "At least you collected the knife already.\n"
        )
        state.current_room = "east_corridor"
        return state
    elif "lab_2003" in state.visited_rooms and "lab_2003_affirmations" in state.visited_rooms:
        print("You are back in Laboratory 2003.")
    elif "lab_2003" not in state.visited_rooms:
        state.visited_rooms.append("lab_2003")
        print("You are in the Computer lab 2.003.")

    print("Use command look to explore the room.")

    can_use_look = True
    can_choose_action = True
    pickable_items: list[str] = []
    attempts = 0
    max_attempts = 3

    while True:
        cmd, *args = get_user_input()
        cmd = cmd.lower()
        args = [a.lower() for a in args]
        full_input = " ".join([cmd, *args]).strip().lower()

        match cmd:
            case "help":
                display_help()

            case "look":
                if can_use_look:
                    print(
                        "There is just one computer on. On the screen it displays:\n"
                        "“Login required – Insert authorized password.”\n"
                        "You must unlock it.\n"
                        "Possible commands:\n"
                        "1.Type code from Project room\n"
                        "2.Write a goodbye letter\n"
                        "3.Type your mom's number\n"
                        "4.Write positive affirmations"
                    )
                    can_choose_action = True

            case "take":
                if len(pickable_items) > 0:
                    if len(args) != 1:
                        display_invalid_syntax("take")
                        continue
                    arg = args[0].lower()
                    match arg:
                        case "?":
                            display_take_help()
                        case "list":
                            display_take_list(pickable_items)
                        case "knife":
                            print("You picked up the knife and head back to East Corridor")
                            time.sleep(1.5)
                            state.inventory.append("knife")
                            state.current_room = "east_corridor"
                            return state
                        case _:
                            print("You can't take that.")

            case "go":
                if len(args) != 1:
                    display_invalid_syntax("go")
                    continue
                arg = args[0].lower()
                match arg:
                    case "?":
                        display_go_help()
                    case "list":
                        display_go_list(pickable_items)

            case "quit":
                quit_game()

            case "pause":
                pause_game(state)

            case "map":
                display_map()
                continue

            case "inventory":
                display_inventory(state)
                continue

            case "items":
                display_items_list()
                continue

            case "where":
                display_where_am_i(state)
                continue

            case "stats":
                display_stats(state)
                continue

            case "leaderboard":
                display_leaderboard()
                continue

            case _:
                if can_choose_action:
                    full_input = " ".join([cmd, *args]).strip().lower()
                    choice = full_input

                    choice = full_input.lower()

                    if choice == "1":
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

                    elif choice == "2":
                        print(
                            "Your hands are shaking, you breathe roughly, sweat covers your face.\n"
                            "You decide to save your last words on the school's computer.\n"
                        )
                        last_words = input("  ")
                        print(
                            "\nAs you finish typing your letter, computer displays:\n"
                            "Incorrect password. Try again.\n"
                            "You get desperation, you don't know what to do anymore.\n"
                            f"Freaking out, you leave the room desperate and anxious.\n"
                            "You see one of those creatures from behind, so you just bite his neck.\n"
                            "You don't know why you did that, just felt like it...\n"
                        )
                        time.sleep(1.5)
                        print(
                            "The zombie bites you back.\n"
                            "Your arm starts to swallow, so much blood is coming out of it"
                            "You bleed to death in the East Corridor.\n"
                            f"{last_words} — you may rest in peace.\n"
                            "Room will be restarted"
                        )
                        state = deepcopy(state_snapshot)
                        return state

                    elif choice == "3":
                        print("As an instinct, you decide to type your mom's number:")
                        mom_number = input("  ")
                        print(
                            "\nThe screen displays 'Incorrect password' and you cry a lot.\n"
                            "You cried so, so, so much that now you feel dehydrated.\n"
                            "You spot a glass in one of the tables.\n"
                            "You are so, so, so thirsty that you drink it.\n"
                            "You start to smell something bad, and you realize you are stinking.\n"
                            "'How is that possible....' you think to yourself. 'I know I used deodorant this morning!!'\n"
                            "You look at your hands, and then you understand: you are rotting.\n"
                            "You drank a potion that turned all your classmates in zombies.\n"
                        )
                        time.sleep(1.5)
                        print(
                            "You are now one of them. It is not allowed to become a zombie.\n"
                            "You are D-E-A-D. \n"
                            "Room will be restarted :)"
                        )
                        state = deepcopy(state_snapshot)
                        return state

                    elif choice == "4":
                        print(
                            "You write some positive affirmations.\n"
                            "Things don't get better, but at least you're leaving laboratory 2.003 optimistic now."
                        )
                        time.sleep(1)
                        if "lab_2003_affirmations" not in state.visited_rooms:
                            state.visited_rooms.append("lab_2003_affirmations")
                        state.current_room = "east_corridor"
                        return state

                    else:
                        print("Invalid choice.")


if __name__ == "__main__":
    test_state = State(
        player_name="TestPlayer",
        current_room="lab_2003",
        previous_room="",
        visited_rooms=[],
        time_played=TimeDelta(),
        inventory=[],
        session_start_time=datetime.now(),
    )
    lab_2003(test_state)
