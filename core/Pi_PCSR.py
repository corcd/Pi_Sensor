#超声波测距传感器
import RPi.GPIO as GPIO
import time
import math

Trig_Pin = 20  #超声波发送脚
Echo_Pin = 21  #超声波接收检测脚

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(Trig_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Echo_Pin, GPIO.IN)

time.sleep(1)


def checkdist():
    GPIO.output(Trig_Pin, GPIO.HIGH)
    time.sleep(0.00015)
    GPIO.output(Trig_Pin, GPIO.LOW)
    while not GPIO.input(Echo_Pin):
        pass
    t1 = time.time()
    while GPIO.input(Echo_Pin):
        pass
    t2 = time.time()
    return (t2 - t1) * 340 * 100 // 2


temp = checkdist()
print(round(temp))
GPIO.cleanup()
