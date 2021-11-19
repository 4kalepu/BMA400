import time

import serial

from time import sleep

import re

import urllib.request

from subprocess import call


ser = serial.Serial(port='/dev/ttyAMA0', baudrate = 9600, parity-serial.PARITY NONE, stopbits-serial.STOPBITS_ONE, bytesize-serial.EIGHTBITS, timeout=1 }

ldr='' 
ctemp=''
ftemp=""
brake=''

counter=0

ser.flushInput()

url1= https://api.thingspeak.com/update?api_key=0S0P7Z4TPI9587KG&fieldl=0'

while 1:

	data_string=ser.readline().decode() 
	data_float= re.findall('\d+(?:\.\d+)?, data_string) 
	NID=data_float [1]

	if NID=="1":
		ldr=data_float [2] 
	elif NID=="2":
		ctemp=data_float [2] 
	elif NID=="3":
		brake=data float [2]
	elif NID=="4":
		ftemp=data_float [2]

	counter=counter+1
	print (data_float)

	if counter>=4:
		upload1=urllib.request.urlopen(urll+ldr+"&field2=0"+ctemp+"&field3=0"+brake+"&field4=0"+ftemp)
		upload1.read()
		upload1.close()
		counter=0