# # print("you enter a room")
# #
# #
# #
# # print("You see a barren classroom with something written on the whiteboard."
# #       " You take a closer look. \n "
# #       "It seems to be a password to a computer, but it is encrypted."
# #       " On the whiteboard, it says: \n ")
# #
# # userguess = input(
# #     "Dial 1 is a prime number greater than 5. \n "
# #     "Dial 2 is the smallest prime number. \n "
# #     "Dial 3 equals (Dial 1 + Dial 4 − Dial 2). \n "
# #     "Dial 4 is a perfect square digit, it’s even, and it’s greater than 2. \n "
# #     "Dial 5 shows a number that is exactly one less than Dial 1. \n "
# #     "Self-check: The sum of all five digits should be 28. \n "
# #     "What is your guess")
# #
# #
# # while userguess != "72946":
# #     userguess = input("Incorrect, try again")
# #
# # print("Correct, You solved the puzzle and wrote down the combination on a piece of paper.")
# #
# #
# #
# #
# # Print("You have already seen this room")
#
# def projectroom1(state):
#     if state["rooms_visited"]["ProjectRoom1"]:
#         print("you enter a room for the first time")
#     else:
#         print("You have already seen this room")
#
#     state["rooms_visited"]["ProjectRoom1"] = True
#
#     while True:
#         print("Type \"Look around\" to look around")
#
#         user_input = input("> ")
#
#         if user_input == "Look around":
#             break
#
#         print('"Hey man, you should look around." someone whispered ')
#
#
# print("You see a barren classroom with something written on the whiteboard."
#        " You take a closer look. \n "
#        "It seems to be a password to a computer, but it is encrypted."
#        " On the whiteboard, it says: \n ")
#
# userguess = input(
#     "Dial 1 is a prime number greater than 5. \n "
#     "Dial 2 is the smallest prime number. \n "
#     "Dial 3 equals (Dial 1 + Dial 4 − Dial 2). \n "
#     "Dial 4 is a perfect square digit, it’s even, and it’s greater than 2. \n "
#     "Dial 5 shows a number that is exactly one less than Dial 1. \n "
#     "Self-check: The sum of all five digits should be 28. \n "
#     "What is your guess")
#
# # while userguess != "72946":
# #     userguess = input("Incorrect, try again")
# #
# # print("Correct, You solved the puzzle and wrote down the combination on a piece of paper.")
#
#
#
#
#
#
#
#

def projectroom1(state):
    if state["rooms_visited"]["ProjectRoom1"]:
        print("You have already seen this room")
    else:
        print("you enter a room for the first time")

    state["rooms_visited"]["ProjectRoom1"] = True

    print(
        "possible commands:\n"
        "look around\n"
        "go to lobby\n"
        "quit"
    )

    while True:
        user_input = input("> ")

        match user_input:
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

                print("Correct, You solved the puzzle and wrote down the combination on a piece of paper, and return to the lobby.")

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
