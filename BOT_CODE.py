# vivekGusain

# MarmikSharma #MaxDevilio

# MayankSingh #Dyknoww



import time as t #For delay and all

import RPi.GPIO as g #to use gpio

import json  #to convert data in dictionary

import requests as r #to fetch data from a site



Trig = 24

Echo = 23

stopa = 0





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

#Trig

g.setup(Trig,g.OUT)

#Echo

g.setup(Echo,g.IN)



arr=[]

def stop():

        g.output(29,g.LOW)

	g.output(35,g.LOW)

	g.output(31,g.LOW)

	g.output(33,g.LOW)

      

def ultra():

        

        print("checking obstacles")

       # will work at least 3 times

        if 1:

                g.output(Trig,False)

                t.sleep(0.02)

                g.output(Trig,True)

                t.sleep(0.0001)

                g.output(Trig,False)



                while g.input(Echo) == 0 :

                        pulse_start = t.time()

                while g.input(Echo) == 1 :

                        pulse_end = t.time()



                pulse_dur = pulse_end - pulse_start

                distance = pulse_dur * 17150

                distance = round(distance,2)

                #print(distance)

        

                if distance<= 10 :

                        print("OBSTACLE DETECTED")

                        stop()

                        stopa=1

                        direction('r',3)

                        #print("Turning right")

                        direction('f',3)

                        #print("going Ahead")

                        direction('l',3)

                        #print("Turning LEFT")

                        direction('f',3)

                        #print("going Ahead")

                        direction('l',3)

                        #print("Turning LEFT")

                        direction('f',3)

                        #print("going Ahead")

                        direction('r',3)

                        #print("Turning right")

                        

                                               



  



def direction(p ,k):

        #ultra()

	#for going forward	

	if p=="f":

		g.output(29,g.HIGH)

		g.output(35,g.HIGH)

		g.output(31,g.LOW)

		g.output(33,g.LOW)

		print("Going Forward")

                for o in range(k):

                        t.sleep(0.23)

                        print(o)

	#for going backward

	elif p=="b":

		g.output(29,g.LOW)

		g.output(35,g.LOW)

		g.output(31,g.HIGH)

		g.output(33,g.HIGH)

		print("Going Backward")

		for o in range(k):

                        t.sleep(0.23)

                        print(o)

	#for going right

	elif p=="r":

		g.output(29,g.LOW)

		g.output(31,g.LOW)

		g.output(35,g.HIGH)

		g.output(33,g.LOW)

		print("Going Right")

		for o in range(3):

                        t.sleep(0.23)

                        print(o)

	#for going left

	elif p=="l":

		g.output(29,g.HIGH)

        	g.output(35,g.LOW)

        	g.output(31,g.LOW)

        	g.output(33,g.LOW)

		print ("Going Left")

		for o in range(3):

                        t.sleep(0.23)

                        print(o)

	

                



q = 'a'

while(1):

        

        

	data = r.get("https://api.thingspeak.com/channels/458106/feeds.json?api_key=XQ037NVAG71W4PWA&results=2")

	dict = data.json()

	for x in range(1):

		x = int(dict['feeds'][1]['field1'][0])

		y = int(dict['feeds'][1]['field1'][1])

		z = int(dict['feeds'][1]['field1'][2])

		p = dict['feeds'][1]['field1'][3]

		k =  z + y*10 +x*100

	

        if p == 'R':

               while(p != 'M' and p!= 'S'):

                        data = r.get("https://api.thingspeak.com/channels/458106/feeds.json?api_key=XQ037NVAG71W4PWA&results=2")

                        dict = data.json()

                        for x in range(1):

                                x = int(dict['feeds'][1]['field1'][0])

                                y = int(dict['feeds'][1]['field1'][1])

                                z = int(dict['feeds'][1]['field1'][2])

                                p = dict['feeds'][1]['field1'][3]

                                k =  z + y*10 +x*100

                        if p != q:

                                arr.append((p,k))

                                q = p

                                print(arr)

        print("S or M is present")

       

        if p == 'M':

                ultra()

                print("keep rolling baby")

                sz = len(arr)

                for i in range(1,sz):

                        p_dash = arr[i][0]

                        k_dash = arr[i][1]

                        direction(p_dash,k_dash)

                        if i == sz-2:

                                p = 'S'

                                print("S detected")

                                break

        

        if p == 'S':

                        print("stop mode baby")

                        stop()
