print("You enter the stairwell, and thick, greenish virus smoke fills the space.\n"
    "The acrid fumes make it hard to breathe, and the groans of zombies echo from below.\n"
    "The upper floors are blocked by debris, leaving no other route.\n"
    "You must find a way to pass the smoke in order to leave the building.\n")


print("A) Use the Keycard found at the front office as a makeshift respirator over your nose and mouth to sneak through the smoke.\n"
      "B) Rush through the smoke without any protection.\n"
      "C) Try to force open the blocked doors to create another route.\n"
      "D) Go back to the previous corridor.")

choice = input("What is your next action?")

if choice == "A":
    print("You press the keycard tightly over your nose and mouth, the plastic shielding you from the worst of the fumes\n"
          "The groans below grow louder, but you stay low, moving past the thickest clouds.\n"
          "At the far end of the stairwell, you stumble into a service landing with a heavy steel door.\n"
          "It is the emergency exit!\n"
          "You are close to escape the building")
elif choice == "B":
    print("You rush straight into the thick smoke, your lungs are burning.")
    life = 3 #3 chances to escape the smoke

    while life > 0:
        print(f"You have three chances to escape the smoke. You currently have {life} left.")
        print("1) Keep pushing forward blindly.\n"
              "2) Drop low to the ground to find cleaner air.\n"
              "3) Search around in the smoke for something useful.")
        action = input("What do you do? ")
        if action == "1":
            life -= 1
            print(" You stumble blindly, coughing harder. Your strength fades\n"
                  "You fall into the floor unconsciously")
        elif action == "2":
            print("You drop low and breathe slightly cleaner air.\n"
             "Through the haze, you spot the emergency exit door ahead!")
            break
        elif action == "3":
            print("You find a broken gas mask on the floor! With it, you push forward and survive the smoke.\n")
            break
        else:
            print("You hesitate for too long. You fall on the floor unconsciously.")
    if life <= 0 :
        print("The smoke overwhelms you. Your vision fades to black. Game Over.")
    elif choice == "C" :
        print("You try to force the blocked doors, but the noise draws zombies closer.\n"
              "The smoke thickens around you. It’s too late. Game Over.")
    elif choice == "D" :
        print("You retreat back into the corridor, safe for now. But the stairwell still blocks your escape.")