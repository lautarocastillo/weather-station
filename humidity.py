#!/usr/bin/python3

from flask import Flask, render_template
import Adafruit_DHT
app = Flask(__name__)
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

@app.route("/")
def main():
   humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
   templateData = {
      'temperature' : temperature,
      'humidity': humidity
      }
   return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080, debug=True)

