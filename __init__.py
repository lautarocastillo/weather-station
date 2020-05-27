import os
from flask import Flask, render_template, request
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import board
import busio
import adafruit_veml6075

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.root_path, 'db/weather-station.sqlite')
    )
    DHT_SENSOR = Adafruit_DHT.DHT22
    DHT_PIN    = 4
    LDR_SENSOR = 8

    from . import db
    db.init_app(app)

    GPIO.setmode(GPIO.BOARD)

    def rc_time(ldr_pin):
        count = 0
        GPIO.setup(ldr_pin, GPIO.OUT)
        GPIO.output(ldr_pin, GPIO.LOW)
        time.sleep(0.1)

        GPIO.setup(ldr_pin, GPIO.IN)

        while (GPIO.input(ldr_pin) == GPIO.LOW):
            count += 1

        return count

    def uv_sensor():
        i2c  = busio.I2C(board.SCL, board.SDA)
        veml = adafruit_veml6075.VEML6075(i2c, integration_time=100)

        return veml

    @app.route("/")
    @app.route("/json")
    def main():
        from weather.db import get_db
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        light = rc_time(LDR_SENSOR)
        templateData = {
            'temperature': round(temperature, 2),
            'humidity':    round(humidity, 2),
            'light':       light,
            'uv_index':    uv_sensor.uv_index,
            'uva':         uv_sensor.uva,
            'uvb':         uv_sensor.uvb
        }

        db = get_db()
        db.execute(
            'INSERT INTO weather (temperature, humidity, light) VALUES (?, ?, ?)',
            (temperature, humidity, light)
        )
        db.commit()

        if request.path == "/json":
            return templateData

        else:
            return render_template('main.html', **templateData)

    @app.route("/weather")
    def weather():
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        return {
            'temperature': round(temperature, 2),
            'humidity':    round(humidity, 2)
        }

    @app.route("/light")
    def light():
        light = rc_time(LDR_SENSOR)
        return { 'light': light }

    return app
