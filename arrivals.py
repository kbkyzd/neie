#!/usr/bin/env python
import requests
import arrow
from settings import *
from grovepi import *
from grove_rgb_lcd import *
from time import *
import itertools

headers = {
    'Authorization': 'Bearer ' + secret,
    'Content-Type': 'application/json'
}

pinMode(ledIn, 'OUTPUT')
pinMode(soundIn, 'OUTPUT')
sleep(0.5)

while True:
    try:
        r = requests.get(baseurl + 'bus/arrival/' + current_stop, headers=headers)
        res = r.json()

        for _ in itertools.repeat(None, 4):
            for result in res:
                if not len(result['NextBus']['EstimatedArrival']):
                    continue

                estArrival = arrow.get(result['NextBus']['EstimatedArrival'])
                diff = estArrival.humanize()

                if ((estArrival - arrow.now()).total_seconds()) < 300:
                    analogWrite(ledIn, 255)
                    digitalWrite(soundIn, 1)

                setRGB(16, 3, 16)

                setText(result['ServiceNo'] + ': ' + diff)
                print('Diff for ' + result['ServiceNo'] + ': ' + diff)
                sleep(3)

                analogWrite(ledIn, 0)
                digitalWrite(soundIn, 0)

                setText(result['ServiceNo'] + ': ' + result['NextBus']['Load'])
                sleep(5)

        sleep(update_interval)

    except KeyboardInterrupt as e:
        setText('')
        setRGB(0, 0, 0)
        analogWrite(ledIn, 0)
        digitalWrite(soundIn, 0)
        exit(0)
