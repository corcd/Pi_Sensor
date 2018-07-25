#人体热释电传感器
import RPi.GPIO as GPIO
import time

Pin = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(Pin, GPIO.IN)

try:
    while True:
        if GPIO.input(Pin) == 1:
            print("true")
        else:
            print("false")
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
