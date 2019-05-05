import sensorRead as sensor
import PWM_All_LEDs as LED
import time

old_color = [0, 0, 0]

try:
	while True:
		color = sensor.get_color()
		print(color)
		if color != old_color:
			LED.reset()
			LED.set_color(color)
		
		old_color = color
		time.sleep(2)
except KeyboardInterrupt:
	pass
