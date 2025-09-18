# #Illia Room
# import sys
#
# def enterLab001(state):
#     # --- Room entry description ---
#     print(
#         " You enter Lab 001. The lights flicker on and off, making strange shadows on the walls.\n"
#         "Tables are overturned, and zombies shuffle between them, their groans filling the silence.\n"
#         "On a nearby desk, you spot a Keycard that could unlock electronic doors in the corridor.\n"
#         "The zombies are too close for comfort, though. You'll have to be careful if you want to grab it without being noticed."
#     )
#
#     got_keycard = "keycard" in state["inventory"]
#     room_cleared = got_keycard
#
#     # --- Command handlers ---
#     def handle_look():
#         print(
#             "You scan the chaotic lab.\n"
#             "Zombies shuffle between overturned tables, groaning. Shadows dance on the walls."
#         )
#         if not got_keycard:
#             print(
#                 "The Keycard is still on the desk, but the zombies are dangerously close.\n"
#                 "You need to decide how to get it: Sneak, Fight, Fly away, or Set the building on fire."
#             )
#         else:
#             print(
#                 "You already have the Keycard. The zombies seem less interested in you now.\n"
#                 "- Possible exits: lobby\n"
#                 "- Your current inventory:",
#                 state["inventory"]
#             )
#
#     def handle_help():
#         print(
#             "Available commands:\n"
#             "- look around         : Examine the lab and your options."
#         )
#         if not got_keycard:
#             print(
#                 "- sneak              : Try to sneak past the zombies to get the Keycard\n."
#                 "- fight              : Fight the zombies.\n"
#                 "- fly away           : Attempt to fly away.\n"
#                 "- set the building on fire : Set the lab on fire.\n"
#                 "- go lobby           : Leave the lab and return to the lobby.\n"
#                 "- ?                  : Show this help message.\n"
#                 "- quit               : Quit the game."
#             )
#
#     def handle_sneak():
#         nonlocal got_keycard, room_cleared
#         if got_keycard:
#             print("You already have the Keycard. No need to sneak again.")
#             return None
#         print(
#             "You move quietly between the tables, holding your breath. The zombies don't notice you.\n"
#             "You grab the Keycard and slip out of their reach!"
#         )
#         state["inventory"].append("keycard")
#         got_keycard = True
#         room_cleared = True
#         return None
#
#     def handle_fight():
#         print("You try to fight the zombies, but they are stronger than you are. You get bitten. Game over.")
#         sys.exit()
#
#     def handle_fly():
#         print("You have no wings, so the zombies get you. Game over.")
#         sys.exit()
#
#     def handle_fire():
#         print("You set the building on fire, but you can't escape. The zombies vanish, but you die. Game over.")
#         sys.exit()
#
#     def handle_go(destination):
#         if destination == "lobby":
#             if got_keycard:
#                 print("You leave Lab 001 and go to the lobby, Keycard in hand.")
#             else:
#                 print("You leave Lab 001 and go to the lobby, but you didn't get the Keycard.")
#             return "corridor"
#         else:
#             print(f"❌ You can't go to '{destination}' from here.")
#             return None
#
#     # --- Main command loop ---
#     while True:
#         command = input("\n> ").strip().lower()
#
#         if command == "look around":
#             handle_look()
#
#         elif command == "?":
#             handle_help()
#
#         elif command == "sneak":
#             result = handle_sneak()
#             if result:
#                 return result
#
#         elif command == "fight":
#             handle_fight()
#
#         elif command == "fly away":
#             handle_fly()
#
#         elif command == "set the building on fire":
#             handle_fire()
#
#         elif command.startswith("go "):
#             destination = command[3:].strip()
#             result = handle_go(destination)
#             if result:
#                 return result
#
#         elif command == "quit":
#             print("👋 You run from the lab, leaving the adventure behind. Game over.")
#             sys.exit()
#
#         else:
#             print("❓ Unknown command. Type '?' to see available commands.")
#
# if __name__ == "__main__":
#     import copy
#
#     from main import state as main_state
#
#     state = copy.deepcopy(main_state)
#     enterLab001(state)


def lab2001(state):
    if state["rooms_visited"]["Lab2001"]:
        print("You have already seen this room")
        state["rooms_visited"]["Lab001"] = True
    else:
        print("you enter a room for the first time")


    print(
        "possible commands:\n"
        "look around\n"
        "go to lobby\n"
        "quit",
    )

    while True:
        user_input = input("> ")

        match user_input:
            case "look around":
                # print(
                #     "You enter Lab 001. The lights flicker on and off, making strange shadows on the walls.\n"
                #     "Tables are overturned, and zombies shuffle between them, their groans filling the silence.\n"
                #     "On a nearby desk, you spot a Keycard that could unlock electronic doors in the corridor.\n"
                #     "The zombies are too close for comfort, though. You'll have to be careful if you want to grab it without being noticed."
                # )
                #
                # userguess = input(
                #     "- sneak              : Try to sneak past the zombies to get the Keycard\n."
                #     "- fight              : Fight the zombies.\n"
                #     "- fly away           : Attempt to fly away.\n"
                #     "- set the building on fire : Set the lab on fire.\n"
                #     "- go lobby           : Leave the lab and return to the lobby.\n"
                #     "- ?                  : Show this help message.\n"
                #     "- quit               : Quit the game."
                # )
                #
                # while userguess != "sneak":
                #     userguess = input("Incorrect, try again!")
                #
                # print("Correct, You are sneaking in between the zombies and take the keycard!")
                #
                # state["current_room"] = "Lobby"
                # return

                print(
                    "You enter Lab 001. The lights flicker on and off, making strange shadows on the walls.\n"
                    "Tables are overturned, and zombies shuffle between them, their groans filling the silence.\n"
                    "On a nearby desk, you spot a Keycard that could unlock electronic doors in the corridor.\n"
                    "The zombies are too close for comfort, though. You'll have to be careful if you want to grab it without being noticed."
                )

                while True:
                    userguess = input(
                        "- sneak              : Try to sneak past the zombies to get the Keycard\n."
                        "- fight              : Fight the zombies.\n"
                        "- fly away           : Attempt to fly away.\n"
                        "- set the building on fire : Set the lab on fire.\n"
                        "- ?                  : Show this help message.\n"
                        "- quit               : Quit the game."
                    )

                    match userguess:
                        case "fight":
                            print("something fight")
                        case "fly away":
                            print("Something bad happend")
                        case "set the building on fire":
                            print("Nice, you died")
                        case "fly away":
                            state["go to lobby"] = "Lobby"
                            return
                        case "sneak":
                            print("You won")
                            break

            case "go to lobby":
                state["go to lobby"] = "Lobby"
                return

            case "quit":
                exit()


if __name__ == "__main__":
    import copy

    from main import state as main_state

    state = copy.deepcopy(main_state)
    lab2001(state)
