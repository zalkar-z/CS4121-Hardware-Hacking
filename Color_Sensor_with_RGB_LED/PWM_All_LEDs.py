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

