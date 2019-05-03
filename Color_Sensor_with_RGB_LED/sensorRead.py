import board
import busio
import time
import adafruit_tcs34725
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tcs34725.TCS34725(i2c)


def get_color():
	return sensor.color_rgb_bytes

