from datetime import timedelta as TimeDelta

from models import State
from rooms.east_corridor import east_corridor
from rooms.front_desk_office import front_desk_office
from rooms.lab_2001 import lab_2001
from rooms.lab_2003 import lab_2003
from rooms.north_corridor import north_corridor
from rooms.project_room_1 import project_room_1
from rooms.teacher_room_3 import teacher_room_3
from rooms.west_corridor import west_corridor

state: State = State(
    current_room="main_menu",
    inventory=[],
    previous_room="",
    time_played=TimeDelta(),
    user_name="",
    visited_rooms=[],
)


def main_menu():
    # load state into global variable
    ...


while True:
    match state.current_room:
        case "main_menu":
            main_menu()
        case "east_corridor":
            east_corridor(state)
        case "front_desk_office":
            front_desk_office(state)
        case "lab_2001":
            lab_2001(state)
        case "lab_2003":
            lab_2003(state)
        case "north_corridor":
            north_corridor(state)
        case "project_room_1":
            project_room_1(state)
        case "teacher_room_3":
            teacher_room_3(state)
        case "west_corridor":
            west_corridor(state)
