from datetime import datetime

from rooms.eastcorridor import eastcorridor
from rooms.frontdeskoffice import frontdeskoffice
from rooms.lab2003 import lab2003
from rooms.northcorridor import northcorridor
from rooms.projectroom1 import projectroom1
from rooms.stairexit import stairexit
from rooms.storageroom import storageroom
from rooms.teachersroom4 import teachersroom4
from rooms.lab2001 import lab2001
from rooms.lobby import lobby
from rooms.westcorridor import westcorridor

# state dictionary
state = {
    "current_room": "Lab2001",
    "rooms_visited": {
        "Lab2001": False,
        "EastCorridor": False,
        "Lab2003": False,
        "Lobby": False,
        "ProjectRoom1": False,
        "NorthCorridor": False,
        "FrontDeskOffice": False,
        "TeachersRoom4": False,
        "Storage": False,
        "WestCorridor": False,
        "StairExit": False,
    },
    "inventory": {
        "Map": False,
        "MasterKey": False,
        "Keycard": False,
        "Handle": False,
        "Jacket": False,
        "Passcode": False
    },
    "player_name": "not implemented",
    "start_time": datetime.now(),
}

if __name__ == "__main__":
    # main loop
    while True:
        match state["current_room"]:
            case "Lab2001":
                lab2001(state)
            case "EastCorridor":
                eastcorridor(state)
            case "Lab2003":
                lab2003(state)
            case "Lobby":
                lobby(state)
            case "ProjectRoom1":
                projectroom1(state)
            case "NorthCorridor":
                northcorridor(state)
            case "FrontDeskOffice":
                frontdeskoffice(state)
            case "TeachersRoom4":
                teachersroom4(state)
            case "Storage":
                storageroom(state)
            case "WestCorridor":
                westcorridor(state)
            case "StairExit":
                stairexit(state)
            case "TeachersRoom4":
                teachersroom4(state)
