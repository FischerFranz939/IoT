import requests
import json
import pytz
import time
import Const
from InfluxDB import InfluxDB
from datetime import datetime
from DeviceFactory import DeviceFactory


#-------------------------------------------------------------------------------
factory = DeviceFactory()
devices = factory.get_device_list()

#-------------------------------------------------------------------------------
influx = InfluxDB()

#influx.drop_measurement("total W")
#query = 'DROP SERIES FROM "total W"'
#query = 'SHOW FIELD KEYS'
#query = 'SELECT "temperature", "device" FROM "telegraf"."autogen"."temperature C" WHERE time > now() - 15m'
#query = 'SELECT "total", "device" FROM "telegraf"."autogen"."total W" WHERE time > now() - 15m'
#influx.execute_query(query)
#exit(1)


#-------------------------------------------------------------------------------
# LOOP
#-------------------------------------------------------------------------------
while True:
    time_string = datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    for device in devices:
        url = device.get_status_url()
        response = None
        try:
            response = requests.get(url, timeout=Const.REQUEST_TIMEOUT)
            if response.status_code == 200:
                json_data = json.loads(response.text)
                device.initialize(json_data, time_string)
                #device.print_data()
                points = device.create_list_of_measurements(False)
                influx.write_points(points)
        except requests.ConnectionError:
            print("ERROR: " + device.get_name() + " has ConnectionError")

    time.sleep(Const.LOOP_SLEEP)
