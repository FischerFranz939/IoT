from DeviceBase import DeviceBase
import Const


class ShellySwitch25(DeviceBase):
    def __init__(self, name, ip_address):
        super(ShellySwitch25, self).__init__(name, ip_address, Const.POWER_SWITCH)

    def get_status_url(self):
        return DeviceBase.get_ip_address(self) + "/status"

    def initialize(self, response, time):
        DeviceBase.set_time(self, time)
        self.ssid = response['wifi_sta']['ssid']
        self.rssi = response['wifi_sta']['rssi']
        self.switch_0_on = response['relays'][0]['ison']
        self.switch_1_on = response['relays'][1]['ison']
        self.power_0 = response['meters'][0]['power']
        self.total_0 = response['meters'][0]['total']
        self.power_1 = response['meters'][1]['power']
        self.total_1 = response['meters'][1]['total']
        self.temperature = response['temperature']
        self.voltage = response['voltage']
        self.uptime = response['uptime']
        self.switch_0_overpower = response['relays'][0]['overpower']
        self.switch_1_overpower = response['relays'][1]['overpower']
        self.switch_0_overtemperature = response['relays'][0]['overtemperature']
        self.switch_1_overtemperature = response['relays'][1]['overtemperature']
        self.temperature_status = response['temperature_status']

    def print_data(self):
        DeviceBase.print_data(self)
        print("ssid:                      " + str(self.ssid))
        print("rssi:                      " + str(self.rssi))
        print("switch_0_on:               " + str(self.switch_0_on))
        print("switch_1_on:               " + str(self.switch_1_on))
        print("power_0 (W):               " + str(self.power_0))
        print("total_0 (W):               " + str(self.total_0))
        print("power_1 (W):               " + str(self.power_1))
        print("total_1 (W):               " + str(self.total_1))
        print("temperature (C):           " + str(self.temperature))
        print("voltage (V):               " + str(self.voltage))
        print("uptime (s):                " + str(self.uptime))
        print("switch_0_overpower:        " + str(self.switch_0_overpower))
        print("switch_1_overpower:        " + str(self.switch_1_overpower))
        print("switch_0_overtemperature:  " + str(self.switch_0_overtemperature))
        print("switch_1_overtemperature:  " + str(self.switch_1_overtemperature))
        print("temperature_status:        " + str(self.temperature_status))

    def create_list_of_measurements(self, log=False):
        points = list()

        point = DeviceBase.create_point_rssi(self, self.ssid, self.rssi)
        DeviceBase.print_point(self, point, log)
        points.append(point)

        point = DeviceBase.create_point_switch_state(self, "switch_0", self.switch_0_on)
        DeviceBase.print_point(self, point, log)
        points.append(point)

        point = DeviceBase.create_point_switch_state(self, "switch_1", self.switch_1_on)
        DeviceBase.print_point(self, point, log)
        points.append(point)

        point = DeviceBase.create_point_power(self, "switch_0", self.power_0)
        DeviceBase.print_point(self, point, log)
        points.append(point)

        #TODO: should be float ...needs internet access/time...unit: W minutes
        point = DeviceBase.create_point_total(self, "switch_0", int(self.total_0))
        DeviceBase.print_point(self, point, log)
        points.append(point)

        point = DeviceBase.create_point_power(self, "switch_1", self.power_1)
        DeviceBase.print_point(self, point, log)
        points.append(point)

        #TODO: should be float ...needs internet access/time...unit: W minutes
        point = DeviceBase.create_point_total(self, "switch_1", int(self.total_1))
        DeviceBase.print_point(self, point, log)
        points.append(point)

        point = DeviceBase.create_point_temperature(self, self.temperature)
        DeviceBase.print_point(self, point, log)
        points.append(point)

        point = DeviceBase.create_point_voltage(self, self.voltage)
        DeviceBase.print_point(self, point, log)
        points.append(point)

        # uptime
        # switch_0_overpower
        # switch_1_overpower
        # switch_0_overtemperature
        # switch_1_overtemperature
        # temperature_status

        return points

'''
https://shelly-api-docs.shelly.cloud/gen1/#shelly2-status
'''