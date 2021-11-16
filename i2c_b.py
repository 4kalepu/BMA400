# I2C with BM400

import smbus
import time
import math
from time import sleep

bus= smbus.SMBus(1)

#switch from sleep to normal mode ACC_CONFIG0
bus.write_byte_data(0x15,0x19,0x02) 
#leave some turn on time
time.sleep(1.5)

while 1: 
    time.sleep(0.1)
    #from the addr 0x15 and register 0x4, read 6 following bytes
    data=bus.read_i2c_block_data(0x15,0x04,6)
    #data is now in pairs of bytes of MSB and LSB for X Y and Z,
    print(data)
    a =data[0]
    b =data[2]
    c=a/b;
    angle= math.asin(c)
    print(angle)
