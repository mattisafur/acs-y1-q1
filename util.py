import json
from datetime import datetime as DateTime
from datetime import timedelta as TimeDelta

from models import State


def get_user_input() -> list[str]:
    return input("> ").strip().split(" ")


def quit_game() -> None:
    exit()


def pause_game(state: State) -> None:
    state.time_played = update_time_played(state.time_played, state.session_start_time)
    save_data = {
        "player_name": state.player_name,
        "current_room": state.current_room,
        "inventory": state.inventory,
        "time_played": state.time_played.total_seconds(),
        "last_saved": DateTime.now().isoformat(),
    }
    saved_file_name = f"{state.player_name}_save.json"
    with open(saved_file_name, "w") as f:
        json.dump(save_data, f, indent=4)
    print(f"Game paused and saved successfully as '{saved_file_name}'.")
    quit_game()


def display_leaderboard() -> None:
    raise NotImplementedError


def display_stats(state: State) -> None:
        total_seconds = int(state.time_played.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        percentage = (len(state.rooms_visited) / len(state.all_rooms)) * 100 if state.all_rooms else 0

        print("Stats\n"
        "-----\n"
        f"Name: {state.player_name}\n"
        f"Time played: {hours}h{minutes}m\n"
        f"Rooms visited: {percentage:.0f}% ({len(state.rooms_visited)}/{len(state.all_rooms)})")


def display_inventory(state: State) -> None:
    print("Inventory:\n" + "\n".join(state.inventory))


def update_time_played(
    current_time_played: TimeDelta, session_start_time: DateTime
) -> TimeDelta:
    time_played_this_session = DateTime.now() - session_start_time
    return current_time_played + time_played_this_session


def display_go_list(rooms: list[str]) -> None:
    print("Connected rooms:\n", "\n".join(rooms))


def display_take_list(items: list[str]) -> None:
    print("Items available to pick up:\n" + "\n".join(items))


def display_invalid_command() -> None:
    print("Invalid command.")


def display_invalid_syntax(command_name: str) -> None:
    print(f"Invalid syntax\nUser `{command_name} ?` for help")


def display_go_help() -> None:
    print(
        "go <room name>|list\n"
        "Go to another room\n"
        "<room name>\n"
        "\tGo to the specified room\n"
        "list\n"
        "\tList connected rooms"
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
    print("inventory\nDisplay the items currently in your inventory")


def display_new_help() -> None:
    raise NotImplementedError


def display_load_help() -> None:
    raise NotImplementedError


def display_delete_help() -> None:
    raise NotImplementedError
