import smbus
import time


# set device address
SENSOR_ADDRESS = 0x29

# user bus#1
bus = smbus.SMBus(1)

# read a color from the sensor
def get_color():
	# enable register - 0X03
	bus.write_byte_data(SENSOR_ADDRESS, 0x00, 0b00000011)

	# for all [Clear, Red, Green, Blue] below, we have to read LOW state first, and then HIGH state. 
	# Since, according to the manafacturer's datasheet, it would give us the most accurate value
	# Once we get HIGH state, we don't care about LOW state
	# NOTE: for all colors, LOW and HIGH states have consequent addresses

	# CLEAR
	clear = bus.read_byte_data(SENSOR_ADDRESS, 0b10010100)
	clear = bus.read_byte_data(SENSOR_ADDRESS, 0b10010101)

	# RED
	red = bus.read_byte_data(SENSOR_ADDRESS, 0b10010110)
	red = bus.read_byte_data(SENSOR_ADDRESS, 0b10010111)

	# GREEN
	green = bus.read_byte_data(SENSOR_ADDRESS, 0b10011000)
	green = bus.read_byte_data(SENSOR_ADDRESS, 0b10011001)

	# BLUE
	blue = bus.read_byte_data(SENSOR_ADDRESS, 0b10011010)
	blue = bus.read_byte_data(SENSOR_ADDRESS, 0b10011011)
	
	# if the color is black
	if clear == 0:
		red = green = blue = 0
	else:
		red = red / clear * 255.0
		green = green / clear * 255.0
		blue = blue / clear * 255.0

	return [red, green, blue]

