def get_user_input() -> list[str]:
    return input("> ").strip().split(" ")


def print_leaderboard() -> None:
    raise NotImplementedError


def print_stats() -> None:
    raise NotImplementedError


def quit_game() -> None:
    exit()


def pause_game() -> None:
    raise NotImplementedError
