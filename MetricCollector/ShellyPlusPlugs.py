from DeviceBase import DeviceBase
import Const


class ShellyPlusPlugs(DeviceBase):
    def __init__(self, name, ip_address):
        super(ShellyPlusPlugs, self).__init__(name, ip_address, Const.POWER_SWITCH)

    def get_status_url(self):
        return DeviceBase.get_ip_address(self) + "/rpc/Shelly.GetStatus"

    def initialize(self, response, time):
        DeviceBase.set_time(self, time)
        self.ssid        = response['wifi']['ssid']
        self.rssi        = response['wifi']['rssi']
        self.switch_on   = response['switch:0']['output']
        self.power       = response['switch:0']['apower']
        self.voltage     = response['switch:0']['voltage']
        self.current     = response['switch:0']['current']
        self.total       = response['switch:0']['aenergy']['total']
        self.temperature = response['switch:0']['temperature']['tC']
        self.uptime      = response['sys']['uptime']

    def print_data(self):
        DeviceBase.print_data(self)
        print("ssid:            " + str(self.ssid))
        print("rssi:            " + str(self.rssi))
        print("switch_on:       " + str(self.switch_on))
        print("power (W):       " + str(self.power))
        print("voltage (V):     " + str(self.voltage))
        print("current (A):     " + str(self.current))
        print("total (W):       " + str(self.total))
        print("temperature (C): " + str(self.temperature))
        print("uptime (s):      " + str(self.uptime))

    def create_list_of_measurements(self, log=False):
        points = list()

        point = DeviceBase.create_point_rssi(self, self.ssid, self.rssi)
        DeviceBase.print_point(self, point, log)
        points.append(point)

        point = DeviceBase.create_point_switch_state(self, "switch_0", self.switch_on)
        DeviceBase.print_point(self, point, log)
        points.append(point)

        point = DeviceBase.create_point_power(self, "switch_0", self.power)
        DeviceBase.print_point(self, point, log)
        points.append(point)

        point = DeviceBase.create_point_voltage(self, self.voltage)
        DeviceBase.print_point(self, point, log)
        points.append(point)

        point = DeviceBase.create_point_current(self, "switch_0", self.current)
        DeviceBase.print_point(self, point, log)
        points.append(point)

        #TODO: should be float 
        point = DeviceBase.create_point_total(self, "switch_0", int(self.total))
        DeviceBase.print_point(self, point, log)
        points.append(point)

        point = DeviceBase.create_point_temperature(self, self.temperature)
        DeviceBase.print_point(self, point, log)
        points.append(point)

        # uptime

        return points

'''
https://shelly-api-docs.shelly.cloud/gen2/ComponentsAndServices/WiFi/#wifigetstatus-example
http://shellyplusplugs/rpc/Shelly.GetStatus
http://192.168.178.xxx/rpc/WiFi.SetConfig?config={"ap":{"enable":true}}
'''
