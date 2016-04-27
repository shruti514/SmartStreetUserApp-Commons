# -*- coding: utf-8 -*-
# Connects to Parse Database and save the count when object detected



#Import Libraries
import RPi.GPIO as GPIO
import time
import json 
import httplib


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)



try:        
       
        while True:
#Parse Database connection       
                connection = httplib.HTTPSConnection('api.parse.com', 443)
                connection.connect()
                

#Read input from sensor       
                inp = GPIO.input(PIR_PIN)
                print(inp)
                if inp==1:
                    payload = {'Count':1}
                    connection.request('POST', '/1/classes/ProximitySensorRecord', json.dumps(payload), { "X-Parse-Application-Id": "pQCx3CjwJTZgOfoWjrkdAGdKqAxBoXJoSVbltkeB","X-Parse-REST-API-Key": "iITWf0dW7MbLy3hv5LwgoQaiIEluK5lfh4apdgDr"})
                    result = json.loads(connection.getresponse().read())
                    print result
                time.sleep(5)
             
            
except KeyboardInterrupt:
        print "Quit"
        GPIO.cleanup()

