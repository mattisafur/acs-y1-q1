from datetime import timedelta as TimeDelta, datetime as DateTime
from models import State


def get_user_input() -> list[str]:
    return input("> ").strip().split(" ")


def display_leaderboard() -> None:
    raise NotImplementedError


def display_stats() -> None:
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


def display_take_list(items: list[str]) -> None:
    raise NotImplementedError


def display_take_invalid_syntax() -> None:
    raise NotImplementedError


def display_answer_invalid_syntax() -> None:
    raise NotImplementedError


def display_invalid_command() -> None:
    print("Invalid command.")


def update_time_played(
    current_time_played: TimeDelta, session_start_time: DateTime
) -> TimeDelta:
    time_played_this_session = DateTime.now() - session_start_time
    return current_time_played + time_played_this_session
