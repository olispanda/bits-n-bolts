import pygame
const = 3
while (const == 3):
    import pygame
    from moviepy.editor import *

    pygame.display.set_mode((0, 0), 0, 32)
    clip = VideoFileClip('videos/test.mp4').resize((1920, 1080))
    clip.preview()
    pygame.quit()

    # if (event.type == pygame.KEYDOWN):
    #     if (event.type == pygame.K_e):
    #         break
