import copy


def projectroom1(state):
    state_snapshot = copy.deepcopy(state)

    if state["rooms_visited"]["ProjectRoom1"]:
        print("You have already seen this room")
        state["current_room"] = "Lobby"
        return
    else:
        print("you enter a room for the first time")
        state["rooms_visited"]["ProjectRoom1"] = True
    print(
        "Possible commands:\n"
        "Look around\n"
        "Go to lobby\n"
        "Quit"
    )

    while True:
        user_input = input("> ")

        match user_input.strip().lower():
            case "look around":
                print(
                    "You see a barren classroom with something written on the whiteboard.\n"
                    "You take a closer look.\n"
                    "It seems to be a password to a computer, but it is encrypted.\n"
                    "On the whiteboard, it says:"
                )

                userguess = input(
                    "Dial 1 is a prime number greater than 5. \n "
                    "Dial 2 is the smallest prime number. \n "
                    "Dial 3 equals (Dial 1 + Dial 4 − Dial 2). \n "
                    "Dial 4 is a perfect square digit, it’s even, and it’s greater than 2. \n "
                    "Dial 5 shows a number that is exactly one less than Dial 1. \n "
                    "Self-check: The sum of all five digits should be 28. \n "
                    "What is your guess"
                )

                while userguess != "72946":
                    userguess = input("Incorrect, try again")
                    state = state_snapshot

                print(
                    "Correct, You solved the puzzle and wrote down the combination on a piece of paper, and return to the lobby."
                )
                state["inventory"]["Passcode"] = True

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
    projectroom1(state)
