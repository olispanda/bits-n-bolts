from moviepy.editor import *
import pygame
import moviepy
from pynput import keyboard

# import keyboard
# while True:
#     if keyboard.is_pressed("e"):
#         print("Test")
#         break


# function startVideo() {

# screen = pygame.display.set_mode((800, 600))
# screen.fill((0, 0, 0))
# video = moviepy.editor.VideoFileClip("videos/test.mp4")
# video.preview()
# started = true
# }

while True:
    # The event listener will be running in this block
    with keyboard.Events() as events:
        # Block at most one second
        event = events.get(1.0)
        if event is None:
            print('You did not press a key within one second')
        else:
            print('Received event {}'.format(event))

    # if !started
    # startVideo()

#     with keyboard.Events() as events:
#         for event in events:
#             print('Received event {}'.format(event))

    # if keyboard.press('shift'):
    #     print("Test")
    #     break

    # clip = VideoFileClip('videos/test.mp4').resize((1920, 1080))
    # clip.preview()
    # pygame.quit()

    # if (event.type == pygame.KEYDOWN):
    #     if (event.type == pygame.K_e):
    #         break
