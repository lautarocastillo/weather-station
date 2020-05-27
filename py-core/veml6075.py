#!/usr/bin/python3

import board
import busio
import adafruit_veml6075

def main():
    i2c  = busio.I2C(board.SCL, board.SDA)
    veml = adafruit_veml6075.VEML6075(i2c, integration_time=100)

    return {
        'uv_index': veml.uv_index,
        'uva':      veml.uva,
        'uvb':      veml.uvb
    }

print(main())
