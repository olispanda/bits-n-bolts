from multiprocessing.connection import wait
import RPi.GPIO as GPIO
import time
from time import sleep
from subprocess import Popen, PIPE
import pexpect


GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.IN)

buttonPressed = False

# _______________________________________________________________________

videoplayer = pexpect.spawn('vlc --intf rc --no-video-title-show')


def Video1():
    videoplayer.sendline('add videos/test-720.mp4 --loop')
    videoplayer.sendline('play')


Video1

# ________________________________________________________________________

print("yolo")


while True:
    if GPIO.input(24) == 0:
        GPIO.output(23, GPIO.LOW)
        buttonPressed = False
    else:
        GPIO.output(23, GPIO.HIGH)
        if buttonPressed == False:
            print('xolo2')
            videoplayer.sendline('pause')
            buttonPressed = True
        elif buttonPressed == True:
            videoplayer.sendline('add videos/test2.mp4')
            sleep(10)
            print('yolo3')
            buttonPressed == False
            Video1
