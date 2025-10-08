# def lab_2003(state:State):
#     print(
#         "You just enter the Computer Lab 2003.\n"
#         "There is just one computer on. On the screen it displays:\n"
#         "“Login required – Insert authorized password.”\n"
#         "You must type something in. You decide to type: \n"
#     )
#
#     while True:
#        print(
#             "Code from Project room\n"
#             "Goodbye letter\n"
#             "Type mom's number\n"
#             "Positive affirmations\n"
#         )
#         choice = get_user_input()
#
#         match choice:
#             case "Code from Project room":
#                 code = input("You carefully type in: ")
#                 if code == "72946":
#                     print(
#                         "After a short pause, the screen unlocks. The computer has a document opened.\n"
#                         "One line sparks your attention:\n"
#                         "'Tools can be found at the top left of the cabinet'\n"
#                         "You start to look for it, and find a knife"
#                     )
#                     # knife collect and add inventory
#                     state["current_room"] = "east_corridor"
#                     return
#
#                 else:
#                     print("Computer displays: 'Incorrect password!'\n")
#                     state["current_room"] = "lab_2003"
#                     return
#
#             case "Goodbye letter":
#                 print(
#                     "Your hands are shaking, you breath roughly you feel sweat over your face.\n"
#                     "You are so afraid of the zombies, that you decide to save your last words on earth in the school's computer.\n"
#                 )
#                 last_words = input("The space is short, so you briefly write your goodbye words: ")
#                 print(
#                     "You leave the room desperate and anxious, and without thinking, decides to bite up a zombie from behind\n"
#                     "The zombie bites you back, and you bleed to death in East Corridor\n"
#                     f"{last_words} you may rest in peace"
#                 )
#                 return
#
#             case "Type mom's number":
#                 print("As a instinct, you decide to type your mom's number:")
#                 mom_number = input(" ")
#                 print(
#                     "The screen displays 'Incorrect password' and you cry a lot.\n"
#                     "You start to feel thirsty from so many water you lost on your tears, so you start to look for something to drink\n"
#                     "You spot a glass on the table and decide to drink it.\n"
#                     "It is not water.\n"
#                     "It is the potion that transformed all the students in zombies.\n"
#                     "Now, you are one of them.\n\n"
#                     "You lost the game.\n"
#                     "It is not allowed to become a zombie"
#                 )
#                 return
#
#             case "Positive affirmations":
#                 print(
#                     "Not thinking the computer would be useful, you start to write positive affirmations as a manifestation to the universe.\n"
#                     "You believe this way, things will get better.\n"
#                     "Things don't get better, so you just leave the room, but now with a optimistic mindset."
#                 )
#                 state["current_room"] = "east_corridor"
#                 return
#             case _:
#                    print("Invalid choice")
#
#
#
# lab_2003(State)
