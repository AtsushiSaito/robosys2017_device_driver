# robosys2017_device_driver
LED Device Driver for Raspberry Pi 3 (Raspbian)

## Description
A Electronic Dice using 7 LEDs.

When you insmod this driver, myled0 will appear in /dev.

## Demo
[Electronic Dice with RaspberryPi3 - YouTube](https://www.youtube.com/watch?v=V4qKCxzMV2Y
)
## Requirements

* RaspberryPi 3
* linux kernel source
	* download kernel source into /usr/src/linux
	* kernel build scripts : https://github.com/ryuichiueda/raspberry_pi_kernel_build_scripts
* Led
* resistor
	* 10[Ω]

## Installation
Connect led, resistors, to Raspberry Pi GPIO [5, 6, 13, 19, 26, 12, 16, 20, 21].


※Digital dice uses 7 LEDs, but up to 9 LEDs can be used with this device driver.


First, download this repository.

```
https://github.com/AtsushiSaito/robosys2017_device_driver.git
```

Next, move into robosys2017_device_driver directory and following command.

```
cd robosys2017_device_driver
make && sudo insmod myled.ko
sudo chmod 666 /dev/myled0

```

## Usage
Run the following script.

```
./Dice.py
```

## License
This repository is licensed under the GPLv3 license, see LICENSE.