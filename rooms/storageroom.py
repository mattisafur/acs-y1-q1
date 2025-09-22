def storageroom(state):
    if state["rooms_visited"].get("storageroom", False):
        print("You have already seen this room.")
    else:
        print("You enter a room for the first time.")
        state["rooms_visited"]["storageroom"] = True

    print("\nPossible commands:\n")
    print("Look around\n")
    print("Go to lobby\n")
    print("Quit")

    print("\nYou step into the Storage room.")
    print("You can barely see anything.")
    print("To your left, you see a table flipped over.")
    print("To your right, you see a very big cabinet.")
    print("In front of you is a pathway made by fallen debris, flipped tables, and chairs.")

    while True:
        print("\nWhich option would you like to explore?")
        print("move a few steps -  Move a few steps forward and explore the maze created by the debris.")
        print("move past dig cabinet - Try to move past the big cabinet.")
        print("leave - Leave the room.")
        print("move past table - See if you can move past the table to your left.")
        print("Or type 'go to lobby' or 'quit' at any time.")

        user_choice = input("\nEnter your choice: ").strip().lower()

        if user_choice == "move a few steps":
            print(
                "You move forward and see the pathway splitting into two paths. One to your right and one to the left."
                )

            user_choice2 = input(
                "\nChoose:\ngo left - Take the path to the left\ngo right - Take the path to the right\n> "
                ).strip().lower()

            if user_choice2 == "go left":
                print("\nYou walk on the left path and get surprised by a zombie!")
                print("You try to escape, but fail to choose quickly enough and get killed.")
                state["current_room"] = "Lobby"
                return

            elif user_choice2 == "go right":
                print("\nYou take the path to the right and reach another fork.")

                user_choice3 = input("\nGo left\nGo right\n> ").strip().lower()

                if user_choice3 == "go left":
                    print("\nYou find a familiar door handle. It's the emergency exit door.")
                    print("You return to the Lobby with new information.")
                    # code to pick up and add door handle to inverntory
                    state["current_room"] = "Lobby"
                    return

                elif user_choice3 == "go right":
                    print(
                        "\nYou walk onto the path on the right and get jumpscared by a zombie that instantly bites you."
                        )
                    state["current_room"] = "Lobby"
                    return

                else:
                    print("Invalid option in the second fork.")

            else:
                print("Invalid option in the first fork.")

        elif user_choice == "move past dig cabinet":
            print("\nYou try to push past the big cabinet, but it's too heavy. You reconsider your options.")

        elif user_choice == "leave" or user_choice == "go to lobby":
            print("\nYou leave the storage room and return to the lobby.")
            state["current_room"] = "Lobby"
            return

        elif user_choice == "move past table":
            print("\nYou try to move past the table, but it’s too cramped to squeeze through.")

        elif user_choice == "quit":
            print("Exiting game.")
            exit()

        else:
            print("Invalid input. Try again.")


if __name__ == "__main__":
    import copy

    from main import state as main_state

    state = copy.deepcopy(main_state)
    storageroom(state)
