import copy


def westcorridor(state):
    state_snapshot = copy.deepcopy(state)
    firt_time_in_room = False
    if not state["rooms_visited"]["WestCorridor"]:
        print("You are first time in West Corridor")
        state["rooms_visited"]["WestCorridor"] = True
        firt_time_in_room = True
    else:
        print("You have been here")

    # TODO we need to implement rooms where the player will go and what rooms he will see
    print(
        "You can see this\n"
        "You can see this\n"
        "You can see this\n"
        "You can see this\n"
    )
    while True:
        print(
            "Go to Stair Exit \n"
            "Go to Teachers Room 4\n"
            "Go to East Corridor \n"
            "go to Classroom 2.031\n"
            "Go to Classroom 2.032"
        )

        choice = input("> ")

        match choice.strip().lower():
            case "go to stair exit":
                print("Okay, you are going into StairExit")
                state["current_room"] = "StairExit"
                return

            case "go to teachers room 4":
                print("Okay, you are going into Teachers Room 4")
                state["current_room"] = "TeachersRoom4"
                return

            case "go to east corridor":
                print("Okay, you are going into ...")
                state["current_room"] = "EastCorridor"
                return

            case "go to classroom 2.031" | "Go to classroom 2.032":
                print("The door is locked, is not possible to get in.")
                return


if __name__ == "__main__":
    import copy

    from main import state as main_state

    state = copy.deepcopy(main_state)
    westcorridor(state)
