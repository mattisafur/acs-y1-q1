import json
from datetime import datetime as DateTime
from datetime import timedelta as TimeDelta

from models import State


def get_user_input() -> list[str]:
    return input("> ").strip().split(" ")


def quit_game() -> None:
    print("Thank you for playing!")
    exit()


def pause_game(state: State) -> None:
    from db import save_state
    
    state.time_played = update_time_played(state.time_played, state.session_start_time)
    save_state(state)
    print(f"Game paused and saved as '{state.player_name}'.\n \n")
    print("To reload the game with your process use command load + username")
    quit_game()


def display_leaderboard() -> None:
    print("Leaderboard: \n")
    try:
        with open("leaderboard.txt", "r", encoding="utf-8") as f:
            lines = [ln.strip() for ln in f if ln.strip()]
    except FileNotFoundError:
        print("No records yet.")
        return
    if not lines:
        print("No records yet.")
        return
    for i, line in enumerate(lines[:10], 1):
        print(f"{i}. {line}")



def display_stats(state: State) -> None:
        total_seconds = int(state.time_played.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        percentage = (len(state.visited_rooms) / len(state.all_rooms)) * 100 if state.all_rooms else 0

        print("Stats\n"
        "-----\n"
        f"Name: {state.player_name}\n"
        f"Time played: {hours}h{minutes}m\n"
        f"Rooms visited: {percentage:.0f}% ({len(state.visited_rooms)}/{len(state.all_rooms)})")

def display_help() -> None:
    print(
        "Possible commands:\n"
        "look around       look around the room\n"
        "where              displays the room you are currently on\n"
        "take        pick up an item\n"
        "go          go to another room\n"
        "stats       display your stats\n"
        "leaderboard view the leaderboard\n"
        "pause       save and quit the game\n"
        "quit        quit the game without saving\n"
        "inventory   display the items in your inventory\n"
        "load + username        go back to the game after you paused"
    )

def display_inventory(state: State) -> None:
    print("Inventory:\n" + "\n".join(state.inventory))


def update_time_played(
    current_time_played: TimeDelta, session_start_time: DateTime
) -> TimeDelta:
    time_played_this_session = DateTime.now() - session_start_time
    return current_time_played + time_played_this_session


def display_go_list(rooms: list[str]) -> None:
    print("Rooms available:\n", "\n".join(rooms))
    print("Use command 'go' before typing your chosen room")

def display_take_list(items: list[str]) -> None:
    print("Items available to pick up:\n" + "\n".join(items))


def display_invalid_command() -> None:
    print("Invalid command.")


def display_invalid_syntax(command_name: str) -> None:
    print(f"Invalid syntax\nUser `{command_name} ?` for help")


def display_go_help() -> None:
    print(
        "go <room name>\n"
        "'go' should be typed before room name\n"
    )

def display_look_help() -> None:
    print("look\nlooks around the room and says what you see")


def display_take_help() -> None:
    print(
        "take <item>|list\n"
        "Pick up an item from the room and place it in your inventory\n"
        "<item>\n"
        "\tpick up the specified item\n"
        "list\n"
        "\tlist items possible to take"
    )


def display_answer_help() -> None:
    print("answer <answer>\nAnswer a challenge")


def display_inventory_help() -> None:
    print("inventory\nDisplay the items currently in your inventory\nTo access it type 'inventory'")


def display_new_help() -> None:
    print("New player <player name>\n"
          "New game\n"
          )


def display_load_help() -> None:
    print("load <save_name>")
    print("Load a saved game by username.")
    print("Username is the name you defined at the beginning of the game")
    print("Examples:")
    print("  load player 1")
    print("  load player 2")

def display_where_am_i(state: State) -> None:
    print(f"You are in {state.current_room}.")

def display_delete_help() -> None:
    print("Delete player <player name>\n"
        "Delete item <item> from your inventory\n"
        "Delete progress")
