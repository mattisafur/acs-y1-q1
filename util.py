from types import NotImplementedType
from models import State


def get_user_input() -> list[str]:
    return input("> ").strip().split(" ")


def print_leaderboard() -> None:
    raise NotImplementedError


def print_stats() -> None:
    raise NotImplementedError


def quit_game() -> None:
    exit()


def pause_game(state: State) -> None:
    raise NotImplementedError


def display_inventory(state: State) -> None:
    raise NotImplementedError


def display_go_help() -> None:
    print(
        "go <room name>|list\n"
        "Go to another room\n"
        "<room name>\n"
        "\tGo to the specified room\n"
        "list\n"
        "\tList connected rooms"
    )


def display_go_list(rooms: list[str]) -> None:
    print("Connected rooms:\n", "\n".join(rooms))


def display_go_invalid_syntax() -> None:
    print("Invalid syntax\nUse `go ?` for help")


def display_take_help() -> None:
    raise NotImplementedError


def display_take_invalid_syntax() -> None:
    raise NotImplementedError
