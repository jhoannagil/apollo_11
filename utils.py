from datetime import datetime
import random
from dataclasses import dataclass
from mission import Mission
import os

@dataclass
class Utils:

    def getHash(mission:Mission) ->str:
        if mission.name == "Unknown":
            return "unknown"
        else:
            return str(hash((mission.name, mission.date, mission.device_type, mission.device_status)))

    def getFileName(mission: Mission, fileNumber: int)-> str:
        return "APL[" + mission + "]-0" + "{:03d}".format(fileNumber) + ".log"

    def getReportName() ->str:
        return "APLSTATS-[REPORTE]-" + Utils.getDate() + ".log"

    def getMission()->str:
        options:list[str] = ["OrbitOne", "ColonyMoon", "VacMars", "GalaxyTwo", "Unknown"]
        random_mission: str = random.choice(options)
        return random_mission

    def getDeviceStatus()->str:
        options: list[str] = ["Excellent", "Good", "Warning", "Faulty", "Killed", "Unknown"]
        random_status :str = random.choice(options)
        return random_status

    def getDeviceType() ->str:
        options: list[str] = ["Satellites", "Ships", "Suits", "Space vehicles"]
        random_device_type :str = random.choice(options)

        return random_device_type

    def getDate() ->str:
        date :datetime = datetime.now()
        formatdate : str = date.strftime("%d%m%Y%H%M%S")
        return formatdate

    def createSimulation(name: str, mission:Mission)->None:
        try:
            os.makedirs("./Files/Devices")
        except FileExistsError:
            pass
        except FileNotFoundError:
            raise
        with open('./Files/Devices/'+name,'x',newline='') as file:
            file.write("date,mission,device_type,device_status,hash\n")
            file.write(mission.date+","+mission.name+","+mission.device_type+","+mission.device_status+","+Utils.getHash(mission)+"\n")
        
    def initDataEmpty():
        optionsMissions:list[str] = ["OrbitOne", "ColonyMoon", "VacMars", "GalaxyTwo", "Unknown"]
        optionsDevices: list[str] = ["Satellites", "Ships", "Suits", "Space vehicles", "Unknown"]
        listMissions = {}
        for mission in optionsMissions:
            listMissions[mission] = {}
            for device in optionsDevices:
                listMissions[mission][device] = []

        return listMissions

