import RPi.GPIO as GPIO
import time

# set GPIO mode to physical pins
GPIO.setmode(GPIO.BOARD)

# an array with physical addresses of RGB respectively
rgb_pins = [15, 13, 11]

# an empty list for later use of PWM objects
colors = []

# set all three color pins in PWM mode
for i in range(3):
	GPIO.setup(rgb_pins[i], GPIO.OUT)
	colors.append(GPIO.PWM(rgb_pins[i], 100))

#
# Function: changes LED's colors
# rgb_colors - an array of size 3
#
def set_color(rgb_colors):
	# convert passed values to display on LED
	for i in range(3):
		# since my LED is common-anode, "0" here means the brightest (255) and vice-versa
		colors[i].start(100 - round(rgb_colors[i] / 255 * 100))

