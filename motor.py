#Add Phidget Library

from Phidget22.Phidget import *
from Phidget22.Devices.RCServo import *
#Required for sleep statement
import time

#Create
servoController = RCServo()

#Open
servoController.openWaitForAttachment(1000)

degree = int(input("Introduzca el grado del servo: "))

servoController.setTargetPosition(degree)

#Engage the motor controller
servoController.setEngaged(True)

time.sleep(1.0)

i = 0
while i < 5:
    
    degree = int(input("Introduzca el grado del servo: "))
    
    #Set a target position
    servoController.setTargetPosition(degree)

    #Engage the motor controller
    servoController.setEngaged(True)
    
    i += 1
    
    time.sleep(1.0)

servoController.setEngaged(False)
