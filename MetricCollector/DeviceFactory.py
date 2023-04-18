import Const
from ShellySwitch25 import ShellySwitch25
from ShellyPlusPlugs import ShellyPlusPlugs


#-------------------------------------------------------------------------------
# List of devices
#-------------------------------------------------------------------------------
device_ids = dict()
#          <------------ name ------------>    <--------- url ------->
device_ids[Const.SHELLY_SWITCH_25  + "-001"] = "http://192.168.128.20"
device_ids[Const.SHELLY_PLUS_PLUGS + "-001"] = "http://192.168.128.43"


#-------------------------------------------------------------------------------
# Factory
#-------------------------------------------------------------------------------
class DeviceFactory:
    def __init__(self):
        self.devices = list()
        for name, url in device_ids.items():
            if Const.SHELLY_SWITCH_25 in name:
                self.devices.append(ShellySwitch25(name, url))
            if Const.SHELLY_PLUS_PLUGS in name:
                self.devices.append(ShellyPlusPlugs(name, url))

    def get_device_list(self):
        return self.devices
