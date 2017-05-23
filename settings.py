import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Site
baseurl = os.environ.get('BASEURL')
secret = os.environ.get('EIENKEY')

# Sensors
delay = os.environ.get('DELAY')
dht_sensor_port = int(os.environ.get('TEMP_SENSOR_PORT'))
dht_sensor_type = int(os.environ.get('TEMP_SENSOR_TYPE'))
ledIn = int(os.environ.get('LED_PORT'))
soundIn = int(os.environ.get('BUZZER_PORT'))

# Stops/Arrival
current_stop = os.environ.get('CURRENT_STOP')
update_interval = int(os.environ.get('UPDATE_INTERVAL'))
