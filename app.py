#!/usr/bin/python3

from flask import Flask, render_template
import Adafruit_DHT
import RPi.GPIO as GPIO
import time

app        = Flask(__name__)
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN    = 4
LDR_SENSOR = 26
GPIO.setmode(GPIO.BOARD)

@app.route("/")
def main():
   humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
   light = rc_time(LDR_SENSOR)
   templateData = {
      'temperature': temperature,
      'humidity':    humidity,
      'light':       light
   }
   return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080, debug=True)

def rc_time(ldr_pin):
    count = 0
    GPIO.setup(ldr_pin, GPIO.OUT)
    GPIO.output(ldr_pin, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(ldr_pin, GPIO.IN)

    while (GPIO.input(ldr_pin) == GPIO.LOW):
        count += 1

    GPIO.cleanup()
    return count
