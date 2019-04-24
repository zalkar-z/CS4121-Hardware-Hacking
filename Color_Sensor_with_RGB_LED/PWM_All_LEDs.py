import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

rgb_pins = [15, 13, 11]

def tri_color(rgb_colors):

	GPIO.setup(rgb_pins[0], GPIO.OUT)
	red = GPIO.PWM(rgb_pins[0], 100)
	red.start(100 - round(rgb_colors[0] / 255 * 100))

	GPIO.setup(rgb_pins[1], GPIO.OUT)
	green = GPIO.PWM(rgb_pins[1], 100)
	green.start(100 - round(rgb_colors[1] / 255 * 100))
	
	GPIO.setup(rgb_pins[2], GPIO.OUT)
	blue = GPIO.PWM(rgb_pins[2], 100)
	blue.start(100 - round(rgb_colors[2] / 255 * 100))
	
	time.sleep(5)	

	red.stop()
	green.stop()
	blue.stop()

input_rgb = [0, 0, 0]

input_rgb[0] = int(input("Enter RED value:"))
input_rgb[1] = int(input("Enter GREEN value:"))
input_rgb[2] = int(input("Enter BLUE value:"))

tri_color(input_rgb)

# time.sleep(5)
GPIO.cleanup()
