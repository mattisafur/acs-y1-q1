import copy


def frontdeskoffice(state):
    state_snapshot = copy.deepcopy(state)

    print(
        "You step into the room\n"
        "Possible commands:\n"
        "Look around\n"
        "Go to Lobby\n"
        "Quit", )

    while True:
        user_input = input("> ")

        match user_input.strip().lower():
            case "look around":
                print(
                    "You enter the Front Desk office. A zombie is slumped in a chair, seemingly asleep.\n"
                    "The room is filled with clutter, and you notice a glint of metal under the zombie.\n"
                    "It is the Master Key and you’ll have to retrieve it carefully without waking the zombie."
                )

                print(
                    "Possible commands:\n"
                    "Look around\n"
                    "Fight\n"
                    "Sneak around"
                )

                while True:
                    user_input = input("> ")
                    match user_input.strip().lower():
                        case "look around":
                            print(
                                "You look around the room for anything useful in this situation.\n"
                                "you see a jacket left behind by a student on a chair. you pick it up\n"
                                "Maybe it could be helpful.\n"
                                "Possible commands:\n"
                                "Fight\n"
                                "Go to Corridor\n"
                                "Tie the zombie up"
                            )
                            state["inventory"]["Jacket"] = True

                            while True:
                                user_input = input("> ")
                                match user_input.strip().lower():
                                    case "fight":
                                        print("you died")
                                        state = state_snapshot
                                        state["current_room"] = "NorthCorridor"
                                        return
                                    case "go to corridor":
                                        print("As you try to leave the room the zombie wakes up and you die")
                                        state = state_snapshot
                                        state["current_room"] = "NorthCorridor"
                                        return
                                    case "tie the zombie up":
                                        print(
                                            "Where on the zombie do you wanna tie?\n"
                                            "possible commands:\n"
                                            "Tie his face\n"
                                            "Tie his Body"
                                        )
                                        while True:
                                            user_input = input("> ")
                                            match user_input.strip().lower():
                                                case "tie his face":
                                                    print(
                                                        "You tied his face so the zombie cannot see you,\n"
                                                        "however the zombie can still smell you and wakes up\n"
                                                        "You died"
                                                    )
                                                    state = state_snapshot
                                                    return

                                                case "tie his body":
                                                    print(
                                                        "You tied the zombie to the chair. It violently wakes up and tries to attack you.\n"
                                                        "However, the zombie is tied down and cannot move. You quickly grab the Master Key\n"
                                                        "and head out of the front office"
                                                    )
                                                    state["inventory"]["MasterKey"] = True

                                                    state["current_room"] = "NorthCorridor"
                                                    return

                        case "fight":
                            print("you die")
                            state = state_snapshot
                            state["current_room"] = "NorthCorridor"
                            return
                        case "sneak around":
                            print(
                                "You immediately become silent and approach the zombie carefully\n"
                                "Any action from here on out has to be very quiet. You have to type\n"
                                "out every action with lowercase letters to not wake the zombie up."
                            )
                            print(
                                "Possible commands:\n"
                                "Move the zombie\n"
                                "Dig the key from under the zombie"
                            )

                            while True:
                                user_input = input("> ")

                                if any(char.isupper() for char in user_input):
                                    print("You spoke too loudly, the zombie woke up. You have died.")
                                    state = state_snapshot
                                    state["current_room"] = "NorthCorridor"
                                    return
                                match user_input.strip().lower():
                                    case "move the zombie":
                                        print("You wake up the zombie. you have died.")
                                        state = state_snapshot
                                        state["current_room"] = "NorthCorridor"
                                        return
                                    case "dig the key from under the zombie":
                                        print(
                                            "you manage to take the master key from under the zombie.\n"
                                            "you immediately leave the room"
                                        )
                                        state["inventory"]["MasterKey"] = True

                                        state["current_room"] = "NorthCorridor"
                                        return
            case "go to lobby":
                state["go to lobby"] = "Lobby"
                return
            case "quit":
                exit()
