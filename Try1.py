import pygame
import sys

# مقداردهی اولیهٔ pygame
pygame.init()

# تنظیمات صفحه نمایش
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("قایق روی آب")

# رنگ‌ها
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# تعریف قایق
boat_width = 100
boat_height = 20
boat = pygame.Rect(screen_width // 2 - boat_width // 2, screen_height // 2, boat_width, boat_height)

# حرکت موج
wave_offset = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # حرکت موج
    wave_offset += 1
    wave_y = int(10 * pygame.math.sin(pygame.time.get_ticks() / 500))

    # رسم زمینه
    screen.fill(BLUE)

    # رسم قایق
    boat.y = screen_height // 2 + wave_y
    pygame.draw.rect(screen, WHITE, boat)

    pygame.display.flip()
    clock.tick(60)
