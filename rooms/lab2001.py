# #Illia Room

def lab2001(state):
    if state["rooms_visited"]["Lab2001"]:
        print("You have already seen this room")
        state["rooms_visited"]["Lab001"] = True
    else:
        print("you enter a room for the first time")

    print(
        "Possible commands:\n"
        "Look around\n"
        "Quit\n",
    )

    while True:
        user_input = input("> ")

        match user_input.strip().lower():
            case "look around":
                print(
                    "You enter Lab 001. The lights flicker on and off, making strange shadows on the walls.\n"
                    "Tables are overturned, and zombies shuffle between them, their groans filling the silence.\n"
                    "On a nearby desk, you spot a Keycard that could unlock electronic doors in the corridor.\n"
                    "The zombies are too close for comfort, though. You'll have to be careful if you want to grab it without being noticed."
                )

                while True:
                    userguess = input(
                        "Possible commands:\n"
                        "Sneak (Try to sneak past the zombies to get the Keycard)\n"
                        "Fight (Fight the zombies)\n"
                        "Fly away (Attempt to fly away)\n"
                        "Set the building on fire (Set the lab on fire)\n"
                        "? (? Show this help message)\n"
                        "Quit\n"
                        "> "
                    )

                    match userguess.strip().lower():
                        case "fight":
                            print("something fight")
                        case "fly away":
                            print("Something bad happend")
                        case "set the building on fire":
                            print("Nice, you died")
                        case "fly away":
                            state["go to lobby"] = "Lobby"
                            return
                        case "sneak":
                            print("You won")
                            state["current_room"] = "EastCorridor"
                            return
                            break

            case "quit":
                exit()


if __name__ == "__main__":
    import copy

    from main import state as main_state

    state = copy.deepcopy(main_state)
    lab2001(state)
