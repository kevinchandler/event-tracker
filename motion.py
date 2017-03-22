import datetime
from dateutil import parser
import time

# Logging
def log_event():
    write_timestamp_to_file(event_file())
    write_timestamp_to_file(last_event_file())

def event_file(mode = 'a'):
    return open('logs/events.log', mode)

def last_event_file(mode = 'w'):
    return open('logs/last_recorded_event.log', mode)

def last_event_time():
    last_event = last_event_file('r').read().rstrip()
    return parser.parse(last_event)

def write_timestamp_to_file(file):
    timestamp = datetime.datetime.now().isoformat()
    file.write(timestamp)
    file.write('\n')
    file.close()

def should_log_event():
    current_time = datetime.datetime.now()
    last_logged_time = last_event_time()
    time_difference = current_time - last_event_time()
    if time_difference > datetime.timedelta(minutes = 2):
        return True
    else:
        return False

# Motion
def motion_detected():
    if should_log_event():
        log_event()
        print 'sleeping for 2 minutes'
        time.sleep(120)

def detect_motion():
    while True:
        # TODO: Implement GPIO
        gpio = 1
        if gpio == 1:
            motion_detected()


detect_motion()
