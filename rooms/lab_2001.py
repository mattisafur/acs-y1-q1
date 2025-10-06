from models import State, Command, Inventory
from util import get_user_input, print_leaderboard

def lab_2001(state: State):
    if "lab_2001" in state.visited_rooms:
        print("You have already seen this room")
    else:
        print("You enter a room for the first time")
        state.visited_rooms.append("lab_2001")
    
    print(
        "Possible commands:\n"
        "--- Look around\n"
        "--- Quit\n",
    )

    while True:
        user_input = get_user_input()

        match user_input.strip().lower():
            case "look around":
                print(
                    "You enter Lab 2001. The lights flicker on and off, making strange shadows on the walls.\n"
                    "Tables are overturned, and zombies shuffle between them, their groans filling the silence.\n"
                    "On a nearby desk, you spot a Keycard that could unlock electronic doors in the corridor.\n"
                    "The zombies are too close for comfort, though. You'll have to be careful if you want to grab it without being noticed."
                )

                while True:
                    userguess = get_user_input(
                        "Possible commands:\n"
                        "Sneak (Try to sneak past the zombies to get the Keycard)\n"
                        "Fight (Fight the zombies)\n"
                        "Fly away (Attempt to fly away)\n"
                        "Set the building on fire (Set the lab on fire)\n"
                        "? (Show this help message)\n"
                        "Quit\n"
                        "> "
                    )

                    match userguess:
                        case "fight":
                            print("You try to fight the zombies, but there are too many!")
                            print("You die a horrible death...")
                            # Return to the previous room or game over
                            state.current_room = state.previous_room if state.previous_room else "main_menu"
                            return
                        
                        case "set the building on fire":
                            print("Nice idea! But you're still inside...\n"
                                "You died in the flames!\n")
                            state.current_room = "main_menu"
                            return
                        
                        case "fly away":
                            print("You flap your arms... but humans can't fly!\n"
                                "The zombies notice you. Time to go!\n")
                            state.previous_room = "lab_2001"
                            state.current_room = "lobby"
                            return
                        
                        case "sneak":
                            print("You carefully sneak past the zombies...\n"
                                "You grab the Keycard! SUCCESS!\n"
                                "You quietly slip out to the East Corridor.\n")
    # TODO: Add keycard to inventory when Inventory class is implemented
    # state.inventory.add_item("keycard")
                            state.previous_room = "lab_2001"
                            state.current_room = "east_corridor"
                            return
                        
                        case "quit":
                            print("Thanks for playing!")
                            exit()
                        
                        case _:
                            print("Invalid choice. Try again.")
            
            case "quit":
                print("Thanks for playing!")
                exit()
            
            case _:
                print("Invalid command. Try 'Look around' or 'Quit'.")


if __name__ == "__main__":

    # DOESNT WORK WITHOUT THIS STUFF!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


    # This runs only when testing the room standalone
    import sys
    from pathlib import Path
    from datetime import time as Time
    
    # Add parent directory to Python path so we can import from main folder
    parent_dir = Path(__file__).parent.parent
    sys.path.insert(0, str(parent_dir))
    
    from models import State, Inventory
    
    state = State(
        user_name="Tester",
        current_room="lab_2001",
        previous_room="main_menu",
        visited_rooms=[],
        time_played=Time(),
        inventory=Inventory()
    )