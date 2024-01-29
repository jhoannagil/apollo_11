from utils import Utils
from dataclasses import dataclass
import csv
import os
import shutil

@dataclass
class Report:

    def GenerateReports(cicle: int, quantityMissions: int, date: str,listMissions: dict) -> None:
        reportName:str = Utils.getReportName()
        Report.generateReportEvents(cicle, reportName, date,listMissions)
        Report.generateReportDisconnection(cicle, reportName, date,listMissions)
        Report.generateReportKilled(cicle, reportName, date,listMissions)
        Report.generateReportPercentage(cicle, quantityMissions, reportName, date, listMissions)
        Report.generateBackup(cicle, date)

    def generateReportEvents(cicle: int, reportName: str, date: str,listMissions: dict) -> None:
        status: list[str] = ["Excellent", "Good", "Warning", "Faulty", "Killed", "Unknown"]
        try:
            os.makedirs("./Files/Reports/"+date+"/Cicle-"+str(cicle))
        except FileExistsError:
            pass
        with open('./Files/Reports/'+date+'/Cicle-'+str(cicle)+"/"+reportName,'x',newline='') as file:
            file.write("***analisis de la cantidad de eventos por estado para cada misión y dispositivo***\n")
            file.write("mission,device_type,device_status,quantity\n")
            for missionName, devicesType in listMissions.items():
                for device, devicesStatus in devicesType.items():
                    for state in status:
                        file.write(missionName+","+device+","+ state+","+ str(devicesStatus.count(state))+"\n")

    def generateReportDisconnection(cicle: int, reportName: str, date: str, listMissions: dict):
        with open('./Files/Reports/'+date+'/Cicle-'+str(cicle)+"/"+reportName,'a') as file:
            file.write("***analisis de la cantidad de desconexiones por dispositivo y misión***\n")
            for missionName, devicesType in listMissions.items():
                for device, devicesStatus in devicesType.items():
                    quantity :int = devicesStatus.count("Unknown")
                    if device != "Unknown" and quantity != 0:
                        file.write("Para la misión " + missionName + " y el dispositivo " + device + " se presento " + str(quantity) + " desconexion(es)\n")

    def generateReportKilled(cicle: int, reportName: str, date: str, listMissions: dict):
        with open('./Files/Reports/'+date+'/Cicle-'+str(cicle)+"/"+reportName,'a') as file:
            file.write("***análisis de la cantidad de dispositivos inoperables***\n")
            totalMissions : int = 0
            for missionName, devicesType in listMissions.items():
                totalKilled: int = 0
                for _, devicesStatus in devicesType.items():
                    totalKilled = totalKilled + devicesStatus.count("Killed")
                totalMissions = totalMissions + totalKilled
                file.write("El total de dispositivos inoperables  para la mision "+missionName+" es: " + str(totalKilled) + "\n")
            file.write("El total de dispositivos inoperables es: " + str(totalMissions) + "\n")
    
    def generateReportPercentage(cicle: int, quantityMissions:int, reportName: str, date: str, listMissions: dict):
        with open('./Files/Reports/'+date+'/Cicle-'+str(cicle)+"/"+reportName,'a') as file:
            file.write("***análisis de la cantidad de dispositivos inoperables***\n")
            for missionName, devicesType in listMissions.items():
                for device, devicesStatus in devicesType.items():
                    totalPercentaje: float = (len(devicesStatus) / quantityMissions) * 100
                    file.write("Se generaron "+str(totalPercentaje)+"% del total de datos para el dispositivo "+device+" y la mision "+missionName+"\n")

    # Backup en que estamos moviendo los archivos generados en la simulacion
    def generateBackup(cicle: int, date: str) -> None:
        try:
            listFiles:list[str] = os.listdir("./Files/Devices")
            dateBackup:str = Utils.getDate()
            os.makedirs("./Files/Backups/"+date+"/Cicle-"+str(cicle))
            for _, fileName in enumerate(listFiles):
                shutil.move("./Files/Devices/"+fileName, "./Files/Backups/"+date+"/Cicle-"+str(cicle)+"/"+fileName)
        except FileNotFoundError:
            raise
        except FileExistsError:
            print("File exists")
        except OSError:
            raise

                