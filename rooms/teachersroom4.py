def teachersroom4(state):
    if state["rooms_visited"]["TeacherRoom4"]:
        print("You have already seen this room")
        state["rooms_visited"]["TeachersRoom4"] = True
    else:
        print("you enter a room for the first time")

    print(
        "Possible commands:\n"
        "Look around\n"
        "Go to Lobby\n"
        "Quit",
    )

    while True:
        user_input = input("> ")

        match user_input.strip().lower():
            case "look around":
                print(
                    "You step into the teacher’s lounge. Papers are scattered, coffee mugs still half full. "
                    "A bookshelf is tilted, blocking part of the exit. On the desk you see four folders labeled A, B, C, D with notes stuck to them. "
                    "A whiteboard says: ‘Put knowledge in the right order. Only then the truth is revealed.’"
                )

                userguess = input(
                    "The teacher’s lounge is a mess. The bookshelf looks unstable.\n"
                    "On the desk are four folders labeled A, B, C, D. Each has a note:\n"
                    "Folder A: ‘Comes after B.’\n"
                    "Folder B: ‘Must be first.’\n"
                    "Folder C: ‘Is never next to A.’\n"
                    "Folder D: ‘Always after C.’\n"
                    "A whiteboard reads: ‘Put knowledge in the right order. Only then the truth is revealed.’"
                )

                while userguess != "BCDA":
                    userguess = input("Incorrect, try again!")

                print("Correct, you solved this one")

                state["current_room"] = "Lobby"
                return
            case "go to lobby":
                state["current_room"] = "Lobby"
                return
            case "quit":
                exit()


if __name__ == "__main__":
    import copy

    from main import state as main_state

    state = copy.deepcopy(main_state)
    teachersroom4(state)
