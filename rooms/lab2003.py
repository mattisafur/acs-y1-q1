import copy


def lab2003(state):
    state_snapshot = copy.deepcopy(state)

    # Check if the room has been visited
    if not state["rooms_visited"]["Lab2003"]:
        print("You enter the room for the first time.")
        state["rooms_visited"]["Lab2003"] = True
    else:
        print("You have already seen this room.")

    print(
        "You enter the Computer Lab. The room is dark, with overturned chairs and scattered papers on the floor.\n"
        "A few computer screens are still flickering, casting eerie light across the walls\n"
        "The silence is broken only by the buzzing of old machines and the distant growls of zombies\n"
        "On the main monitor, a glowing message appears:\n"
        "“Login required – Insert authorized password.\n”"
        "You remember the strange code from the classroom earlier\n"
    )

    while True:
        print(
            "Possible commands:\n"
            "Enter the code 72946\n"
            "Try a random number\n"
            "Smash the keyboard in frustration\n"
            "Shut down the computer\n"
            "Go to East Corridor\n"
            "Quit"
        )
        choice = input("> ")

        match choice.strip().lower():
            case "enter the code 72946":
                print(
                    "You carefully type in 72946. After a short pause, the screen unlocks.\n"
                    "The computer reveals the digital map of the school.\n"
                    "Safe rooms are highlighted in green, blocked corridors in red, and the emergency exits glow in blue.\n"
                    "You quickly print a copy and take it with you.\n"
                    "You obtained the map.\n"
                    "You are being redirected to the corridor to continue the game"
                )
                state["inventory"]["Map"] = True
                state["current_room"] = "EastCorridor"
                return
            case "try a random number":
                print(
                    "The loud error beep echoes through the room.\n"
                    "You panic, worried the zombies outside heard it. You leave in a rush, empty-handed."
                )
                state["current_room"] = "EastCorridor"
                return
            case "smash the keyboard in frustration":
                print(
                    "The monitor flickers and dies.\n"
                    "No chance of recovering the information now.\n"
                    "You storm out angrily."
                )
                state = state_snapshot
                return
            case "shut down the computer":
                print(
                    "The screen goes black.\n"
                    "You realize you just locked yourself out of the system.\n"
                    "With no time to fix it, you leave the lab."
                )
                state["current_room"] = "EastCorridor"
                return
            case "go to east corridor":
                state["current_room"] = "EastCorridor"
                return
            case "quit":
                exit()
            case _:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    import copy

    from main import state as main_state

    state = copy.deepcopy(main_state)
    lab2003(state)
