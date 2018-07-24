#人体热释电传感器
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.IN)

try:
  while True:
    if GPIO.input(5) == 1:
      print ("Some people here!")
    else:
      print ("Nobody!")
    time.sleep(.1)
except KeyboardInterrupt:
  GPIO.cleanup()
