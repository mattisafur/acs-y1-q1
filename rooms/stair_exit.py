from datetime import timedelta as TimeDelta
from models import Command, State
from util import (
    display_invalid_syntax,
    display_go_help,
    display_go_list,
    display_invalid_command,
    display_leaderboard,
    display_stats,
    display_take_help,
    display_take_list,
    get_user_input,
    pause_game,
    quit_game,
    display_help,
)

def stair_exit(state: State):

    print(
        "You spot a door with an EXIT sign — your chance to escape the building!\n"
        "You start smashing the door with your hammer until it breaks open.\n"
        "You enter the stairwell, and thick, greenish virus smoke fills the space.\n"
        "The acrid fumes make it hard to breathe, and the groans of zombies echo from below.\n"
        "The upper floors are blocked by debris, leaving no other route.\n"
        "You hear loud noises coming from where the door is. The wall starts to crumble — you're stuck!\n"
        "You must find a way to pass the smoke to leave the building. There is nowhere else to go.\n"
    )

    can_choose_action = True

    while True:
        cmd, *args = get_user_input()

        print(
            "Possible commands:\n"
            "Improvise a mask with keycard\n"
            "Rush through the smoke without any protection.\n"
            "Try to force open the blocked doors to create another route.\n"
        )

        match cmd:
            case Command.help:
                display_help()

            case Command.answer:
                if can_choose_action:
                    if not args:
                        print("Invalid syntax! You need to provide an answer.")
                        continue

                    match " ".join(args):
                        case "Improvise a mask with keycard":
                            print(
                                "You press the keycard tightly over your nose and mouth — the plastic shielding you from the worst of the fumes.\n"
                                "The groans below grow louder, but you stay low, moving past the thickest clouds.\n"
                                "At the far end of the stairwell, you stumble into a service landing with a heavy steel door.\n"
                                "It’s the emergency exit!\n"
                                "You use the master key on the door... It works!\n"
                                "You are free!"
                            )

                        case "Rush through the smoke without any protection.":
                            print(
                                "You rush straight into the thick smoke. Your lungs burn and your vision blurs.\n"
                                "You have three chances to make it through alive."
                            )
                            life = 3
                            while life > 0:
                                print(f"\nYou have {life} chances left.")
                                print(
                                    "Possible commands:\n"
                                    "Keep pushing forward blindly\n"
                                    "Drop low to the ground to find cleaner air\n"
                                    "Search around in the smoke for something useful"
                                )
                                action = input("> ").strip()

                                match action:
                                    case "Keep pushing forward blindly":
                                        print(
                                            "You stumble blindly, coughing harder. Your strength fades.\n"
                                            "You fall to the floor, unconscious. Game Over."
                                        )
                                        state.current_room = "stair_exit"
                                        return state

                                    case "Drop low to the ground to find cleaner air":
                                        print(
                                            "You drop low and breathe slightly cleaner air.\n"
                                            "Through the haze, you spot the emergency exit door ahead.\n"
                                            "You reach it and use the master key... It works!\n"
                                            "You are free!"
                                        )

                                    case "Search around in the smoke for something useful":
                                        print("You find nothing useful. The smoke chokes you. Game Over.")
                                        state.current_room = "stair_exit"
                                        return state

                                    case "quit":
                                        quit_game()

                                    case _:
                                        print("Invalid option.")
                                        continue

                                life -= 1

                            print("The smoke overwhelms you. Your vision fades to black. Game Over.")
                            state.current_room = "stair_exit"
                            return state

                        case "Try to force open the blocked doors to create another route.":
                            print(
                                "You try to force the blocked doors, but the noise draws zombies closer.\n"
                                "The smoke thickens around you. It’s too late. Game Over."
                            )
                            state.current_room = "stair_exit"
                            return state

                        case _:
                            print("Invalid choice.")
                            continue

            case Command.quit:
                quit_game()

            case Command.pause:
                pause_game(state)

            case Command.stats:
                display_stats()

            case Command.leaderboard:
                display_leaderboard()

            case _:
                display_invalid_command()
                continue

    return state


if __name__ == "__main__":
    from datetime import datetime

    test_state = State(
        player_name="TestPlayer",
        current_room="stair_exit",
        previous_room="west_corridor",
        visited_rooms=[],
        time_played=TimeDelta(),
        inventory=[],
        session_start_time=datetime.now(),
    )
    stair_exit(test_state)
