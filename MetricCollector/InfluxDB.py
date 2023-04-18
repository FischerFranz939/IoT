from influxdb import InfluxDBClient
import Const


class InfluxDB:
    def __init__(self):
        self.client = InfluxDBClient(Const.INFLUXDB_HOST, Const.INFLUXDB_PORT)
        self.client.switch_database(Const.INFLUXDB_NAME)

    def write_points(self, points):
        self.client.write_points(points)

    def drop_measurement(self, measurement):
        self.client.drop_measurement(measurement)

    def execute_query(self, query):
        result = self.client.query(query)
        print(result)

'''
#InfluxDB shell version: 1.8.10

https://w2.influxdata.com/blog/getting-started-python-influxdb/


#result = client.query('SELECT "temperature", "device" FROM "telegraf"."autogen"."temperature C" WHERE time > now() - 1s')
#result = client.query('SELECT * FROM "telegraf"."autogen"."temperature C" WHERE time > now() - 10s')
#result = client.query('SELECT * FROM "telegraf"."autogen"."wifi status" WHERE time > now() - 30s')
#result = client.query('SELECT * FROM "telegraf", "wifi status" WHERE time > now() - 30s')
#print(result)


ResultSet(
    {'('temperature C', None)':
        [
            {'time': '2023-04-09T16:06:44.362830Z',
             'device': 'Agent03',
             'temperature': 15.3,
             'temperature T0': None,
             'temperature T1': None,
             'temperature T2': None,
             'temperature T3': None,
             'temperature T4': None,
             'temperatureAvg': None},
            {'time': '2023-04-09T16:06:44.385712Z', 'device': 'Agent03', 'temperature': None, 'temperature T0': None, 'temperature T1': None, 'temperature T2': None, 'temperature T3': None, 'temperature T4': None, 'temperatureAvg': 15.41},
            {'time': '2023-04-09T16:06:45.305075Z', 'device': 'Agent01', 'temperature': 15.6, 'temperature T0': None, 'temperature T1': None, 'temperature T2': None, 'temperature T3': None, 'temperature T4': None, 'temperatureAvg': None},
            {'time': '2023-04-09T16:06:45.326261Z', 'device': 'Agent01', 'temperature': None, 'temperature T0': None, 'temperature T1': None, 'temperature T2': None, 'temperature T3': None, 'temperature T4': None, 'temperatureAvg': 15.6}
        ]
    }
)
'''
