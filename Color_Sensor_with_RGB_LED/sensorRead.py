import board
import busio
import adafruit_tcs34725
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tcs34725.TCS34725(i2c)

print('Color: ({0}, {1}, {2})'.format(*sensor.color_rgb_bytes))
