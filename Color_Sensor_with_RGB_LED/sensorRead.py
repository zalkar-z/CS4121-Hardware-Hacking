import smbus
import time

SENSOR_ADDRESS = 0x29
bus = smbus.SMBus(1)

def get_color():
	# enable register - 0X03
	bus.write_byte_data(SENSOR_ADDRESS, 0x00, 0b00000011)

	# CLEAR LOW
	clear = bus.read_byte_data(SENSOR_ADDRESS, 0b10010100)
	clear_high = bus.read_byte_data(SENSOR_ADDRESS, 0b10010101)

	# RED LOW
	red = bus.read_byte_data(SENSOR_ADDRESS, 0b10010110)
	red_high = bus.read_byte_data(SENSOR_ADDRESS, 0b10010111)

	# GREEN LOW
	green = bus.read_byte_data(SENSOR_ADDRESS, 0b10011000)
	green_high = bus.read_byte_data(SENSOR_ADDRESS, 0b10011001)

	# BLUE LOW
	blue = bus.read_byte_data(SENSOR_ADDRESS, 0b10011010)
	blue_high = bus.read_byte_data(SENSOR_ADDRESS, 0b10011011)

	# temporary
	clear = clear_high

	if clear == 0:
		red = green = blue = 0
	else:
		red = red_high / clear * 255.0
		green = green_high / clear * 255.0
		blue = blue_high / clear * 255.0

	return [red, green, blue]

