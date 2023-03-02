from multiprocessing.connection import wait
from signal import pause
import RPi.GPIO as GPIO
import time
from time import sleep
from subprocess import Popen, PIPE
import pexpect


GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.IN)

videoplayer1 = pexpect.spawn('vlc --intf rc --no-video-title-show --loop')
videoplayer1.sendline('play videos/test-720.mp4')


print("yolo")
buttonPressed = False

while True:
    # if button is not pressed:
    if GPIO.input(24) == 0:
        GPIO.output(23, GPIO.LOW)
        buttonPressed = False

    # if button is pressed:
    else:
        GPIO.output(23, GPIO.HIGH)
        if buttonPressed == False:
            print('xolo2')
            videoplayer1.sendline('pause')
            videoplayer2 = pexpect.spawn('vlc --intf rc --no-video-title-show')
            videoplayer2.sendline('play videos/test2.mp4')
            videoplayer1.sendline('play')
            print('yolo3')
