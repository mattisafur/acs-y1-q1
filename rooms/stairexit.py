import copy


def game_won(state):
    print("\nCongratulations! You have successfully escaped the building!")
    state["game_over"] = True
    exit()


def stairexit(state):
    state_snapshot = copy.deepcopy(state)

    if not state["rooms_visited"]["StairExit"]:
        print("You enter the room for the first time.")
        state["rooms_visited"]["StairExit"] = True
    else:
        print("You have already seen this room.")

    print(
        "You enter the stairwell, and thick, greenish virus smoke fills the space.\n"
        "The acrid fumes make it hard to breathe, and the groans of zombies echo from below.\n"
        "The upper floors are blocked by debris, leaving no other route.\n"
        "You must find a way to pass the smoke in order to leave the building.\n"
    )

    while True:
        print(
            "Possible commands:\n"
            "Use Keycard (Use Keycard as a makeshift respirator over your nose and mouth to sneak through the smoke)\n"
            "Rush through the smoke without any protection\n"
            "Force open the blocked doors to create another route\n"
            "Go back\n"
            "Quit"
        )
        choice = input("> ")

        match choice.strip().lower():
            case "use keycard":
                print(
                    "You press the keycard tightly over your nose and mouth, the plastic shielding you from the worst of the fumes\n"
                    "The groans below grow louder, but you stay low, moving past the thickest clouds.\n"
                    "At the far end of the stairwell, you stumble into a service landing with a heavy steel door.\n"
                    "It is the emergency exit!\n"
                    "You are close to escape the building"
                )
                game_won(state)
            case "rush through the smoke without any protection":
                print("You rush straight into the thick smoke, your lungs are burning.")
                life = 3  # 3 chances to escape the smoke

                while life > 0:
                    print(f"You have three chances to escape the smoke. You currently have {life} left.")
                    print(
                        "possible commands:\n"
                        "Keep pushing forward blindly.\n"
                        "Drop low to the ground to find cleaner air.\n"
                        "Search around in the smoke for something useful.\n"
                        "Quit"
                    )
                    action = input("> ")
                    match action:
                        case "Keep pushing forward blindly":
                            print(
                                "You stumble blindly, coughing harder. Your strength fades\n"
                                "You fall to the floor unconsciously"
                            )
                            state = state_snapshot
                        case "Drop low to the ground to find cleaner air":
                            print(
                                "You drop low and breathe slightly cleaner air.\n"
                                "Through the haze, you spot the emergency exit door ahead.\n"
                                "You are able to get to the exit door"
                            )
                            game_won(state)
                            break
                        case "Search around in the smoke for something useful":
                            print(
                                "You don't find anything.\n"
                                "Game over"
                            )
                            state["current_room"] = "Lab2001"
                            return
                        case "Quit":
                            exit()
                        case _:
                            print("Option Invalid.")
                    life -= 1
                else:
                    print("The smoke overwhelms you. Your vision fades to black. Game Over.")
                    state["current_room"] = "Lab2001"
                    return
            case "force open the blocked doors to create another route":
                print(
                    "You try to force the blocked doors, but the noise draws zombies closer.\n"
                    "The smoke thickens around you. It’s too late. Game Over."
                )
                state["current_room"] = "Lab2001"
                return

            case "go back":
                print("You retreat back into the corridor, safe for now. But the stairwell still blocks your escape.")
                state["current_room"] = "WestCorridor"
                return


if __name__ == "__main__":
    import copy

    from main import state as main_state

    state = copy.deepcopy(main_state)
    stairexit(state)
