#光线传感器
import RPi.GPIO as GPIO
import time

Pin = 26  # GPIO Pin 26

GPIO.setmode(GPIO.BCM)
time.sleep(1)
# Setup light sensor pin status
GPIO.setup(Pin, GPIO.OUT)
GPIO.output(Pin, GPIO.LOW)
time.sleep(0.5)
GPIO.output(Pin, GPIO.HIGH)
GPIO.setup(Pin, GPIO.IN)

try:
    print("LDR Online")
    i = 0
    while True:
        v = GPIO.input(Pin)
        print(v)
        if v == GPIO.LOW:
            i = i + 1
            print("LOW")
        if v == GPIO.HIGH:
            print("HIGH")
        time.sleep(2)

except (KeyboardInterrupt, SystemExit):
    GPIO.cleanup()
    print("LDR Outline")
    pass
