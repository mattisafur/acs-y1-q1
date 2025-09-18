def eastcorridor(state):
    if not state["rooms_visited"]["EastCorridor"]:
        state["rooms_visited"]["EastCorridor"] = True
        print("You step into the East Corridor for the first time. The air smells of dust and chemicals.")
        else:
        print("You are back in the East Corridor.")

    while True:
            print(
            "1) Go to Lab 2001\n"
            "2) Go to Lab 2003\n"
            "3) Go to Lobby")

        choice = input("> ")
        match choice:
            case "1":
                state["current_room"] = "lab2001"
                return
            case "2":
                state["current_room"] = "lab2003"
                return
            case "3":
                state["current_room"] = "lobby"
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
