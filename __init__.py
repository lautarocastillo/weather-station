import os
from flask     import Flask, render_template, request
from .dht22    import Dht22
from .ldr      import Ldr
from .veml6075 import Veml6075
from .myIp     import MyIp


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.root_path, 'db/weather-station.sqlite')
    )
    DHT_PIN = 4
    LDR_PIN = 14

    from . import db
    db.init_app(app)

    @app.route("/")
    @app.route("/json")
    def main():
        from weather.db import get_db
        uv_sensor  = Veml6075()
        dht_sensor = Dht22(DHT_PIN)
        light      = Ldr(LDR_PIN)
        weather    = dht_sensor.read()
        ip         = MyIp.get()

        templateData = {
            **weather,
            'light': light.read(),
            **uv_sensor.read(),
            'my_ip': ip
        }

        # db = get_db()
        # db.execute(
        #     'INSERT INTO weather (temperature, humidity, light) VALUES (?, ?, ?)',
        #     (weather['temperature'], weather['humidity'], light)
        # )
        # db.commit()

        if request.path == "/json":
            return templateData

        else:
            return render_template('main.html', **templateData)

    @app.route("/weather")
    def weather():
        dht_sensor = Dht22(DHT_PIN)
        return dht_sensor.read()

    @app.route("/light")
    def light():
        light = Ldr(LDR_PIN)
        return { 'light': light.read() }

    return app
