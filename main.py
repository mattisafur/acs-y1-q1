from db import delete_state, initialize_database, load_state, save_state
from models import Command, State
from rooms.east_corridor import east_corridor
from rooms.front_desk_office import front_desk_office
from rooms.lab_2001 import lab_2001
from rooms.lab_2003 import lab_2003
from rooms.lobby import lobby
from rooms.north_corridor import north_corridor
from rooms.project_room_1 import project_room_1
from rooms.stair_exit import stair_exit
from rooms.storage_room import storage_room
from rooms.teacher_room_3 import teacher_room_3
from rooms.west_corridor import west_corridor
from util import (
    display_delete_help,
    display_invalid_command,
    display_invalid_syntax,
    display_leaderboard,
    display_load_help,
    display_new_help,
    display_help,
    display_where_am_i,
    get_user_input,
    quit_game,
)

state = State.new_game("dummy_state")

initialize_database()


def main_menu():
    global state
    print("Welcome. Just some useful information before you start:\n"
          "To start new game, type 'new' + How you like to be called.\n"
          "Example: new Johnson\n"
          "To resume the game from the pause, type 'load' + username you want to load.\n"
          "Example: load Johnson\n"
          "To quit the game, type 'quit'.\n"
          "Type '?' to display all possible commands during the game.\n"
          "Use command 'look around' to explore inside of the rooms.\n"
          "What would you like to do?")

    while True:

        cmd, *args = get_user_input()

        match cmd:
            case Command.help:
                display_help()
            case Command.new:
                if len(args) != 1:
                    display_invalid_syntax("new")
                    continue
                if args[0] == "?":
                    display_new_help()
                    continue
                if load_state(args[0]) is not None:
                    print("a save with the specified name already exists")
                    continue
                state = State.new_game(args[0])
                save_state(state)
                print("starting new game")
                return
            case Command.load:
                if len(args) != 1:
                    display_invalid_syntax("load")
                    continue
                if args[0] == "?":
                    display_load_help()
                    continue
                loaded_state = load_state(args[0])
                if loaded_state is None:
                    print("Save does not exist")
                    continue
                state = loaded_state
                print("save loaded, resuming game")
                return
            case Command.delete:
                if len(args) != 1:
                    display_invalid_syntax("delete")
                    continue
                if args[0] == "?":
                    display_delete_help()
                    continue
                if load_state(args[0]) is None:
                    print("Save does not exist")
                    continue
                user_input = input("are you sure you want to delete the save? [y/N]: ")
                if user_input == "y":
                    delete_state(args[0])
                    print("save deleted")
                continue
            case Command.where:
                display_where_am_i(state)
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
            state = lab_2001(state)
        case "east_corridor":
            state = east_corridor(state)
        case "lobby":
            state = lobby(state)
        case "front_desk_office":
            state = front_desk_office(state)
        case "lab_2003":
            state = lab_2003(state)
        case "north_corridor":
            state = north_corridor(state)
        case "project_room_1":
            state = project_room_1(state)
        case "stair_exit":
            state = stair_exit(state)
        case "storage_room":
            state = storage_room(state)
        case "teacher_room_3":
            state = teacher_room_3(state)
        case "west_corridor":
            state = west_corridor(state)
