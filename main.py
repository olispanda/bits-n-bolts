from time import sleep
from moviepy.editor import *
import threading
import RPi.GPIO as GPIOs
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.IN)


def loop():
    while True:
        pass
        # loop vid


def button():
    while True:
        print("checking")
        if GPIO.input(24) == 1:
            GPIO.output(23, GPIO.HIGH)
            print('button was pressed')
        else:
            pass


global x
x = threading.Thread(target=loop)
x.start()
y = threading.Thread(target=button)
y.start()
