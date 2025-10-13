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


def stair_exit(state: State):
    print(
        "You spot a door with a exit sign. That is your chance to escape the building\n"
        "You start to smash the door with your hammer until it breaks open.\n"
        "You enter the stairwell, and thick, greenish virus smoke fills the space.\n"
        "The acrid fumes make it hard to breathe, and the groans of zombies echo from below.\n"
        "The upper floors are blocked by debris, leaving no other route.\n"
        "You hear loud noises coming from where the door ir. The wall start to fall. You are stuck\n"
        "You must find a way to pass the smoke in order to leave the building. There is nowhere else to go. What do you do?"
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
                raise NotImplementedError

            case Command.answer:
                if can_choose_action:
                    if not args:
                        print("Invalid syntax! You need to provide an answer.")
                        continue
                    match " ".join(args):
                        case "Improvise a mask with keycard":
                            print(
                                "You press the keycard tightly over your nose and mouth, the plastic shielding you from the worst of the fumes.\n"
                                "The groans below grow louder, but you stay low, moving past the thickest clouds.\n"
                                "At the far end of the stairwell, you stumble into a service landing with a heavy steel door.\n"
                                "It is the emergency exit!\n"
                                "You use the masterkey on the door... It works!"
                                "You are free!"
                            )
                            state.current_room = "west_corridor"
                            return
                        case "Rush through the smoke without any protection.":
                            print(
                                "You rush straight into the thick smoke, your lungs are burning.\n"
                                "You have three chances: \n"
                            )
                            life = 3
                            while life > 0:
                                print(f"You have {life} chances left to escape the smoke.")
                                print("Possible commands:\n"
                                      "Keep pushing forward blindly\n"
                                      "Drop low to the ground to find cleaner air\n"
                                      "Search around in the smoke for something useful")
                                action = input("> ")
                                match action:
                                    case "Keep pushing forward blindly":
                                        print("You stumble blindly, coughing harder. Your strength fades.\n"
                                              "You fall to the floor unconsciously. Game Over.")
                                        return
                                    case "Drop low to the ground to find cleaner air":
                                        print("You drop low and breathe slightly cleaner air.\n"
                                              "Through the haze, you spot the emergency exit door ahead.\n"
                                              "You are able to get to the exit door.\n"
                                              "You use the masterkey on the door... It works!\n"
                                              "You are free!")
                                        state.current_room = "west_corridor"
                                        return
                                    case "Search around in the smoke for something useful.":
                                        print("You don't find anything.\nGame Over.")
                                        return
                                    case "quit":
                                        exit()
                                    case _:
                                        print("Option Invalid.")
                                life -= 1
                            else:
                                print("The smoke overwhelms you. Your vision fades to black. Game Over.")
                                state.current_room = "stair_exit"
                                return
                        case "Try to force open the blocked doors to create another route.":
                            print("You try to force the blocked doors, but the noise draws zombies closer.\n"
                                  "The smoke thickens around you. It’s too late. Game Over.")
                            state.current_room = "stair_exit"
                            return
                        case _:
                            print("Invalid choice.")
            case Command.quit:
                quit_game()
            case Command.pause:
                pause_game(state)

            case Command.stats:
                display_stats()

            case Command.leaderboard:
                display_leaderboard()

if __name__ == "__main__":
    test_state = State(
        player_name="TestPlayer",
        current_room="stair_exit",
        previous_room="",
        visited_rooms=[],
        time_played=TimeDelta(),
        inventory=[],
    )
    stair_exit(test_state)
