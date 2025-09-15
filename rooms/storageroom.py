def enterStorageroom(state):
    print("\n You step into the Storage room. ")
    print(
        " \n You can barely see anything. \n To your left you see a table flipped over. \n To your right you see a very big cabinet. ")
    print(" \n In front of you you see a pathway made by fallen debris, flipped tables and chairs. ")
    print(
        "Which option would you like to explore? \n a Move a few steps forward and explore the maze created by the debris. ")
    print(
        "b Try to move past the big cabinet. \n c Leave the room. \n d See if you can move past the table to your left. ")
    correct_answer = ""
    while user_answer != correct_answer:

    user_choice = input("\n Enter your choice: ")
    if user_choice == "a":
        (print("You move forward and see the pathway splitting up 2 different paths. One to your right and one to the left."))
        user_choice2 = input(" \n a to choose the path on the left \n a to choose the path on the right. \n ")
        if user_choice2 == "a":
            print("You walk on the path on the left and get surprised by a zombie. You run to the other path, but presented with 2 more paths you fail you to choose fast enough and get killed by the zombie. ")

          #code end room phase and bring player back to the previous room
        elif user_choice2 == "b":
            print("You walk on the path to the right and once again get presented with 2 choice")
            user_choice3 = input(" \n a to go on the path to the left. \n b to go on the path to the right.\n ")
            if user_choice3 == "a":
                print("You walk onto the path to the left and stumble onto a door handle. You remember this handle. Its the door handle for the emergency exit. ")
                #code to pick up door handle and add it to inventory.
                print("You exited the Storage room.")
            elif user_choice3 == "b":
                print("You walk onto the path on the right and get jumpscared by a zombie that instantly bites you. \n")
                #code end room phase and bring player back to the previous room

    elif user_choice =="b":
        print("You try to push past the big cabinet. With no success you reconsider your options")

if __name__ == "__main__":
    import copy

    from main import state as main_state

    state = copy.deepcopy(main_state)
    enterStorageroom(state)
