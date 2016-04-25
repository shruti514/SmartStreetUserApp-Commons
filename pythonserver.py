# -*- coding: utf-8 -*-
# Connects to Parse Database and check the status 
# If true Lights on else swiftch off

#Import Libraries
import json 
import httplib
import RPi.GPIO as GPIO
import time

while True:
#Connect to parse
        connection = httplib.HTTPSConnection('api.parse.com', 443)
#connection =  httplib.HTTPSConnection('api.parse.com', 443)
        connection.connect()
        connection.request('GET', '/1/classes/Interaction/KHTyejPc8j', '', { "X-Parse-Application-Id": "pQCx3CjwJTZgOfoWjrkdAGdKqAxBoXJoSVbltkeB","X-Parse-REST-API-Key": "iITWf0dW7MbLy3hv5LwgoQaiIEluK5lfh4apdgDr"})
        result = json.loads(connection.getresponse().read())

#Get status and perform action
#print "the Result of :",result
        status = result[u'status']
        print status

#Send signal to port 18 of raspberry pi to switch on LED

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18,GPIO.OUT)
#status = False
        if status==True :
                GPIO.output(18,GPIO.HIGH)
        	print "Lights On"
                time.sleep(2)
        else:
                GPIO.output(18,GPIO.LOW)
                print "Lights Off"
                time.sleep(2)
	
