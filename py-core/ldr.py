#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

def main():
    LDR_PIN = 8
    count   = 0
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LDR_PIN, GPIO.OUT)
    GPIO.output(LDR_PIN, GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(LDR_PIN, GPIO.IN)

    while (GPIO.input(LDR_PIN) == GPIO.LOW):
        count += 1

    return count

print(main())
