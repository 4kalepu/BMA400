import time
import serial
import re
import urllib2


# setup serial communication
ser = serial.Serial(
    port='/dev/ttyAMA0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)
ser.flushInput()

# declare globals
counter = 0



# prepare API codes
url1 = 'https://api.thingspeak.com/update?api_key=OS0P7Z4TPI9587KG&field1=0'
url2 = 'https://api.thingspeak.com/update?api_key=OS0P7Z4TPI9587KG&field2=0'
url3 = 'https://api.thingspeak.com/update?api_key=OS0P7Z4TPI9587KG&field3=0'
url4 = 'https://api.thingspeak.com/update?api_key=OS0P7Z4TPI9587KG&field4=0'


# main loop
while 1:
    time.sleep(.25)
    data_string = ser.readline()   # read data from the serial port
    # filter data from the printed string
    data_num = re.findall('\d+(?:\.\d+)?', data_string)

    # assign which node is the data from
    NID = data_num[1]
    print(data_num)
    if NID == "1":  #  Cabin temperature of the engine
        Temperature1 = data_num[2]

    elif NID == "2":  # Node two takes in the temperature outside and the surrounding light
        Temperature2 = data_num[2]
        Light2 = data_num[3]
    elif NID == "3":  # Node three takes in the data from the accelerometer
        Accel1 = data_num[2]
        Accel2 = data_num[3]
        Accel3 = data_num[4]
    elif NID == "4": # Node four takes the data from parking sensors
        ParkingSensor = data_num[2]

    counter = counter+1 # keep note on the amount of taken samples
    print(data_num)

    if counter >= 64:  # once there is enough data captured
       
        print("Uploading..")
        upload1 = urllib2.urlopen(
            url1+'&field1=0'+str(Temperature1)+"&field2=0"+str(Light1))
        upload1.read()
        upload1.close()
        upload1 = urllib2.urlopen(
            url2+'&field1=0'+str(Temperature2)+"&field2=0"+str(Light2))
        upload1.read()
        upload1.close()
        upload1 = urllib2.urlopen(
            url3+'&field1=0'+str(Accel1)+"&field2=0"+str(Accel2)+"&field3=0"+str(Accel3))
        upload1.read()
        upload1.close()
        upload1 = urllib2.urlopen(
            url4+'&field1=0'+str(ParkingSensor))
        upload1.read()
        upload1.close()
        counter = 0
        print("Uploaded!")