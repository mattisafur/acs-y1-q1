def westcorridor(state):
    firt_time_in_room = False
    if not state["rooms_visited"]["WestCorridor"]:
        print("You are first time in West Corridor")
        state["rooms_visited"]["WestCorridor"] = True
        firt_time_in_room = True
    else:
        print("You w been here")

    print(
        "You can see this\n"
        "You can see this\n"
        "You can see this\n"
        "You can see this"
    )
    while True:
        print(
            "Go to Lab2001 \n"
            "Go to ... \n"
            "Go to ... \n"
            "Go to ... \n"
            "Go to ... \n"
        )

        choice = input ("> ")

        match choice:
            case "Go to Lab2001":
                print("Okey, you are going into Lab 2001")
                state["current_room"] = "Lab2001"
                return

            case "Go to ...":
                print("Okey, you are going into ...")
                state["current_room"] = "..."
                return

            case "Go to ...":
                print("Okey, you are going into ...")
                state["current_room"] = "..."
                return

            case "Go to ...":
                print("Okey, you are going into ...")
                state["current_room"] = "..."
                return

if __name__ == "__main__":
    import copy

    from main import state as main_state

    state = copy.deepcopy(main_state)
    westcorridor(state)
