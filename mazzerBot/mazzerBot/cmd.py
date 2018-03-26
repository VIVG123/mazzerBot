
# vivek123
# Marmik
# MayankSingh #Dyknoww

import time as t #For delay and all
import RPi.GPIO as g #to use gpio
import json  #to convert data in dictionary
import requests as r #to fetch data from a site

g.setmode(g.BOARD)
g.setwarnings(False)
# right forward  wheel 
g.setup(29,g.OUT)
# right backward wheel
g.setup(31,g.OUT)
# left backward wheel
g.setup(33,g.OUT)
# left  forward wheel
g.setup(35,g.OUT)

while(1):
	data = r.get("https://api.thingspeak.com/channels/458106/feeds.json?api_key=XQ037NVAG71W4PWA&results=2")
	dict = data.json()
	for x in range(1):
		x = int(dict['feeds'][1]['field1'][1])
		y = int(dict['feeds'][1]['field1'][2])
		z = int(dict['feeds'][1]['field1'][3])
		p = dict['feeds'][1]['field1'][5]
		k =  z + y*10 +x*100
	print("dist " + str(k)+ " dir " + p)


	#for going forward	
	if p=="f":
		g.output(29,g.HIGH)
		g.output(35,g.HIGH)
		g.output(31,g.LOW)
		g.output(33,g.LOW)
		print("Going Forward")
	#for going backward
	elif p=="b":
		g.output(29,g.LOW)
		g.output(35,g.LOW)
		g.output(31,g.HIGH)
		g.output(33,g.HIGH)
		print("Going Backward")
	#for going right
	elif p=="r":
		g.output(29,g.LOW)
		g.output(31,g.LOW)
		g.output(35,g.HIGH)
		g.output(33,g.LOW)
		print("Going Right")
	#for going left
	elif p=="l":
		g.output(29,g.HIGH)
        	g.output(35,g.LOW)
        	g.output(31,g.LOW)
        	g.output(33,g.LOW)
		print ("Going Left")
