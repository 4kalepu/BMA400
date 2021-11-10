#!/usr/bin/env python3
import requests
import time
import Adafruit_DHT

KEY = 'OS0P7Z4TPI9587KG'

def pushData(temp:float, humidity:float):
    '''Takes temperature and humidity readings and pushes data to ThingSpeak server'''
    #Set up request url and parameters
    url = 'https://api.thingspeak.com/update?api_key=OS0P7Z4TPI9587KG&field1=0'
    params = {'key': KEY, 'field1': temp, 'field2': humidity}

    #Publish values to ThingSpeak
    res = requests.get(url, params=params)


def getData(sensor:int, pin:int):
    '''
    Input DHT sensor type and RPi GPIO pin to collect a sample of data
    
    Parameters:
    sensor: Either 11 or 22, dependring on sensor used (DHT11 or DHT22)
    pin: GPIO pin used (e.g. 4)
    '''
    try:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        return humidity, temperature
    except:
        Exception("Error reading sensor data")
        return False

if __name__ == "__main__":
    while True:
        sensor = 22
        pin = 10
        humidity, temp = getData(sensor,pin)
        pushData(temp,humidity)
        time.sleep(10)

