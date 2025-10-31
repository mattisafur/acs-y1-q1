from copy import deepcopy
import time
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
    display_items_list,
    display_leaderboard,
    display_stats,
    display_where_am_i,
    display_map,
    get_user_input,
    pause_game,
    quit_game,
)

def north_corridor(state: State):
    state_snapshot = deepcopy(state)

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

        can_choose_action = True

    elif "north_corridor_boss_defeated" not in state.visited_rooms:
        print("As you go in direction of North Corridor, you notice a creature in front of it.\n"
              "He is gigantic and will not let you pass by.\n")
        time.sleep(1)

        print("It is.. your old math teacher.\n"
              "He is also one of them now. He is a zombie math teacher...\n")
        time.sleep(1)

        print("The most ugly one.\n"
              "You must do something to go further.\n\n")
        time.sleep(1)

        print("You feel the cold steel of the knife you picked up in Lab 2003 in your pocket.\n"
              "The zombie takes a lumbering step forward, drool pooling at its feet.\n")
        time.sleep(1)

        print("You’re ready.\n\n"
              "Choose how you’ll attack your math teacher:\n")
        time.sleep(1)

        print(
            "1. Go for a tough, direct strike to the head.       |     2. Throw the knife at the zombie.      |     3. Sneak up and attack."
        )

        can_choose_action = True
    else:
        can_choose_action = False

    while True:
        cmd, *args = get_user_input()
        cmd = cmd.lower() if cmd else ""
        args = [a.lower() for a in args]
        full_input = " ".join([cmd, *args]).strip().lower()

        match cmd:
            case Command.help:
                display_help()
                continue
            case Command.inventory:
                display_inventory(state)
                continue
            case Command.where:
                display_where_am_i(state)
                continue
            case Command.quit:
                quit_game()
            case Command.pause:
                pause_game(state)
            case Command.stats:
                display_stats(state)
                continue
            case Command.leaderboard:
                display_leaderboard()
                continue
            case Command.items:
                display_items_list()
                continue
            case Command.map:
                display_map()
                continue
            case Command.go:
                if len(args) != 1:
                    display_invalid_syntax("go")
                    continue
                destination = args[0]
                match destination:
                    case "?":
                        display_go_help()
                        continue
                    case "list":
                        display_go_list([
                            "lobby",
                            "front_desk_office",
                            "equinox_students_society",
                            "storage_room",
                            "project_room_3",
                            "teacher_room_3",
                            "teachers_room_2",
                            "teachers_room_1",
                            "west_corridor",
                        ])
                        continue
                    case "lobby":
                        if "north_corridor_boss_defeated" in state.visited_rooms:
                            print(
                                "\nYou try to leave the north corridor, but the enormous corpse of your zombie math teacher lies sprawled across the path.\n"
                                "Its twisted limbs block the entire passage, and the smell of decaying chalk makes your eyes water.\n"
                                "It is not possible to leave the corridor.\n"
                                "Explore corridor further with 'look' command"
                            )
                            continue
                        state.current_room = "lobby"
                        return state
                    case "front_desk_office":
                        state.current_room = "front_desk_office"
                        print("\nYou walk toward Front Desk office.")
                        return state
                    case "storage_room":
                        state.current_room = "storage_room"
                        print("\nYou move quietly toward the storage room, the air heavy with leftover tension.")
                        return state
                    case "project_room_3":
                        print("The door is locked")
                        continue
                    case "west_corridor":
                        state.current_room = "west_corridor"
                        return state
                    case "teacher_room_3":
                        state.current_room = "teacher_room_3"
                        return state
                    case "teachers_room_2" | "teachers_room_1":
                        print("The door is locked")
                        continue
                    case "equinox_students_society":
                        print("You slowly turn the handle of the Equinox Students Society door...\n"
                              "It barely moves—something’s blocking it from the inside.\n"
                              "You push harder and hear a loud *CLANG!* A pile of chairs, tables, and vending machines are stacked up like a fortress.\n")
                        time.sleep(1.5)

                        print("From behind the barricade, you hear frantic whispers—\n"
                              '"Who’s there?!"\n'
                              '"Go away! We’re not opening the door!"\n')
                        time.sleep(1.5)

                        print('"Last time someone knocked, it wasn’t human!"\n'
                              "You realize they’re other students—alive—but clearly not taking visitors.\n"
                              'A nervous laugh escapes you as someone shouts: "Try the cafeteria if you want snacks, we’re out!"\n')
                        time.sleep(1.5)

                        print("You decide it’s best not to argue with a barricade and quietly close the door.\n"
                              "Time to check another room...\n")
                        continue
                    case _:
                        display_invalid_command()
                        continue

        if can_choose_action:
            if "lab_2003" not in state.visited_rooms:
                match full_input:
                    case "1" | "forward" | "face":
                        answer = input("\nYour answer: ").strip()
                        if answer == "7":
                            subchoice = input("> ").strip().lower()
                            match subchoice:
                                case "1" | "stab" | "chalk":
                                    print(
                                        "\nYou grab the chalk and jab it into his chest — it snaps instantly.\n"
                                        "He stares down, offended. 'Detention!' he bellows, flinging you across the hallway.\n"
                                        "You crash into the lobby door, dazed but alive.\n"
                                        "You realize that you can't talk to a zombie, you must fight it.\n"
                                        "Maybe there's a weapon you can use in a room in lobby."
                                    )
                                    state.visited_rooms.append("north_corridor")
                                    state.current_room = "lobby"
                                    return state
                                case "2" | "kick" | "run":
                                    print(
                                        "\nYou give the zombie a solid kick and sprint back.\n"
                                        "He loses balance for a second but then roars: 'NO RUNNING IN THE HALLS!'\n"
                                        "A telekinetic force blasts you through the lobby doors."
                                        "You realize that you can't talk to a zombie, you must fight it.\n"
                                        "Maybe there's a weapon you can use in a room"
                                    )
                                    state.visited_rooms.append("north_corridor")
                                    state.current_room = "lobby"
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
                                        "You realize that you can't talk to a zombie, you must fight it.\n"
                                        "Maybe there's a weapon you can use in a room"
                                    )
                                    state.visited_rooms.append("north_corridor")
                                    state.current_room = "lobby"
                                    return state
                        else:
                            print(
                                "\nThe zombie growls: 'WRONG!'\n"
                                "He raises his arms, and glowing equations swirl around you like chains.\n"
                                "‘Repeat the class… in the afterlife.’\n"
                                "He throws you very far away.\n"
                                "Happily, you feel against one of the couches on the lobby, so you survive"
                                "You realize that you can't talk to a zombie, you must fight it.\n"
                                "Maybe there's a weapon you can use in a room"
                            )
                            state.current_room = "lobby"
                            return state
                    case "2" | "explore" | "around":
                        print(
                            "\nYou back away slowly, heart pounding.\n"
                            "The zombie tilts its head as it watches you go but doesn’t follow.\n"
                            "You slip back into the lobby, determined to find something that can help you."
                            "You realize that you can't talk to a zombie, you must fight it.\n"
                            "Maybe there's a weapon you can use in a room"
                        )
                        state.current_room = "lobby"
                        return state
                    case _:
                        display_invalid_command()
                        continue
            else:
                attack_choice = input("> ").strip().lower()
                match attack_choice:
                    case "1" | "head" | "strike" | "go for a tough, direct strike to the head":
                        print("\nYou grip the knife tightly, waiting for the perfect moment.\n")
                        time.sleep(1)
                        print("As your teacher lunges, you sidestep and drive the blade straight into his skull.\n")
                        time.sleep(1)
                        print("The creature collapses. You survived. The path ahead is clear.\n"
                              "Explore corridor further with 'look' command")
                        time.sleep(1)
                    case "2" | "throw" | "Throw the knife at the zombie.":
                        print(
                            "\nYou throw the knife — perfect shot! It lands in the zombie’s forehead.\n"
                            "Your teacher freezes mid-growl, then crashes to the ground. You walk forward.\n"
                            "Explore corridor further with 'look' command"
                        )
                    case "3" | "sneak" | "Sneak up and attack":
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
                                print("You leap onto its back and stab down. It collapses. Victory!\n"
                                      "Explore corridor further with 'look' command")
                            case "b":
                                print("You cut its tendons and finish it. The monster falls.\n"
                                      "Explore corridor further with 'look' command")
                            case "c":
                                print("You blind it with a strike to the eyes. It collapses.\n"
                                      "Explore corridor further with 'look' command")
                            case _:
                                print("You panic-stab. Somehow, it works. Luck favors the desperate.\n"
                                      "Explore corridor further with 'look' command")
                state.visited_rooms.append("north_corridor_boss_defeated")
                state.current_room = "north_corridor"
                can_choose_action = False
                continue

        if not can_choose_action:
            print("You are in the north corridor. Choose where you would like to go:")
            display_go_list([
                "lobby",
                "front_desk_office",
                "equinox_students_society",
                "storage_room",
                "project_room_3",
                "teacher_room_3",
                "teachers_room_2",
                "teachers_room_1",
                "west_corridor",
            ])

    return state
if __name__ == "__main__":
    test_state = State(
        player_name="TestPlayer",
        current_room="north_corridor",
        previous_room="lobby",
        visited_rooms=[],
        time_played=TimeDelta(),
        inventory=[],
        session_start_time=datetime.now(),
    )
    north_corridor(test_state)