import board
import busio
import adafruit_veml6075

class Veml6075:
    def __init__(self):
        self.i2c  = busio.I2C(board.SCL, board.SDA)
        self.veml = adafruit_veml6075.VEML6075(self.i2c, integration_time=100)

    def read(self):
        return {
            'uv_index': self.veml.uv_index,
            'uva':      self.veml.uva,
            'uvb':      self.veml.uvb
        }
