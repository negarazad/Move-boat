import pygame
import sys
import math

# تنظیمات اولیه
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("انیمیشن قایق روی امواج دریا")

# ایجاد تصویر قایق با طراحی واقعی‌تر
boat_image = pygame.Surface((120, 60), pygame.SRCALPHA)
pygame.draw.ellipse(boat_image, (139, 69, 19), (10, 30, 100, 20))  # بدنه قایق
pygame.draw.rect(boat_image, (210, 180, 140), (40, 5, 40, 25))  # عرشه قایق
pygame.draw.polygon(boat_image, (255, 255, 255), [(60, 5), (60, -30), (90, 5)])  # بادبان
boat_rect = boat_image.get_rect(center=(400, 300))

# تنظیمات امواج
wave_amplitude = 50
wave_frequency = 0.05
clock = pygame.time.Clock()

# حلقه اصلی انیمیشن
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # محاسبه موقعیت قایق
    time = pygame.time.get_ticks() * 0.001
    boat_rect.y = 300 + wave_amplitude * math.sin(wave_frequency * time)  # حرکت عمودی
    boat_rect.x = 400 + wave_amplitude * math.cos(wave_frequency * time)  # حرکت افقی

    # رسم پس‌زمینه و قایق
    screen.fill((135, 206, 235))  # رنگ آسمان
    pygame.draw.rect(screen, (0, 0, 255), (0, 350, 800, 250))  # رنگ دریا
    screen.blit(boat_image, boat_rect)

    pygame.display.flip()
    clock.tick(60)
