#!/usr/bin/env python
import requests
from settings import *
from grovepi import *
from grove_rgb_lcd import *
from time import *

headers = {
    'Authorization': 'Bearer ' + secret,
    'Content-Type': 'application/json'
}

while True:
    try:
        [temp, hum] = dht(dht_sensor_port, dht_sensor_type)
        t = str(temp)
        h = str(hum)

        if not isinstance(temp, float) or not isinstance(hum, float):
            print('Invalid values from sensor.')

        payload = {
            'temp': float(temp),
            'humi': float(hum),
            'timestamp': int(time()),
            'stop': current_stop,
        }

        r = requests.post(baseurl + 'sensor/tempsAdd', headers=headers, json=payload)
        print(r.text)
        sleep(10)

    except KeyboardInterrupt as e:
        setText('')
        setRGB(0, 0, 0)
        exit(0)
