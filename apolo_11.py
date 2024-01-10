import csv
from datetime import date, datetime, timedelta
import random

def getMission():
    options = ["OrbitOne", "ColonyMoon", "VacMars", "GalaxyTwo", "Unknown"]
    random_mission = random.choice(options)
    print(random_mission)
    return random_mission

def getStatus():
    options = ["Excellent", "Good", "Warning", "Faulty", "Killed"]
    random_status = random.choice(options)
    print(random_status)
    return random_status

def getDeviceType():
    options = ["Satellites", "Ships", "Suits", "Space vehicles"]
    random_device_type = random.choice(options)
    print(random_device_type)
    return random_device_type

def getDate():
    date = datetime.now()
    formatdate = date.strftime("%d%m%Y%H%M%S")
    print(formatdate)
    return formatdate

def createReport(name):
    with open('./devices/'+name,'w',newline='') as file:
        writer = csv.writer(file)
        field = ["date", "mission", "device_type", "device_status", "hash"]
        
        writer.writerow(field)
     



def apolo11():

    print("Bienvenidos Apolo 11:\n")
    print("Ejecutar mision:\n")
    print("1-OrbitOne\n")
    print("2-ColonyMoon\n")
    print("3-VacMars:\n")
    print("4-GalaxyTwo\n")

    mision = input ()
    if mision == "1" :
        print ("Usted a ingresado a la  mision OrbitOne")

    if mision == "2":
        print ("Usted a ingresado a la  mision ColonyMoon")

    if mision == "3":
        
        print ("Usted a ingresado a la  mision VacMars")
        createReport('APL[TMRS]-0001')

    if  mision == "4":
        print ("Usted a ingresado a la mision GalaxyTwo")

    status= getStatus()
    device=getDeviceType()
    date=getDate()
    mission=getMission()





apolo11()


