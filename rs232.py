import time

import serial


ser=serial.Serial(
    port='/dev/ttyAMA0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1

)
ser.flushInput()
while 1:
    data_string=ser.readline().decode()
    print(data_string)
