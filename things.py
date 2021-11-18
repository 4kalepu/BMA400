import time
import serial
from time import sleep
import re
import urllib2

ser = serial.Serial(
        port='/dev/ttyAMA0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)
counter=0
ser.flushInput()
url1='https://api.thingspeak.com/update?api_key=OS0P7Z4TPI9587KG&field1=0'
while 1:
        data_string=ser.readline()
        data_float= re.findall('\d+(?:\.\d+)?',data_string)
        NID=data_float[1]

        if NID=="1":
                Temperature1=data_float[2]
        elif NID=="2":
                Temperature2=data_float[2]
        elif NID=="3":
                Temperature3=data_float[2]
        elif NID=="4":
                Temperature4=data_float[2]

        counter=counter+1
        print(data_float)

if counter>=4:
                upload1=urllib2.urlopen(url1+Temperature1+"&field2=0"+Temperature2+"&field3=0"+Temperature3+"&field4=0"+Temperature4)
                upload1.read()
                upload1.close()
                counter=0
