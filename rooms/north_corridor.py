from models import Command, State
from util import (
    display_go_help,
    display_go_list,
    display_invalid_command,
    display_invalid_syntax,
    display_inventory,
    display_leaderboard,
    display_stats,
    get_user_input,
    pause_game,
    quit_game,
    display_help,  # adicionado
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
                            state.current_room = "lobby"
                            return state

                        case "2" | "kick" | "run":
                            print(
                                "\nYou give the zombie a solid kick and sprint back.\n"
                                "He loses balance for a second but then roars: 'NO RUNNING IN THE HALLS!'\n"
                                "A telekinetic force blasts you through the lobby doors."
                            )
                            state.current_room = "lobby"
                            return state

                        case "3" | "correct" | "math":
                            print(
                                "\nYou puff your chest and declare, 'Actually, the equation is trivial. It is basic algebra, really.'\n"
                                "The zombie tilts his head, insulted.\n"
                                "'Then you can solve THIS!' he snarls, scribbling π × 0 on the wall — before smacking you with the chalkboard.\n"
                                "You died."
                            )
                            quit_game()

                        case _:
                            print(
                                "\nYou hesitate, and the zombie’s patience runs out.\n"
                                "‘Pop quiz over,’ he growls, before tossing you back toward the lobby."
                            )
                            state.current_room = "lobby"
                            return state

                else:
                    print(
                        "\nThe zombie growls: 'WRONG!'\n"
                        "He raises his arms, and glowing equations swirl around you like chains.\n"
                        "‘Repeat the class… in the afterlife.’\n"
                        "You died."
                    )
                    quit_game()

            case "2" | "explore" | "around":
                print(
                    "\nYou back away slowly, heart pounding.\n"
                    "The zombie tilts its head as it watches you go but doesn’t follow.\n"
                    "You slip back into the lobby, determined to find something that can help you."
                )
                state.current_room = "lobby"
                return state

            case _:
                print(
                    "\nYou hesitate too long...\n"
                    "The zombie senses your fear and charges forward — too late to run.\n"
                    "You died."
                )
                quit_game()

    else:
        print(
            "As you go in direction of North Corridor, you notice a creature in front of it.\n"
            "He is gigantic and will not let you pass by.\n"
            "You must do something to go further.\n\n"
            "You feel the cold steel of the knife you picked up in Lab 2003 in your pocket.\n"
            "The zombie takes a lumbering step forward, drool pooling at its feet.\n"
            "This time, you’re ready.\n\n"
            "Choose how you’ll attack:\n"
            "1. Go for a tough, direct strike to the head.\n"
            "2. Throw the knife at the zombie.\n"
            "3. Sneak up and attack."
        )
        attack_choice = input("> ").strip().lower()

        match attack_choice:
            case "1" | "head" | "strike":
                print(
                    "\nYou grip the knife tightly, waiting for the perfect moment.\n"
                    "As the zombie lunges, you sidestep and drive the blade straight into its skull.\n"
                    "The creature collapses. You survived. The path ahead is clear."
                )
                state.visited_rooms.append("north_corridor")
                state.current_room = "north_corridor"

            case "2" | "throw":
                print(
                    "\nYou throw the knife — perfect shot! It lands in the zombie’s forehead.\n"
                    "The creature freezes mid-growl, then crashes to the ground. You walk forward."
                )
                state.visited_rooms.append("north_corridor")
                state.current_room = "north_corridor"

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
                state.visited_rooms.append("north_corridor")
                state.current_room = "north_corridor"

            case _:
                print("\nYou hesitate... The zombie doesn’t. You died.")
                quit_game()

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
    if command == Command.go and len(args) == 1:
        destination = args[0].lower()
        if destination in available_rooms:
            state.current_room = destination
        else:
            print("Invalid destination.")
    elif command == Command.inventory:
        display_inventory(state)
    elif command == Command.quit:
        quit_game()
    elif command == Command.pause:
        pause_game(state)
    elif command == Command.stats:
        display_stats(state)
    elif command == Command.leaderboard:
        display_leaderboard()
    elif command in ("help", "?"):
        display_help()
    else:
        display_invalid_command()

    return state
