import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

rgb_pins = [15, 13, 11]

GPIO.setup(rgb_pins[0], GPIO.OUT)
red = GPIO.PWM(rgb_pins[0], 100)

GPIO.setup(rgb_pins[1], GPIO.OUT)
green = GPIO.PWM(rgb_pins[1], 100)	

GPIO.setup(rgb_pins[2], GPIO.OUT)
blue = GPIO.PWM(rgb_pins[2], 100)
	
def set_color(rgb_colors):
	red.start(100 - round(rgb_colors[0] / 256 * 100))
	green.start(100 - round(rgb_colors[1] / 256 * 100))
	blue.start(100 - round(rgb_colors[2] / 255 * 100))

def reset():
	red = rgb_pins[0]
	green = rgb_pins[1]
	blue = rgb_pins[2]

	red.stop()
	green.stop()
	blue.stop()

	GPIO.cleanup()

# input_rgb = [0, 0, 0]

# input_rgb[0] = int(input("Enter RED value:"))
# input_rgb[1] = int(input("Enter GREEN value:"))
# input_rgb[2] = int(input("Enter BLUE value:"))

# tri_color(input_rgb)

# time.sleep(5)
# GPIO.cleanup()
