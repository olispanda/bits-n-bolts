# # from moviepy.editor import *
# # import pygame
# import moviepy
# # # from pynput import keyboard

# import moviepy.editor as mp
# import pygame
# import sys
# screen = pygame.display.set_mode((800, 600))
# video = moviepy.editor.VideoFileClip("videos/test-720.mp4")
# let = currentSecond = 1
# while True:
#     video.show(currentSecond/10)
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             if event.unicode == 'e':
#                 print('du hast die richtige taste gedrückt')
#     currentSecond = currentSecond + 1

# # # while True:
# # #     # The event listener will be running in this block
# # #     with keyboard.Events() as events:
# # #         event = events.get(1.0)
# # #         if event is None:
# # #             print('You did not press a key within one second')
# # #             started = True
# # #             if started is True:
# # #                 StartVideo()
# # #         else:
# # #             print('Received event {}'.format(event))

# #     # if !started
# #     # startVideo()

# # #     with keyboard.Events() as events:
# # #         for event in events:
# # #             print('Received event {}'.format(event))

# #     # if keyboard.press('shift'):
# #     #     print("Test")
# #     #     break

# #     # clip = VideoFileClip('videos/test.mp4').resize((1920, 1080))
# #     # clip.preview()
# #     # pygame.quit()

# #     # if (event.type == pygame.KEYDOWN):
# #     #     if (event.type == pygame.K_e):
# #     #         break

# # # function startVideo() {

# # # screen = pygame.display.set_mode((800, 600))
# # # screen.fill((0, 0, 0))
# # # video = moviepy.editor.VideoFileClip("videos/test.mp4")
# # # video.preview()
# # # started = true
# # # }


# # pygame.init()

# # screen = pygame.display.set_mode((640, 480))

# # clock = pygame.time.Clock()

# # video = mp.VideoFileClip("videos/test-720.mp4")

# # video.fps = 30

# # frames = []

# # for i in range(int(video.fps * video.duration)):
# #     frames.append(video.get_frame(i / video.fps))

# # frame_index = 0

# # while True:
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             pygame.quit()
# #             sys.exit()

# #     screen.blit(frames[frame_index], (0, 0))
# #     pygame.display.update()

# #     frame_index = (frame_index + 1) % len(frames)

# #     clock.tick(30)

# import cv2

# cap = cv2.VideoCapture("videos/test-720.mp4")

# while True:
#     ret, frame = cap.read()

#     if not ret:
#         break

#     cv2.imshow("video", frame)

#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

# cap.release()
# cv2.destroyAllWindows()

# import pyglet

# # width of window
# width = 500

# # height of window
# height = 500

# # caption i.e title of the window
# title = "Geeksforgeeks"

# # creating a window
# window = pyglet.window.Window(width, height, title)


# # video path
# vidPath = "videos/test-720.mp4"

# # creating a media player object
# player = pyglet.media.Player()

# # creating a source object
# source = pyglet.media.StreamingSource()

# # load the media from the source
# MediaLoad = pyglet.media.load(vidPath)

# # add this media in the queue
# player.queue(MediaLoad)

# # play the video
# player.play()

# import thread
import RPi.GPIO as GPIO
import time
from subprocess import Popen


GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.IN)

# VIDEO_CLIP_IDLE = "videos/test-720.mp4"
# video_player = Popen(['vlc', '--fullscreen', '--loop',
#                       '--no-video-title-show', '--no-audio', '--quiet', VIDEO_CLIP_IDLE])

video_player = Popen(['vlc', '--intf rc'])
video_player.communicate('add videos/test-720.mp4')
video_player.communicate('play')
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
