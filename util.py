from datetime import datetime as DateTime
from datetime import timedelta as TimeDelta

from models import State


def get_user_input() -> list[str]:
    return input("> ").strip().split(" ")


def quit_game() -> None:
    exit()


def pause_game(state: State) -> None:
    raise NotImplementedError


def display_leaderboard() -> None:
    raise NotImplementedError


def display_stats(state: State) -> None:
    raise NotImplementedError


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
