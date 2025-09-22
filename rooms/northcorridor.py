def northcorridor(state):
    if not state["rooms_visited"]["NorthCorridor"]:
        state["rooms_visited"]["NorthCorridor"] = True
        print(
            "You step into the North Corridor for the first time. You see a bunch of rooms in the corridor. You check which room you can visit"
        )
    else:
        print("You are back in the East Corridor.")

    while True:
        print(
            "Possible commands:\n"
            "Go to Lobby\n"
            "Go to Front Desk Office\n"
            "Go to Storage Room\n"
            "Go to Teachers room\n"
            "Go to East Corridor\n"
            "Quit"
        )

        choice = input("> ")
        match choice.strip().lower():
            case "go to lobby":
                state["current_room"] = "Lobby"
                return
            case "go to front desk office":
                state["current_room"] = "FrontDeskOffice"
                return
            case "go to storage room":
                state["current_room"] = "Storage"
                return
            case "go to teachers room":
                state["current_room"] = "TeachersRoom4"
                return
            case "go to east corridor":
                state["current_room"] = "EastCorridor"
                return
            case "quit":
                exit()
            case _:
                print("Invalid choice. Try again.")
