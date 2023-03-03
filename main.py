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

print("initial play video")
videoplayer1 = pexpect.spawn(
    'vlc --no-video-title-show --loop bits-n-bolts/videos/video1.mp4')
videoplayer1.sendline('add videos/video1.mp4')
videoplayer1.sendline('play')
print("video 1 started for the first time")


while True:
    # if button is not pressed:
    if GPIO.input(24) == 0:
        GPIO.output(23, GPIO.LOW)

    # if button is pressed:
    else:
        GPIO.output(23, GPIO.HIGH)
        print("button has been pressed")
        print("trying to quit video 1")
        videoplayer1.sendline('quit')
        videoplayer1.close()
        print("video 1 has been closed")
        print("trying to start video 2")
        videoplayer2 = pexpect.spawn(
            'vlc --no-video-title-show bits-n-bolts/videos/video2.mp4')
        videoplayer2.sendline('add videos/video2.mp4')
        videoplayer2.sendline('play')
        print("video 2 has been started... waiting for 42 seconds")
        sleep(42)
        print("wait over. trying to quit video 2")
        videoplayer2.sendline('quit')
        videoplayer2.close()
        print("video 2 has been terminated")
        print("trying to start video 1 again")
        videoplayer1 = pexpect.spawn(
            'vlc --no-video-title-show --loop bits-n-bolts/videos/video1.mp4')
        videoplayer1.sendline('add videos/video1.mp4')
        videoplayer1.sendline('play')
        print("video 1 started again...")
