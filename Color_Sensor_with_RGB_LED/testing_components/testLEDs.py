import RPi.GPIO as GPIO
import time

red = 15
green = 13
blue = 11

pins = [red, green, blue]

for pin in pins:
	# turn off according pin to turn on a particular color
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, 0)

	# display it for 5 seconds
	time.sleep(5)

	# clean up pins
	GPIO.cleanup()
