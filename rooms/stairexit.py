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
            "A) Use the Keycard found at the front office as a makeshift respirator over your nose and mouth to sneak through the smoke.\n"
            "B) Rush through the smoke without any protection.\n"
            "C) Try to force open the blocked doors to create another route.\n"
            "D) Go back to the previous corridor."
            )

        choice = input("> ")

        match choice.upper():
            case "A":
                print(
                    "You press the keycard tightly over your nose and mouth, the plastic shielding you from the worst of the fumes\n"
                    "The groans below grow louder, but you stay low, moving past the thickest clouds.\n"
                    "At the far end of the stairwell, you stumble into a service landing with a heavy steel door.\n"
                    "It is the emergency exit!\n"
                    "You are close to escape the building"
                )
                break
            case "B":
                print("You rush straight into the thick smoke, your lungs are burning.")
                life = 3 #3 chances to escape the smoke

                while life > 0:
                    print(f"You have three chances to escape the smoke. You currently have {life} left.")
                    print("1) Keep pushing forward blindly.\n"
                          "2) Drop low to the ground to find cleaner air.\n"   
                          "3) Search around in the smoke for something useful.")
                    action = input("> ")
                    match action:
                        case "1":
                            print("You stumble blindly, coughing harder. Your strength fades\n"
                                  "You fall to the floor unconsciously")
                        case "2":
                            print("You drop low and breathe slightly cleaner air.\n"
                                  "Through the haze, you spot the emergency exit door ahead.\n"
                                  "You are able to get to the exit door")
                            break
                        case "3":
                            print("You don't find anything.\n"
                                  "Game over")
                        case "quit":
                            exit()
                        case _:
                            print("Option Invalid.")
                    life -= 1
                else:
                    print("The smoke overwhelms you. Your vision fades to black. Game Over.")
            case "C":
                print("You try to force the blocked doors, but the noise draws zombies closer.\n"
                      "The smoke thickens around you. It’s too late. Game Over.")
                state = state_snapshot
                state["current_room"] = "WestCorridor"
                return

            case "D":
                print("You retreat back into the corridor, safe for now. But the stairwell still blocks your escape.")
                state["current_room"] = "WestCorridor"
                return


if __name__ == "__main__":
    import copy

    from main import state as main_state

    state = copy.deepcopy(main_state)
    stairexit(state)