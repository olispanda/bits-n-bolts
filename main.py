import pygame
const = 3
while (const == 3):
    from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
    import pygame

    pygame.display.set_mode((0, 0), 0, 32)
    clip = VideoFileClip('/bitsnbolts/videos/test.mp4').resize((800, 480))
    clip.preview()

    if (event.type == pygame.KEYDOWN):
        if (event.type == pygame.K_e):
            break
