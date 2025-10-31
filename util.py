from datetime import datetime as DateTime
from datetime import timedelta as TimeDelta

from models import State


def get_user_input() -> list[str]:
    user_input = input("> ").strip().split(" ")
    print("")
    return user_input


def display_map():
    print(
        "Map:\n"
        "Rooms available in East_corridor:\n"
        "lab_2001 | lab_2003  | lobby\n\n"
        "To access lab_2003: project_room_1 has to be visited first\n\n"
        "Rooms available in lobby:\n:"
        "north_corridor | east_corridor | project_room_1\n\n"
        "To access north_corrido: lab_2003 has to be visited first\n\n"
        "Rooms available in north_corridor:\n"
        "lobby| front_desk_office | equinox_students_society | storage_room | project_room_3\n",
        "teachers_room_3 | teachers_room_2 | teachers_room_1 | west_corridor\n\n"
        "Rooms available in west_corridor:\n"
        "stair_exit | classroom_2035 | classroom_2031 | north_corridor\n\n"
        "To enter stair_exit: storage_room has to be visited first\n",
    )


def display_items_list():
    print(
        "Pickable items in rooms:\n"
        "Keycard in room lab_2001 |  Knife in lab_2003 | Code in project_room_1  | Hammer in Storage_room  |  Masterkey in front_desk_office"
    )


def quit_game() -> None:
    exit()


def update_time_played(
    current_time_played: TimeDelta, session_start_time: DateTime
) -> TimeDelta:
    time_played_this_session = DateTime.now() - session_start_time
    return current_time_played + time_played_this_session


def track_time_played(state: State) -> None:
    state.time_played = update_time_played(state.time_played, state.session_start_time)
    state.session_start_time = DateTime.now()


def pause_game(state: State) -> None:
    from db import save_state

    track_time_played(state)
    save_state(state)
    print(f"Game paused and saved as '{state.player_name}'.\n \n")
    print("To reload the game with your process use command load + username")
    quit_game()


# FIXME WTFis going on here? this function is completely unrelated to the rest of the code, 100% AI generated and still completely wrong.
def display_leaderboard() -> None:
    from db import get_top_leaderboard

    print("Leaderboard:\n")

    entries = get_top_leaderboard(5)
    if not entries:
        print("No records yet.")
        return

    print(f"{'Rank':<5}{'Player':<18}{'Completion':<12}{'Time Played'}")
    print("-" * 55)

    for idx, entry in enumerate(entries, start=1):
        total_seconds = int(entry.play_time.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        print(f"{idx:<5}{entry.player_name:<18}{entry.completion:>6.0f}%      {hours}h{minutes}m")

def submit_leaderboard(state: State) -> None:
    from db import save_leaderboard
    from models import LeaderboardEntry
    total_time = update_time_played(state.time_played, state.session_start_time)
    total_rooms = len(get_all_rooms())
    completion = 0.0
    if total_rooms > 0:
        completion = (len(state.visited_rooms) / total_rooms) * 100.0
    entry = LeaderboardEntry(player_name=state.player_name, play_time=total_time, completion=completion)
    save_leaderboard(entry)


def display_stats(state: State) -> None:
    track_time_played(state)
    total_seconds = int(state.time_played.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    percentage = (len(state.visited_rooms) / len(get_all_rooms())) * 100
    print(
        "Stats\n"
        "-----\n"
        f"Name: {state.player_name}\n"
        f"Time played: {hours}h{minutes}m\n"
        f"Rooms visited: {percentage:.0f}% ({len(state.visited_rooms)}/{len(get_all_rooms())})"
    )


def get_all_rooms() -> list[str]:
    return [
        "lab_2001",
        "lobby",
        "project_room_1",
        "lab_2003",
        "storage_room",
        "front_desk",
        "teacher_room_3",
        "stairwell",
        "east_corridor",
        "west_corridor",
        "north_corridor",
    ]


def display_help() -> None:
    print(
        "Possible commands:\n"
        "map               displays all rooms and requisites to enter\n"
        "?                  display all possible commands\n"
        "look               explore the room\n"
        "where              displays the room you are currently on\n"
        "take        pick up an item\n"
        "go          go to another room\n"
        "stats       display your stats\n"
        "leaderboard view the leaderboard\n"
        "pause       save and quit the game\n"
        "quit        quit the game without saving\n"
        "items       display a list of all pickable available items\n"
        "inventory   display the items in your inventory\n"
        "load + username        go back to the game after you paused"
    )


def display_inventory(state: State) -> None:
    print("Inventory:\n" + "\n".join(state.inventory))


def display_go_list(rooms: list[str]) -> None:
    import textwrap

    room_line = "  |  ".join(room.lower() for room in rooms)
    wrapped_lines = textwrap.wrap(room_line, width=100)
    print("\nRooms available:\n")
    for line in wrapped_lines:
        print(line)
    print("\nUse command 'go' before typing your chosen room.")


def display_take_list(items: list[str]) -> None:
    print("Items available to pick up:\n" + "\n".join(items))


def display_invalid_command() -> None:
    print("Invalid command.")


def display_invalid_syntax(command_name: str) -> None:
    print(f"Invalid syntax\nUser `{command_name} ?` for help")


def display_go_help() -> None:
    print("go <room name>\n'go' should be typed before room name\n")


def display_look_help() -> None:
    print("look\nlooks around the room and says what you see")


def display_take_help() -> None:
    print(
        "take <item>\n"
        "Pick up an item from the room and place it in your inventory\n"
        "\tpick up the specified item\n"
        "\tlist items possible to take\n"
    )


def display_answer_help() -> None:
    print("answer <answer>\nAnswer a challenge")


def display_inventory_help() -> None:
    print(
        "inventory\nDisplay the items currently in your inventory\nTo access it type 'inventory'"
    )


def display_new_help() -> None:
    print("New player <player name>\nNew game\n")


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
    print(
        "Delete player <player name>\n"
        "Delete item <item> from your inventory\n"
        "Delete progress\n"
    )
