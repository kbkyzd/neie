#!/usr/bin/env python

import requests
import arrow
from settings import *
from grovepi import *
from grove_rgb_lcd import *
from time import *
import itertools

# Set up the headers required for authentication.
headers = {
    'Authorization': 'Bearer ' + secret,
    'Content-Type': 'application/json'
}

# Pin Modes, a small delay to let it catch up
pinMode(ledIn, 'OUTPUT')
pinMode(soundIn, 'OUTPUT')
sleep(0.5)

while True:
    try:
        # Send the request
        r = requests.get(baseurl + 'bus/arrival/' + current_stop, headers=headers)
        
        # Retrieve the output as json
        # json() is a "requests" function
        res = r.json()

        # Repeat 4 times
        for _ in itertools.repeat(None, 4):
            for result in res:
                # If it's empty, don't display
                if not len(result['NextBus']['EstimatedArrival']):
                    continue

                estArrival = arrow.get(result['NextBus']['EstimatedArrival'])
                diff = estArrival.humanize()

                # If estimated arrival is less than x seconds, sound the buzzer
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

    # Make sure all IO is cleaned up on exit (via ctrl-c)
    except KeyboardInterrupt as e:
        setText('')
        setRGB(0, 0, 0)
        analogWrite(ledIn, 0)
        digitalWrite(soundIn, 0)
        exit(0)
