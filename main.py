from db import delete_save, load_save
from models import Command, State
from rooms.east_corridor import east_corridor
from rooms.lab_2001 import lab_2001
from rooms.lobby import lobby
from util import (
    display_delete_help,
    display_invalid_command,
    display_invalid_syntax,
    display_leaderboard,
    display_load_help,
    display_new_help,
    get_user_input,
    quit_game,
)

state = State.new_game("dummy_state")


def main_menu():
    while True:
        global state

        print("what would you like to do?")

        cmd, *args = get_user_input()

        match cmd:
            case Command.help:
                raise NotImplementedError
            case Command.new:
                if args != 1:
                    display_invalid_syntax("new")
                    continue

                if args[0] == "?":
                    display_new_help()
                    continue

                if load_save(args[0]) is not None:
                    print("a save with the specified name already exists")
                    continue

                state = State.new_game(args[0])

                print("starting new game")
                return
            case Command.load:
                if args != 1:
                    display_invalid_syntax("load")
                    continue

                if args[0] == "?":
                    display_load_help()
                    continue

                loaded_state = load_save(args[0])
                if loaded_state is None:
                    print("Save does not exist")
                    continue

                state = loaded_state

                print("save loaded, resuming game")
                return
            case Command.delete:
                if args != 1:
                    display_invalid_syntax("delete")
                    continue

                if args[0] == "?":
                    display_delete_help()
                    continue

                if load_save(args[0]) is None:
                    print("Save does not exist")
                    continue

                user_input = input("are you sure you want to delete the save? [y/N]: ")
                if user_input == "y":
                    delete_save(args[0])
                    print("save deleted")

                continue
            case Command.quit:
                quit_game()
            case Command.leaderboard:
                display_leaderboard()
                continue

        display_invalid_command()


main_menu()

while True:
    match state.current_room:
        case "main_menu":
            main_menu()
        case "lab_2001":
            lab_2001(state)
        case "east_corridor":
            east_corridor(state)
        case "lobby":
            lobby(state)
