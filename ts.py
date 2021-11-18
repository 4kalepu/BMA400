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
url2 = 'https://api.thingspeak.com/update?api_OS0P7Z4TPI9587KG&field2=0'
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
    if NID == "1":  # Node one takes comparator light value and temperature of the engine
        Temperature1 = data_num[2]
        Light1 = data_num[3]
    elif NID == "2":  # Node two takes in the temperature outside and the surrounding light
        
    elif NID == "3":  # Node three takes in the data from the accelerometer
        
    elif NID == "4": # Node four takes the data from parking sensors
        

    counter = counter+1 # keep note on the amount of taken samples
    print(data_num)

    if counter >= 4:  # once there is enough data captured
       
        print("Uploading..")
        if(NID[1]==1)
            upload1 = urllib.urlopen("https://api.thingspeak.com/update?key=OS0P7Z4TPI9587KG&field1=data_num[3]")
            upload1.read()
            upload1.close()
        elif(NID[1]==2)    
            upload1 = urllib2.urlopen(url2+'&field1=0'+str(Temperature2)+"&field2=0"+str(Light2))
            upload1.read()
            upload1.close()
        elif(NID[1]==3)
            upload1 = urllib2.urlopen(url2+'&field1=0'+str(Temperature2)+"&field2=0"+str(Light2))
            upload1.read()
            upload1.close()
        else(NID[1]==4)
            upload1 = urllib2.urlopen(url2+'&field1=0'+str(Temperature2)+"&field2=0"+str(Light2))
            upload1.read()
            upload1.close()
        counter = 0
        print("Uploaded!") 