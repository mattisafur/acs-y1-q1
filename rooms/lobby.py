def lobby(state):
    if not state["rooms_visited"]["Lobby"]:
        state["rooms_visited"]["Lobby"] = True
        print(
            "You step into the Lobby for the first time after unlocking the door. "
        )
    else:
        print("You are back in the Lobby.")

    while True:
        print(
            "Possible commands:\n"
            "Go to West Corridor\n"
            "Go to North Corridor\n"
            "Quit"
        )

        choice = input("> ")
        match choice.strip().lower():
            case "go to west corridor":
                state["current_room"] = "WestCorridor"
                return
            case "go to north corridor":
                if state["inventory"]["Map"]:
                    state["current_room"] = "NorthCorridor"
                    return
                else:
                    print("You need to obtain Map to continue to NorthCorridor.")
            case "quit":
                exit()
            case _:
                print("Invalid choice. Try again.")
