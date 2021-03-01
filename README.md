# PiAPI Python Client Library
##### [Bolillo Kremer](https://youtube.com/BolilloKremer?https://www.youtube.com/BolilloKremer?sub_confirmation=1)

## Overview
This user friendly library allows you to easily interface with multiple raspberry pi's at once using [PiAPI](https://github.com/Bolillo-Kremer/PiAPI). The simplicity of this library makes it easy for anybody to use. Most functionality is based off of [onoff](https://www.npmjs.com/package/onoff), which is running on [PiAPI](https://github.com/Bolillo-Kremer/PiAPI).

For updates on this project and other other entertainging coding projects, please subscribe to my YouTube channel, [Bolillo Kremer](https://youtube.com/BolilloKremer?https://www.youtube.com/BolilloKremer?sub_confirmation=1). 

## How to use

### Requirements
This library requires that [PiAPI](https://github.com/Bolillo-Kremer/PiAPI) is running on your raspberry pi. You can intall it on your pi with only one command! For instructions, [click here](https://github.com/Bolillo-Kremer/PiAPI/blob/master/README.md).

### Initializing
Use this pip command to install the PiAPI package
```
python -m pip install https://github.com/Bolillo-Kremer/PiAPI-Python_Client/blob/master/PiAPI-latest.tar.gz?raw=true
```
After installing package, you will need to setup you PiAPI connection like this.

```py
from PiAPI import Pi
```
```py

#Initialize Pi object with IP address and port of pi
my_pi = Pi.New_Pi("192.168.1.100", Pi.default_port())

#You need to specify which pins will be set as input or output
my_pi.init_pin(2, "in")
my_pi.init_pin(3, "out")
```

If you would rather provide a specific url than using an IP address and a port, you can do so like this.
```py
my_pi = Pi("http://192.168.1.100:5000")
```


### Interfacing

You can get the state (0 or 1) of a given pin using this function
```py
#Returns the state of pin 2 as integer
my_pi.get_state(2)
```

You can also get a JSON formatted string of all the pin states using this function.

```py
#Returns dict
my_pi.get_states()
```
If you want to set the state (0 or 1) of a pin, use this function
```py
#Sets pin 2 to state 0
my_pi.set_state(2, 0)
```
Alternatively, you can use "toggle" to toggle the pins state
```py
#Sets pin 2 to state 0
my_pi.set_state(2, "toggle")
```

If you wish to set the state of all initiated pins, you can do so with the set_all_states() function.


### API Settings

This library also allwos you to interface with the PiAPI settings.

Current Settings:
* Port (Gets or sets the port that the API is running on)
* (IN DEVELOPMENT) Keys (Gets or sets keys that must be provided upon each request)

The settings will take place on server reboot.

#### Example
```py
#Changes port to 5000
my_pi.set_api_port(5000)
```

### Helpers

Memorizing the names for certain actions such as "in", "out", "rising", "falling" can be confusing.
If you need help, you can use the helper module like this


```py
from PiAPI import Pi
from PiAPI.Helpers import Pin

#Initialize Pi object with IP address and port of pi
my_pi = Pi.New_Pi("192.168.1.100", Pi.default_port())

#You need to specify which pins will be set as input or output
my_pi.init_pin(2, Pin.in_())
my_pi.init_pin(3, Pin.out())
```


For updates on this project and other other entertainging coding projects, please subscribe to my YouTube channel, [Bolillo Kremer](https://youtube.com/BolilloKremer?https://www.youtube.com/BolilloKremer?sub_confirmation=1). 
