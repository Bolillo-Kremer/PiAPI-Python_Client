import requests
import json
from PiAPI.Helpers import Pin

class New_Pi:
    __ip_address = ""
    __port = -1
    __url_override = ""

    def __init__(self, address, port = -1):
        if (port != -1):
            self.__ip_address = address
            self.__port = port
        else:
            self.__url_override = address

    def raw_url(self) -> str:
        url = ""
        if (self.__ip_address != ""):
            url += "http://" + self.__ip_address
            url += ":" + str(self.__port) if (self.__port != -1) else ""
        else:
            url += self.__url_override
        return url

    def __check_url(self):
        if not (self.__ip_address != "" or self.__url_override != ""):
            raise Exception("API url not provided")

    def init_pin(self, pin: int, direction: str, edge: str = None, edgeTimeout: int = -1):
        self.__check_url()
        url = self.raw_url() + "/InitPin"

        pin_settings = {
            "pin": str(pin),
            "direction": direction
        }

        if (edge != None):
            pin_settings["edge"] = edge

        if (edgeTimeout != -1):
            pin_settings["edgeTimeout"] = edgeTimeout
        
        return requests.post(url, json.dumps(pin_settings)).text

    def unexport_pin(self, pin: int) -> str:
        self.__check_url()
        url = self.raw_url() + "/Unexport"

        return requests.post(url, str(pin)).text

    def clean_exit(self) -> str:
        self.__check_url()
        url = self.raw_url() + "/CleanExit"

        return requests.get(url).text

    def set_state(self, pin: int, state: int) -> str:
        self.__check_url()
        url = self.raw_url() + "/SetState"

        pin_settings = {
            "pin": pin,
            "state": str(state)
        }

        return requests.post(url, json.dumps(pin_settings)).text

    def set_all_states(self, state: int) -> str:
        self.__check_url()
        url = self.raw_url() + "/SetState"

        pin_settings = {
            "pin": Pin.all(),
            "state": str(state)
        }

        return requests.post(url, json.dumps(pin_settings)).text

    def get_state(self, pin: int) -> int:
        self.__check_url()
        url = self.raw_url() + "/GetState"

        return int(requests.post(url, str(pin)).text)

    def get_all_states(self) -> dict:
        self.__check_url()
        url = self.raw_url() + "/GetState"

        return json.loads(requests.post(url, Pin.all()).text)

    def active_pins(self) -> dict:
        self.__check_url()
        url = self.raw_url() + "/ActivePins"

        return json.loads(requests.get(url).text)
    
    def command(self, command: str):
        self.__check_url()
        url = self.raw_url() + "/Command"

        return requests.post(url, command).text

    def reboot(self):
        self.__check_url()
        return command("sudo reboot")
    
    def shutdown(self):
        self.__check_url()
        return command("sudo shutdown -h")

    def ip_address(self):
        return self.__ip_address
    
    def port(self):
        return self.__port

    def set_setting(self, setting_name, setting_value):
        self.__check_url()
        url = self.raw_url() + "/SetSetting"

        setting = {
            "setting": setting_name,
            "val": json.dumps(setting_value)
        }

        return json.loads(requests.post(url, json.dumps(setting)).text)

    def get_setting(self, setting_name: str):
        self.__check_url()
        url = self.raw_url() + "/GetSetting"

        return requests.post(url, setting_name).text

    def set_api_port(self, port: int):
        return self.set_setting("port", port)

    def api_port(self):
        return self.get_setting("port")

#Module

__default_port = 5000

def default_port() -> int:
    return __default_port