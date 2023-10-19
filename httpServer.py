#Required for HTTP server
from http.server import HTTPServer, BaseHTTPRequestHandler
#Required for Phidgets
from Phidget22.Phidget import *
from Phidget22.Devices.RCServo import *
#Required for sleep statement
import time
#Required for the use of threads
import threading
import codecs
import os

#Global variable
global active
active = False
#Class to use in the thread
def myServer():
    #Class to hadle HTTP requests
    class MyHandler(BaseHTTPRequestHandler):

        def do_POST(self):
            global active
            active = False
            print(active)
            
            myText = "Hola mundo, como estas hoy?"
            
            content_len = int(self.headers.get('content-Length'))
            post_body = self.rfile.read(content_len)
            print(post_body)
            myText = codecs.decode(post_body, "UTF-8")
            print(myText)
            print("espeak -v es '" + myText + "'")
            
            os.system("espeak -v es '" + myText + "'")

            self.send_response(200)
            self.end_headers()
            if active :
                self.wfile.write(bytes("True", "utf-8"))
            else:
                self.wfile.write(bytes("False", "utf-8"))
            
    httpd = HTTPServer(("192.168.3.53", 8080), MyHandler)
    httpd.serve_forever()
    
#Create Servo controller
servoController = RCServo()

#Open
servoController.openWaitForAttachment(1000)

#Start thread
thread = threading.Thread(target = myServer)
thread.start()

while True:
    if active:
        #Set a target position
        servoController.setTargetPosition(0)

        #Engage the motor controller
        servoController.setEngaged(True)
    
        time.sleep(1.0)
       
        #Set a target position
        servoController.setTargetPosition(180)

        #Engage the motor controller
        servoController.setEngaged(True)
        time.sleep(1.0)
        
    else :
        servoController.setEngaged(False)