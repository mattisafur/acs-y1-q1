from datetime import timedelta as TimeDelta
import time
from models import Command, State
from db import initialize_database
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
    display_help, display_where_am_i,
    display_items_list,
    display_inventory,
    display_map
)

def stair_exit(state: State):
    initialize_database()
    pickable_items: list[str] = []
    can_choose_action = True


    if "storage_room" not in state.visited_rooms:
        print("The door is locked. You might need to find something first.")
        return state

    print(
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
        "Improvise a mask with keycard\n"
        "Rush through the smoke without any protection.\n"
        "Try to force open the blocked doors to create another route.\n"
    )

    while True:
        cmd, *args = get_user_input()
        user_input = " ".join([cmd] + args).lower()

        # --- Actions for escaping ---
        if can_choose_action:
            if user_input == "improvise a mask with keycard":
                print(
                    "You press the keycard tightly over your nose and mouth — the plastic shielding you from the worst of the fumes.\n"
                    "The groans below grow louder, but you stay low, moving past the thickest clouds.\n"
                    "At the far end of the stairwell, you stumble into a service landing with a heavy steel door.\n"
                    "It’s the emergency exit!\n"
                    "You use the master key on the door... It works!\n"
                    "You are free!"
                )
                return state

            elif user_input == "rush through the smoke without any protection.":
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
                    action = input("> ").strip().lower()
                    match action:
                        case "keep pushing forward blindly":
                            print(
                                "You stumble blindly, coughing harder. Your strength fades.\n"
                                "You fall to the floor, unconscious. Game Over."
                            )
                            state.current_room = "stair_exit"
                            return state
                        case "drop low to the ground to find cleaner air":
                            print(
                                "You drop low and breathe slightly cleaner air.\n"
                                "Through the haze, you spot the emergency exit door ahead.\n"
                                "You reach it and use the master key... It works!\n"
                                "You are free!"
                            )
                            return state
                        case "search around in the smoke for something useful":
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

            elif user_input == "try to force open the blocked doors to create another route.":
                print(
                    "You try to force the blocked doors, but the noise draws zombies closer.\n"
                    "The smoke thickens around you. It’s too late. Game Over."
                )
                state.current_room = "stair_exit"
                return state

        match cmd:
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
    from models import State
    from datetime import timedelta as TimeDelta

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