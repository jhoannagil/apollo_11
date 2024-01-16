import csv
from datetime import date, datetime, timedelta
import random

class Utils:
    

    def getMission():
        options = ["OrbitOne", "ColonyMoon", "VacMars", "GalaxyTwo", "Unknown"]
        random_mission = random.choice(options)
        return random_mission

    def getDeviceStatus():
        options = ["Excellent", "Good", "Warning", "Faulty", "Killed"]
        random_status = random.choice(options)
        return random_status

    def getDeviceType():
        options = ["Satellites", "Ships", "Suits", "Space vehicles"]
        random_device_type = random.choice(options)
        
        return random_device_type

    def getDate():
        date = datetime.now()
        formatdate = date.strftime("%d%m%Y%H%M%S")
        return formatdate

    def createSimulation(name):
        with open('./devices/'+name,'w',newline='') as file:
            writer = csv.writer(file)
            field = ["date", "mission", "device_type", "device_status", "hash"]
            
            writer.writerow(field)
        
    





   


