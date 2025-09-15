# Teacher Room (Room 6) - Illia
import sys

def enterTeachersRoom(state):
    print(
        "You step into the teacher’s lounge. Papers are scattered, coffee mugs still half full. "
        "A bookshelf is tilted, blocking part of the exit. On the desk you see four folders labeled A, B, C, D with notes stuck to them. "
        "A whiteboard says: ‘Put knowledge in the right order. Only then the truth is revealed.’"
    )
    found_code = "exit code" in state["inventory"]
    puzzle_solved = found_code

    def handle_look():
        print(
            "The teacher’s lounge is a mess. The bookshelf looks unstable.\n"
            "On the desk are four folders labeled A, B, C, D. Each has a note:\n"
            "Folder A: ‘Comes after B.’\n"
            "Folder B: ‘Must be first.’\n"
            "Folder C: ‘Is never next to A.’\n"
            "Folder D: ‘Always after C.’\n"
            "A whiteboard reads: ‘Put knowledge in the right order. Only then the truth is revealed.’"
        )
        if found_code:
            print("You already have the Exit Code. The room is quiet now.\n"
            "- Possible exits: corridor\n"
            "- Your current inventory:", state["inventory"],
                  )

    def handle_help():
        print("Available commands:\n "
        "- look around         : Examine the lounge and clues.\n"
        "- arrange <order>     : Arrange the folders in the order you think is correct. Example: arrange B C D A\n"
        "- go corridor         : Leave the teacher's lounge and return to the corridor.\n"
        "- ?                  : Show this help message.\n"
        "- quit               : Quit the game.\n")

    def handle_arrange(order):
        nonlocal found_code, puzzle_solved
        correct = ["b", "c", "d", "a"]
        attempt = [x.lower() for x in order.split()]
        if attempt == correct:
            print("The folders click into place like a code lock. Inside the last folder is a torn page with the Exit Code written in red marker.")
            state["inventory"].append("exit code")
            found_code = True
            puzzle_solved = True
        else:
            print("The shelf tips and crashes loudly. The sound echoes down the corridor, and you flee empty-handed.")
            return "corridor"
        return None

    def handle_go(destination):
        if destination == "corridor":
            print("You leave the teacher's lounge and return to the corridor.")
            return "corridor"
        else:
            print(f"❌ You can't go to '{destination}' from here.")
            return None

    while True:
        command = input("\n> ").strip().lower()
        match command:
            case "look around":
                handle_look()
            case "?":
                handle_help()
            case "quit":
                exit()
        elif command.startswith("arrange "):
            order = command[len("arrange "):].strip()
            result = handle_arrange(order)
            if result:
                return result
        elif command.startswith("go "):
            destination = command[3:].strip()
            result = handle_go(destination)
            if result:
                return result
        elif case == "quit":
            print("👋 You leave the teacher's lounge. Game over.")
            exit()
        else:
            print("❓ Unknown command. Type '?' to see available commands.")

if __name__ == "__main__":
    import copy

    from main import state as main_state

    state = copy.deepcopy(main_state)
    enterTeachersRoom(state)
