from sensorRead import get_color
from PWM_All_LEDs import set_color
import time

try:
	while True:
		# get the RGB color array from sensorRead.py
		color = get_color()

		print(color)
		print("------")

		# set the LED to match the color from sensor
		set_color(color)

		# check sensor every 2 seconds and update the LED
		time.sleep(2)
except KeyboardInterrupt:
	pass
