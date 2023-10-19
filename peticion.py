#importacion de librerias
from Phidget22.Phidget import *
from Phidget22.Devices.RCServo import *
import time
import requests
import threading

URL = "http://192.168.100.12:8070/getActuador/1"
global activo
activo = False

def http_request():
    global activo
    while True:
        time.sleep(4)
        response = requests.get(url = URL)
        data = response.json()
        activo = data["activo"]
        #print("thread: ", activo)
        
thread = threading.Thread(target = http_request)
thread.start()

#Create
servoController = RCServo()

#Open
servoController.openWaitForAttachment(1000)
response = requests.get(url = URL)
data = response.json()
activo = data["activo"]

while(True):

    #print("while loop: ", activo)
    time.sleep(1)
    if(activo):
        servoController.setTargetPosition(0)
        servoController.setEngaged(True)
        time.sleep(2)
        servoController.setTargetPosition(180)
        servoController.setEngaged(True)
    else:
        servoController.setEngaged(False)
            
    