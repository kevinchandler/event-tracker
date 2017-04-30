import datetime
import time
from dateutil import parser
import RPi.GPIO as GPIO
import requests

SLEEP_DURATION = 120
API_URL = "https://litter-tracker.herokuapp.com/log-event"

# GPIO setup
GPIO_CHANNEL = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_CHANNEL, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setwarnings(True)

# Motion
def motion_detected():
    requests.post(API_URL)
    print 'Sleeping for %s' % SLEEP_DURATION
    time.sleep(SLEEP_DURATION)

def detect_motion():
    while True:
        input_state = GPIO.input(GPIO_CHANNEL)
        if input_state == True:
            print 'Motion detected'
            motion_detected()

detect_motion()
