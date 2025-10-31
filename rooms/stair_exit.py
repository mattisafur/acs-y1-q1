from datetime import timedelta as TimeDelta
import time
from models import Command, State
from db import initialize_database
from util import (
    display_invalid_syntax,
    display_go_help,
    display_leaderboard,
    display_stats,
    display_take_help,
    display_take_list,
    get_user_input,
    pause_game,
    quit_game,
    display_help,
    display_where_am_i,
    display_items_list,
    display_inventory,
    display_map,
    submit_leaderboard,
)

def stair_exit(state: State):
    initialize_database()
    pickable_items: list[str] = []
    can_choose_action = True

    if "storage_room" not in state.visited_rooms:
        print("The door is locked. You might need to find something first.")
        state.current_room = "west_corridor"
        return state

    print(
        "\n"
        "You spot a door with an EXIT sign — your chance to escape the building!\n"
        "You start smashing the door with your hammer until it breaks open.\n"
        "You enter the stairwell, and thick, greenish virus smoke fills the space.\n"
        "The acrid fumes make it hard to breathe, and the groans of zombies echo from below.\n"
        "The upper floors are blocked by debris, leaving no other route.\n"
        "You hear loud noises coming from where the door is. The wall starts to crumble — you're stuck!\n"
        "You must find a way to pass the smoke to leave the building. There is nowhere else to go.\n"
    )
    time.sleep(1)
    print(
        "How will you go through the smoke?\n"
        "Possible commands:\n"
        "1.Improvise a mask with keycard\n"
        "2.Rush through the smoke without any protection.\n"
        "3.Try to force open the blocked doors to create another route.\n"
    )

    while True:
        cmd, *args = get_user_input()
        user_input = " ".join([cmd] + args).lower()

        if can_choose_action:
            if user_input == "1":
                print(
                    "You press the keycard tightly over your nose and mouth — the plastic shielding you from the worst of the fumes.\n"
                    "The groans below grow louder, but you stay low, moving past the thickest clouds.\n"
                    "At the far end of the stairwell, you stumble into a service landing with a heavy steel door.\n"
                    "It’s the emergency exit!\n"
                    "You use the master key on the door... It works!\n"
                    "You are free!\n"
                )
                print(
                    "Congratulations, you have finished the game!\n"
                    "Please rate it 100 stars out of 10."
                    "Thanks for Playing!\n"
                )
                submit_leaderboard(state)
                quit()



            elif user_input == "2":
                print(
                    "You rush straight into the thick smoke. Your lungs burn and your vision blurs.\n"
                    "You have three chances to make it through alive."
                )
                life = 3
                while life > 0:
                    print(f"\nYou have {life} chances left.")
                    print(
                        "Possible commands:\n"
                        "1.Keep pushing forward blindly\n"
                        "2.Drop low to the ground to find cleaner air\n"
                        "3.Search around in the smoke for something useful"
                    )
                    action = input("> ").strip().lower()
                    match action:
                        case "1":
                            print(
                                "You stumble blindly, coughing harder. Your strength fades.\n"
                                "You fall to the floor, unconscious. Game Over.\n"
                            )
                            state.current_room = "stair_exit"
                            life -= 1
                            return state
                        case "2":
                            print(
                                "You drop low and breathe slightly cleaner air.\n"
                                "Through the haze, you spot the emergency exit door ahead.\n"
                                "You reach it and use the master key... It works!\n"
                                "You are free!"
                            )
                            print(
                                "Congratulations, you have finished the game!\n"
                                "Please rate it 100 stars out of 10."
                                "Thanks for Playing!\n"
                            )
                            submit_leaderboard(state)
                            quit()
                        case "3":
                            print("You find nothing useful. The smoke chokes you. Game Over.\n")
                            state.current_room = "stair_exit"
                            return state
                        case "quit":
                            quit_game()
                        case _:
                            print("Invalid option.")
                            continue
                    # life -= 1
                print("The smoke overwhelms you. Your vision fades to black. Game Over.\n")
                state.current_room = "stair_exit"
                return state

            elif user_input == "3":
                print(
                    "You try to force the blocked doors, but the noise draws zombies closer.\n"
                    "The smoke thickens around you. It’s too late. Game Over.\n"
                )
                state.current_room = "stair_exit"
                return state

        match cmd:
            case Command.look:
                if (len(args) == 0) or (len(args) == 1 and args[0].lower() == "around"):
                    print(
                        "The stairwell is filled with thick, greenish smoke. Debris blocks the upper floors,\n"
                        "and distant groans echo from below. You notice your keycard and master key might help\n"
                        "you improvise a way through the smoke."
                    )
                    continue
            case Command.map:
                display_map()
            case Command.help:
                display_help()
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
            case Command.where:
                display_where_am_i(state)
                continue
            case Command.go:
                if len(args) != 1:
                    display_invalid_syntax("go")
                    continue
                match args[0]:
                    case "?":
                        display_go_help()
                        continue
            case Command.take:
                if len(args) != 1:
                    display_invalid_syntax("take")
                    continue
                item = args[0].lower()
                match item:
                    case "?":
                        display_take_help()
                        continue
                    case "list":
                        display_take_list(pickable_items)
                        continue
            case Command.items:
                display_items_list()
                continue
            case Command.inventory:
                display_inventory(state)
                continue
            case _:
                print("Invalid command.")
                continue


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
