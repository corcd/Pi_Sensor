#激光发射器
import RPi.GPIO as GPIO
import time

Pin = 17  # GPIO Pin 17

GPIO.setmode(GPIO.BCM)

# Setup light sensor pin status
GPIO.setup(Pin, GPIO.OUT)
time.sleep(0.5)
GPIO.setwarnings(False)

try:
    print("RAY On")
    while True:
        GPIO.output(Pin, GPIO.HIGH)
        time.sleep(2)

except (KeyboardInterrupt, SystemExit):
    GPIO.output(Pin, GPIO.HIGH)
    GPIO.cleanup()
    print("RAY OFF")
    pass
