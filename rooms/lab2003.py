def lab2003(state):
    # Check if the room has been visited
    if not state["rooms_visited"]["Lab2003"]:
        print("You enter the room for the first time.")
        state["rooms_visited"]["Lab2003"] = True
    else:
        print("You have already seen this room.")

    print("You enter the Computer Lab. The room is dark, with overturned chairs and scattered papers on the floor.\n"
          "A few computer screens are still flickering, casting eerie light across the walls\n"
          "The silence is broken only by the buzzing of old machines and the distant growls of zombies\n"
          "On the main monitor, a glowing message appears:\n"
          "“Login required – Insert authorized password.\n”"
          "You remember the strange code from the classroom earlier\n")

    while True:
        print("A) Enter the code 72946\n"
              "B) Try a random number\n"
              "C) Smash the keyboard in frustration\n"
              "D) Shut down the computer\n")
        choice = input("> ")

        match choice:
            case "A":
                print("You carefully type in 72946. After a short pause, the screen unlocks.")
                print("The computer reveals the digital floor plan of the school.")
                print("Safe rooms are highlighted in green, blocked corridors in red, and the emergency exits glow in blue.")
                print("You quickly print a copy and take it with you.")
                print("You obtained the Floor Plan.")
                break

            case "B":
                print("The loud error beep echoes through the room.")
                print("You panic, worried the zombies outside heard it. You leave in a rush, empty-handed.")
                break

            case "C":
                print("The monitor flickers and dies.")
                print("No chance of recovering the information now.")
                print("You storm out angrily.")
                break

            case "D":
                print("The screen goes black.")
                print("You realize you just locked yourself out of the system.")
                print("With no time to fix it, you leave the lab.")
                break

            case _:
                print("Invalid choice. Try again.")

            case "go to EastCorridor":
                state["current_room"] = "EastCorridor"
                return
            case "quit":
                exit()

if __name__ == "__main__":
    import copy

    from main import state as main_state

    state = copy.deepcopy(main_state)
    lab2003(state)
