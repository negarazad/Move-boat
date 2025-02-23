import pygame
import math

# تنظیمات اولیه
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

# تنظیمات قایق و موج
boat_width, boat_height = 50, 20
boat_color = (0, 0, 255)
wave_color = (173, 216, 230)
wave_amplitude = 50
wave_frequency = 0.02
speed = 2

# تابع برای رسم قایق
def draw_boat(x, y):
    pygame.draw.polygon(screen, boat_color, [
        (x, y), (x - boat_width // 2, y + boat_height),
        (x + boat_width // 2, y + boat_height)
    ])

# تابع برای رسم موج
def draw_wave(offset):
    for x in range(0, width):
        y = height // 2 + wave_amplitude * math.sin(wave_frequency * (x + offset))
        pygame.draw.line(screen, wave_color, (x, height // 2), (x, y))

# حلقه‌ی اصلی
x = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    # رسم موج
    draw_wave(x)

    # محاسبه‌ی موقعیت قایق
    y = height // 2 + wave_amplitude * math.sin(wave_frequency * x)
    draw_boat(x % width, y)

    pygame.display.flip()
    clock.tick(60)
    x += speed

pygame.quit()
