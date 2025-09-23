from datetime import datetime


def print_stats(state):
    print(
        "Stats:\n"
        f"Name - {state["player_name"]}\n"
        f"Time played - {datetime.now() - state["start_time"]}\n"
        f"Percentage of rooms visited - {sum(state["rooms_visited"].values()) / len(state["rooms_visited"])}"
    )
