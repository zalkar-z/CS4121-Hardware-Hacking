# import board
# import busio
# import time
# import adafruit_tcs34725
# i2c = busio.I2C(board.SCL, board.SDA)
# sensor = adafruit_tcs34725.TCS34725(i2c)


# def get_color():
#	return sensor.color_rgb_bytes


import smbus
import time

SENSOR_ADDRESS = 0x29
bus = smbus.SMBus(1)

#bus.write_byte_data(SENSOR_ADDRESS, 0x00, 0x01)

# enable register - 0X03
bus.write_byte_data(SENSOR_ADDRESS, 0x00, 0b00000011)

# setting timing register
# bus.write_byte_data(SENSOR_ADDRESS, 0x01, 0xF6)

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


# time.sleep(2)

# convert from hex to decimal

# clear = int(str(clear), 16)
# red = int(str(red), 16)
# green = int(str(green), 16)
# blue = int(str(blue), 16)


print("CLEAR: ", clear, "-", clear_high)
print("RED: ", red, "-", red_high)
print("GREEN :", green, "-", green_high)
print("BLUE :", blue, "-", blue_high)

print("-----------")

# temporary
clear = clear_high

if clear == 0:
	red = green = blue = 0
else:
	red = red_high / clear * 255.0
	green = green_high / clear * 255.0
	blue = blue_high / clear * 255.0

print("RED: ", red)
print("GREEN: ", green)
print("BLUE: ", blue) 
