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

# print(bus.read_byte_data(0x16, 0b1010011))

bus.write_byte_data(SENSOR_ADDRESS, 0x00, 0x01)
bus.write_byte_data(SENSOR_ADDRESS, 0x00, 0x03)

# RED HIGH
print(bus.read_byte_data(SENSOR_ADDRESS, 0b10010111))


# GREEN HIGH
print(bus.read_byte_data(SENSOR_ADDRESS, 0b10011001))
