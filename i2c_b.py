# I2C with BM400 

from re import X 
import smbus
import time 
import math
import urllib.request
from time import sleep

bus= smbus.SMBus (1)

urll='https://api.thingspeak.com/update?api_key=0S0P7Z4TPI9587KG&fieldl=0'
a= ''
#switch from sleep to normal mode ACC CONFIGO 14 bus.write_byte data (0x15,0x19,0x02)
bus.write_byte_data(0x15,0x19,0x02)
#leave some turn on time
time.sleep (1.5)
print("Initializing I2C") 
while 1:
	print("Reading 12c") 
	time.sleep(0.1)
	#from the addr 0x15 and register 0x4 read 6 following bytes
	data=bus.read_12c_block_data(0x15,0x04,6) 
	#data is now In pairs of bytes of MSB and LSB for X Y and Z.
	#print (data),
	y=data[2]+data[3]*256
	a=0.176*y
	if a<360:
		print(a)
	else:
		a=a-720 
		print (a)
	str_a=str(a)
	uploadl=urllib.request.urlopen(urll+"&field5-0"+str_a)
	upload1.read()
	upload1.close()
	counter=0