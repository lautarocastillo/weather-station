import Adafruit_DHT
import board
import busio

class Dht22:
    def __init__(self, pin):
        self.pin    = pin
        self.sensor = Adafruit_DHT.DHT22

    def read(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        return {
            "humidity":    humidity,
            "temperature": temperature
        }
