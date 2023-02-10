# from moviepy.editor import *
# import pygame
# import moviepy
# # from pynput import keyboard

# # screen.fill((0, 0, 0))e
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

# # while True:
# #     # The event listener will be running in this block
# #     with keyboard.Events() as events:
# #         event = events.get(1.0)
# #         if event is None:
# #             print('You did not press a key within one second')
# #             started = True
# #             if started is True:
# #                 StartVideo()
# #         else:
# #             print('Received event {}'.format(event))

#     # if !started
#     # startVideo()

# #     with keyboard.Events() as events:
# #         for event in events:
# #             print('Received event {}'.format(event))

#     # if keyboard.press('shift'):
#     #     print("Test")
#     #     break

#     # clip = VideoFileClip('videos/test.mp4').resize((1920, 1080))
#     # clip.preview()
#     # pygame.quit()

#     # if (event.type == pygame.KEYDOWN):
#     #     if (event.type == pygame.K_e):
#     #         break

# # function startVideo() {

# # screen = pygame.display.set_mode((800, 600))
# # screen.fill((0, 0, 0))
# # video = moviepy.editor.VideoFileClip("videos/test.mp4")
# # video.preview()
# # started = true
# # }

import sys
import pygame
import moviepy.editor as mp

pygame.init()

screen = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()

video = mp.VideoFileClip("videos/test-720.mp4")

video.fps = 30

frames = []

for i in range(int(video.fps * video.duration)):
    frames.append(video.get_frame(i / video.fps))

frame_index = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(frames[frame_index], (0, 0))
    pygame.display.update()

    frame_index = (frame_index + 1) % len(frames)

    clock.tick(30)
