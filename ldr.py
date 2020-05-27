import RPi.GPIO as GPIO
import time

class Ldr:
    def __init__(self, pin):
        self.pin =  pin

    def read(self):
        GPIO.setup(self.pin, GPIO.OUT)
        count = 0
        GPIO.output(self.pin, GPIO.LOW)
        time.sleep(0.1)
        GPIO.setup(self.pin, GPIO.IN)

        while (GPIO.input(self.pin) == GPIO.LOW):
            count += 1

        return count
