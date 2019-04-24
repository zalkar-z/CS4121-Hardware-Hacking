import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)

p = GPIO.PWM(13, 100)

p.start(0)
time.sleep(5)

#try:
#	while True:
#		for i in range(100):
#			p.ChangeDutyCycle(i)
#			time.sleep(0.02)
#except KeyboardInterrupt:
#	pass

p.stop()
GPIO.cleanup()
