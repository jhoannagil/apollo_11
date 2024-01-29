from mission import Mission
from utils import Utils
from report import Report
import time

cicle: int = 1
nextCicle: bool = True
date: str = Utils.getDate()

while nextCicle == True:
    fileNumber: int = 0
    numFiles: int = 0
    listMissions = Utils.initDataEmpty()
    flag: bool = False
   
    #Validation value input is int
    while flag == False or numFiles > 100:
        try:
            print("Ingrese simulaciones a realizar en el ciclo #"+str(cicle)+": (max 100)")
            maxFiles: str = input()
            numFiles = int(maxFiles)
            flag = True
        except ValueError:
            flag = False

    #Creation files
    while fileNumber < numFiles:
        try:
            fileNumber += 1

            nameMission: str = Utils.getMission()
            codeMission: str = ""
            if nameMission == "OrbitOne":
                codeMission = "ORBONE"
            elif nameMission == "ColonyMoon":
                codeMission = "CLM"
            elif nameMission == "VacMars":
                codeMission = "TMRS"
            elif nameMission == "GalaxyTwo":
                codeMission = "GALXONE"
            else:
                codeMission = "UNKN"

            mission: Mission = Mission()
            mission.name = nameMission
            mission.date = Utils.getDate()
            if codeMission == "UNKN":
                mission.device_status = "Unknowwn"
                mission.device_type = "Unknown"
            else:
                mission.device_status = Utils.getDeviceStatus()
                mission.device_type = Utils.getDeviceType()


            listMissions[mission.name][mission.device_type].append(mission.device_status)
            fileName: str = Utils.getFileName(codeMission, fileNumber)
            Utils.createSimulation(fileName, mission)
        except Exception as error:
            raise

    Report.GenerateReports(cicle, numFiles, date, listMissions)
    
    flag = False
    time.sleep(20)
    #Validation continue execution simulations
    while flag == False:
        try:
            print("¿Deseas continuar con las simulaciones?")
            print("1- CONTINUAR")
            print("0- SALIR")
            option: str = input()
            flag = True
            if option == "0":
                nextCicle = False
            if option == "1":
                cicle += 1
        except ValueError:
            flag = False
    
    