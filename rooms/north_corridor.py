import time

from models import Command, State
from util import (
    display_go_help,
    display_where_am_i,
    display_go_list,
    display_invalid_command,
    display_invalid_syntax,
    display_inventory,
    display_leaderboard,
    display_stats,
    get_user_input,
    pause_game,
    quit_game,
    display_help,
)


def north_corridor(state: State):
    if "lab_2003" not in state.visited_rooms:
        print(
            "\nThe air grows colder as you enter the North Corridor.\n"
            "A deep, echoing growl shakes the floor beneath your feet.\n"
            "From the darkness ahead, a massive figure emerges...\n"
            "You recognize the shadow of the figure ahead of you. It’s your old math teacher.\n"
            "He turns in your direction and you notice his body swollen and rotten, his eyes glowing faintly green.\n"
            "He is unhappy. He knows you've been sleeping in class.\n\n"
            "The way forward is blocked.\n\n"
            "You have two options:\n"
            "1. Go forward and try to face the zombie.\n"
            "2. Explore the rooms around the lobby and east corridor first.\n"
        )

        choice = input("> ").strip().lower()

        match choice:
            case "1" | "forward" | "face":
                print(
                    "\nYou take a deep breath and rush ahead.\n"
                    "The creature lets out a thunderous roar that shakes the floor.\n"
                    "Then suddenly... it speaks.\n"
                    "'You dare interrupt my eternal equation?' the zombie teacher growls, chalk dust puffing from his rotting hands.\n"
                    "He points at the wall behind him, where glowing numbers appear:\n"
                    "  (12 × ?) – 24 = 60\n"
                    "His decaying lips twist into a grin. 'Solve it... or stay for detention. Forever.'"
                )
                answer = input("\nYour answer: ").strip()

                if answer == "7":
                    print(
                        "\nThe zombie groans, almost impressed. 'Correct...' he says, drooling algebra symbols.\n"
                        "He lowers his guard slightly. You edge closer, heart racing.\n\n"
                        "You’re close enough to act! What do you do?\n"
                        "1. Try to snatch the chalk and stab him with it.\n"
                        "2. Kick him and run.\n"
                        "3. Attempt to correct his math and assert dominance."
                    )
                    subchoice = input("> ").strip().lower()

                    match subchoice:
                        case "1" | "stab" | "chalk":
                            print(
                                "\nYou grab the chalk and jab it into his chest — it snaps instantly.\n"
                                "He stares down, offended. 'Detention!' he bellows, flinging you across the hallway.\n"
                                "You crash into the lobby door, dazed but alive."
                            )
                            state.visited_rooms.append("north_corridor")
                            state.current_room = "north_corridor"
                            return state

                        case "2" | "kick" | "run":
                            print(
                                "\nYou give the zombie a solid kick and sprint back.\n"
                                "He loses balance for a second but then roars: 'NO RUNNING IN THE HALLS!'\n"
                                "A telekinetic force blasts you through the lobby doors."
                            )
                            state.visited_rooms.append("north_corridor")
                            state.current_room = "north_corridor"
                            return state

                        case "3" | "correct" | "math":
                            print(
                                "\nYou puff your chest and declare, 'Actually, the equation is trivial. It is basic algebra, really.'\n"
                                "The zombie tilts his head, insulted.\n"
                                "'Then you can solve THIS!' he snarls, scribbling π × 0 on the wall — before smacking you with the chalkboard.\n"
                                "You died."
                            )
                            state.current_room = "north_corridor"

                        case _:
                            print(
                                "\nYou hesitate, and the zombie’s patience runs out.\n"
                                "‘Pop quiz over,’ he growls, before tossing you back toward the lobby."
                            )
                            state.visited_rooms.append("north_corridor")
                            state.current_room = "north_corridor"
                            return state

                else:
                    print(
                        "\nThe zombie growls: 'WRONG!'\n"
                        "He raises his arms, and glowing equations swirl around you like chains.\n"
                        "‘Repeat the class… in the afterlife.’\n"
                        "He throws you very far away.\n"
                        "Happily, you feel against one of the couches on the lobby, so you survive"
                    )
                    state.current_room = "lobby"
                    return state

            case "2" | "explore" | "around":
                print(
                    "\nYou back away slowly, heart pounding.\n"
                    "The zombie tilts its head as it watches you go but doesn’t follow.\n"
                    "You slip back into the lobby, determined to find something that can help you."
                )
                state.current_room = "lobby"
                return state


    elif "north_corridor_boss_defeated" not in state.visited_rooms:
        print(
            "As you go in direction of North Corridor, you notice a creature in front of it.\n"
            "He is gigantic and will not let you pass by.\n"
            "It is.. your old math teacher\n"
            "He is also one of them now. He is a zombie math teacher...\n"
            "The most ugly one.\n"
            "You must do something to go further.\n\n"
            "You feel the cold steel of the knife you picked up in Lab 2003 in your pocket.\n"
            "The zombie takes a lumbering step forward, drool pooling at its feet.\n"
            "You’re ready.\n\n"
            "Choose how you’ll attack your math teacher:\n"
            "1. Go for a tough, direct strike to the head.\n"
            "2. Throw the knife at the zombie.\n"
            "3. Sneak up and attack."
        )
        attack_choice = input("> ").strip().lower()

        match attack_choice:
            case "1" | "head" | "strike":
                print("\nYou grip the knife tightly, waiting for the perfect moment.\n")
                time.sleep(1)
                print("As your teacher lunges, you sidestep and drive the blade straight into his skull.\n")
                time.sleep(1)
                print("The creature collapses. You survived. The path ahead is clear.")
                time.sleep(1)

            case "2" | "throw":
                print(
                    "\nYou throw the knife — perfect shot! It lands in the zombie’s forehead.\n"
                    "Your teacher freezes mid-growl, then crashes to the ground. You walk forward."
                )

            case "3" | "sneak":
                print(
                    "\nYou decide brute force isn’t enough. You’ll have to be smart.\n"
                    "You wait for the zombie to roar, then dash between its legs, slashing as you move.\n"
                    "The knife cuts deep. Quick! Choose your next move:\n"
                    "a) Climb its back and stab from above.\n"
                    "b) Slide under its swing and slice its leg tendons.\n"
                    "c) Aim for the glowing eyes."
                )
                second_action = input("> ").strip().lower()

                match second_action:
                    case "a":
                        print("You leap onto its back and stab down. It collapses. Victory!")
                    case "b":
                        print("You cut its tendons and finish it. The monster falls.")
                    case "c":
                        print("You blind it with a strike to the eyes. It collapses.")
                    case _:
                        print("You panic-stab. Somehow, it works. Luck favors the desperate.")

        state.visited_rooms.append("north_corridor_boss_defeated")
        state.current_room = "north_corridor"

    print("You are in the north corridor. Choose where you would like to go:")
    available_rooms = [
        "lobby",
        "front_desk_office",
        "classroom_2_021",
        "classroom_2_015",
        "equinox_students_society",
        "storage_room",
        "project_room_3",
        "teachers_room_3",
        "teachers_room_2",
        "teachers_room_1",
        "west_corridor",
    ]
    display_go_list(available_rooms)

    command, *args = get_user_input()
    if command.lower() == "go" and len(args) == 1:
        destination = args[0].lower()

        match destination:
            case "lobby":
                print(
                    "\nYou try to leave the north corridor, but the enormous corpse of your zombie math teacher lies sprawled across the path.\n"
                    "Its twisted limbs block the entire passage, and the smell of decaying chalk makes your eyes water.\n"
                    "You’ll need another way around — or a strong stomach."
                )
                return state

            case "front_desk_office":
                state.current_room = "front_desk_office"
                print("\nYou walk carefully past the fallen teacher and make your way toward the Front Desk Office.")
            case "storage_room":
                state.current_room = "storage_room"
                print("\nYou move quietly toward the storage room, the air heavy with leftover tension.")
            case "west_corridor":
                state.current_room = "west_corridor"
                print("\nYou step over debris and head west, deeper into the dark corridors.")
            case "teachers_room_3":
                state.current_room = "teachers_room_3"
                print("\nYou push open the heavy door marked 'Teachers Room 3' and step inside cautiously.")

    elif command.lower() == "inventory":
        display_inventory(state)
    elif command.lower() == "where":
        display_where_am_i(state)
    elif command.lower() == "quit":
        quit_game()
    elif command.lower() == "pause":
        pause_game(state)
    elif command.lower() == "stats":
        display_stats(state)
    elif command.lower() == "leaderboard":
        display_leaderboard()
    elif command.lower() in ("help", "?"):
        display_help()
    else:
        display_invalid_command()

    return state
