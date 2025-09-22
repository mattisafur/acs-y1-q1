def eastcorridor(state):
    if not state["rooms_visited"]["EastCorridor"]:
        state["rooms_visited"]["EastCorridor"] = True
        print("You step into the East Corridor for the first time. The air smells of dust and chemicals.")
    else:
        print("You are back in the East Corridor.")

    while True:
        print(
            "Possible commands:\n"
            "Go to Lab 2001\n"
            "Go to Lab 2003\n"
            "Go to Lobby\n"
            "Quit"
        )

        choice = input("> ")
        match choice.strip().lower():
            case "go to lab 2001":
                state["current_room"] = "Lab2001"
                return
            case "go to lab 2003":
                state["current_room"] = "Lab2003"
                return
            case "go to lobby":
                state["current_room"] = "Lobby"
                return
            case "quit":
                exit()
            case _:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    import copy

    from main import state as main_state

    state = copy.deepcopy(main_state)
    eastcorridor(state)
