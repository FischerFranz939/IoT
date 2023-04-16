from Point import Point


class DeviceBase():
    def __init__(self, name, ip_address, type):
        self.type = type
        self.name = name
        self.ip_address = ip_address
        self.time = ""

    def set_time(self, time):
        self.time = time

    def get_name(self):
        return self.name

    def get_ip_address(self):
        return self.ip_address

    def print_data(self):
        print("type:    " + self.type)
        print("name:    " + self.name)
        print("ip_addr: " + self.ip_address)
        print("time:    " + self.time)

    def print_point(self, point, log):
        if log:
            print(point)

    def create_point_rssi(self, ssid, rssi: float):
        point = Point("wifi status", self.time)
        point.addTag("device", self.name)
        point.addTag("type", self.type)
        point.addTag("SSID", ssid)
        point.addField("RSSI", rssi)
        return point.createJsonObject()

    def create_point_temperature(self, temperature: float):
        point = Point("temperature C", self.time)
        point.addTag("device", self.name)
        point.addTag("type", self.type)
        point.addField("temperature", temperature)
        return point.createJsonObject()

    def create_point_power(self, switch_name, power: float):
        point = Point("power W", self.time)
        point.addTag("device", self.name)
        point.addTag("type", self.type)
        point.addTag("switch", switch_name)
        point.addField("power", power)
        return point.createJsonObject()

    def create_point_voltage(self, voltage: float):
        point = Point("voltage V", self.time)
        point.addTag("device", self.name)
        point.addTag("type", self.type)
        point.addField("voltage", voltage)
        return point.createJsonObject()

    def create_point_switch_state(self, switch_name, switch_on_bool: int):
        point = Point("switch state", self.time)
        point.addTag("device", self.name)
        point.addTag("type", self.type)
        point.addTag("switch", switch_name)
        if switch_on_bool:
            switch_on = 1
        else:
            switch_on = 0
        point.addField("switch on", switch_on)
        return point.createJsonObject()

    def create_point_current(self, switch_name, current: float):
        point = Point("current A", self.time)
        point.addTag("device", self.name)
        point.addTag("type", self.type)
        point.addTag("switch", switch_name)
        point.addField("current", current)
        return point.createJsonObject()

    #TODO: should probably be type float
    def create_point_total(self, switch_name, power_total: int):
        point = Point("power total W", self.time)
        point.addTag("device", self.name)
        point.addTag("type", self.type)
        point.addTag("switch", switch_name)
        point.addField("power total", power_total)
        return point.createJsonObject()
