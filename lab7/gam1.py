import pygame
import sys
import time
import math
from datetime import datetime

pygame.init()


WIDTH, HEIGHT = 1400, 1400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

clock_img = pygame.image.load("clock.png")  
long_hand_img = pygame.image.load("hand1.png")  
short_hand_img = pygame.image.load("hand1.png")  

long_hand_img = pygame.transform.scale(long_hand_img, (long_hand_img.get_width(), long_hand_img.get_height() + 40))
short_hand_img = pygame.transform.scale(short_hand_img, (short_hand_img.get_width(), short_hand_img.get_height() - 20))


CENTER = (WIDTH // 2, HEIGHT // 2)


LONG_HAND_OFFSET = (0, 0)  
SHORT_HAND_OFFSET = (0, 30)  

def draw_rotated_hand(image, angle, center, offset):
    """Рисует руку с правильной точкой вращения."""
    rotated_image = pygame.transform.rotate(image, angle)
    rect = rotated_image.get_rect(center=center)
    rect.x += offset[0]  
    rect.y += offset[1]  
    screen.blit(rotated_image, rect.topleft)


running = True
while running:
    screen.fill((255, 255, 255))  

    
    screen.blit(clock_img, clock_img.get_rect(center=CENTER))

    
    now = datetime.now()
    seconds = now.second
    minutes = now.minute

    
    second_angle = -seconds * 6 + 90
    minute_angle = -minutes * 6 + 90

    
    draw_rotated_hand(long_hand_img, minute_angle, CENTER, LONG_HAND_OFFSET)  
    draw_rotated_hand(short_hand_img, second_angle, CENTER, SHORT_HAND_OFFSET)  

    
    pygame.display.flip()

   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    time.sleep(1)

pygame.quit()
sys.exit()
