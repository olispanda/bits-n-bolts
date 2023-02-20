# import thread
import RPi.GPIO as GPIO
import time
from subprocess import Popen, PIPE


GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.IN)

# VIDEO_CLIP_IDLE = "videos/test-720.mp4"
# video_player = Popen(['vlc', '--fullscreen', '--loop',
#                       '--no-video-title-show', '--no-audio', '--quiet', VIDEO_CLIP_IDLE])

video_player = Popen(['vlc', '--intf', 'rc'], stdin=PIPE)
out, err = video_player.communicate(input=b'play')
print(out)


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
            buttonPressed = True

        # # import pygame
        # # from RPi import GPIO

        # video_player = Popen(['vlc', '--fullscreen', '--loop',
        #                      '--no-video-title-show', '--no-audio', '--quiet', VIDEO_CLIP_IDLE])
        # while True:
        #     for event in pygame.event.get():
        #         if event.type == pygame.KEYDOWN:
        #             if event.unicode == 'x':
        #                 print('du hast die richtige taste gedrückt')
