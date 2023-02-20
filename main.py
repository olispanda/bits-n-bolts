# import thread
from multiprocessing.connection import wait
import RPi.GPIO as GPIO
import time
from time import sleep
from subprocess import Popen, PIPE
import pexpect


GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.IN)

# VIDEO_CLIP_IDLE = "videos/test-720.mp4"
# video_player = Popen(['vlc', '--fullscreen', '--loop',
#                       '--no-video-title-show', '--no-audio', '--quiet', VIDEO_CLIP_IDLE])

# video_player = Popen(['vlc', '--intf', 'rc'], stdin=PIPE)
# video_player.stdin.write('help')

videoplayer = pexpect.spawn('vlc --intf rc --no-video-title-show --loop')
videoplayer.sendline('add videos/test-720.mp4')
videoplayer.sendline('play')


print("yolo")

buttonPressed = False

while True:
    # if button off
    if GPIO.input(24) == 0:
        GPIO.output(23, GPIO.LOW)
        buttonPressed = False
    # if button on
    else:
        GPIO.output(23, GPIO.HIGH)
        if buttonPressed == False:
            print('xolo2')
            videoplayer.sendline('pause')
            buttonPressed = True
            if buttonPressed == True:
                videoplayer.sendline('add videos/test2.mp4')
                sleep(10)
                print('yolo3')
                # break

        # # import pygame
        # # from RPi import GPIO

        # video_player = Popen(['vlc', '--fullscreen', '--loop',
        #                      '--no-video-title-show', '--no-audio', '--quiet', VIDEO_CLIP_IDLE])
        # while True:
        #     for event in pygame.event.get():
        #         if event.type == pygame.KEYDOWN:
        #             if event.unicode == 'x':
        #                 print('du hast die richtige taste gedrückt')
