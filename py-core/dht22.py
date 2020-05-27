#!/usr/bin/python3

import Adafruit_DHT
import board
import busio

def main():
    DHT_SENSOR            = Adafruit_DHT.DHT22
    DHT_PIN               = 4
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    return {
        "humidity":    humidity,
        "temperature": temperature
    }

print(main())
