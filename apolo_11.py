from mission import Mission
from utils import Utils

maxFiles = 1
files = 0
while files < maxFiles:
    files++
    obj = Mission(Utils.getMission(), Utils.getDate(), Utils.getDeviceType(), Utils.getDeviceStatus())
    mission = ""
    
    if obj.name == "OrbitOne":
        mission = "ORBONE"
    elif obj.name == "ColonyMoon":
        mission = "CLM"
    elif obj.name == "VacMars":
        mission = "TMRS"
    elif obj.name == "GalaxyTwo":
        mission = "GALXONE"
    else:
        mission = "UNKN"
