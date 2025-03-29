import pygame
import tkinter as tk
from tkinter import colorchooser

def pick_color():
    root = tk.Tk()
    root.withdraw()
    color_code = colorchooser.askcolor(title="Choose color")[0]
    return (int(color_code[0]), int(color_code[1]), int(color_code[2])) if color_code else None

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'blue'
    draw_mode = 'line'
    points = []
    rect_start, rect_end = None, None
    circle_start, circle_end = None, None
    custom_color = (0, 0, 255)
    
    
    eraser_icon = pygame.image.load("eraser.png")
    rectangle_icon = pygame.image.load("rectangle.png")
    circle_icon = pygame.image.load("circle.png")
    
    eraser_icon = pygame.transform.scale(eraser_icon, (50, 50))
    rectangle_icon = pygame.transform.scale(rectangle_icon, (50, 50))
    circle_icon = pygame.transform.scale(circle_icon, (50, 50))
    
    while True:
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                
                
                if 10 <= mouse_x <= 60:
                    if 10 <= mouse_y <= 60:
                        draw_mode = 'eraser'
                    elif 70 <= mouse_y <= 120:
                        draw_mode = 'rect'
                    elif 130 <= mouse_y <= 180:
                        draw_mode = 'circle'
                else:
                    if draw_mode == 'rect':
                        rect_start = event.pos
                    elif draw_mode == 'circle':
                        circle_start = event.pos
                    elif event.button == 1:
                        radius = min(200, radius + 1)
                    elif event.button == 3:
                        radius = max(1, radius - 1)
                
            if event.type == pygame.MOUSEBUTTONUP:
                if draw_mode == 'rect' and rect_start:
                    rect_end = event.pos
                    pygame.draw.rect(screen, custom_color if mode == 'custom' else (255, 255, 255), (*rect_start, rect_end[0] - rect_start[0], rect_end[1] - rect_start[1]), 2)
                    rect_start = None
                elif draw_mode == 'circle' and circle_start:
                    circle_end = event.pos
                    radius = int(((circle_end[0] - circle_start[0]) ** 2 + (circle_end[1] - circle_start[1]) ** 2) ** 0.5)
                    pygame.draw.circle(screen, custom_color if mode == 'custom' else (255, 255, 255), circle_start, radius, 2)
                    circle_start = None
                
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                if draw_mode == 'line' or draw_mode == 'eraser':
                    points.append((position, draw_mode == 'eraser'))
                    points = points[-256:]
        
        screen.fill((0, 0, 0))
        
        for i in range(len(points) - 1):
            p1, erase = points[i]
            p2, _ = points[i + 1]
            drawLineBetween(screen, i, p1, p2, radius, mode, erase, custom_color)
        
       
        screen.blit(eraser_icon, (10, 10))
        screen.blit(rectangle_icon, (10, 70))
        screen.blit(circle_icon, (10, 130))
        
        
        if draw_mode == 'rect' and rect_start:
            mouse_pos = pygame.mouse.get_pos()
            pygame.draw.rect(screen, (255, 255, 255), (*rect_start, mouse_pos[0] - rect_start[0], mouse_pos[1] - rect_start[1]), 1)
        
        
        if draw_mode == 'circle' and circle_start:
            mouse_pos = pygame.mouse.get_pos()
            radius = int(((mouse_pos[0] - circle_start[0]) ** 2 + (mouse_pos[1] - circle_start[1]) ** 2) ** 0.5)
            pygame.draw.circle(screen, (255, 255, 255), circle_start, radius, 1)
        
        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode, erase, custom_color):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    elif color_mode == 'custom':
        color = custom_color
    
    if erase:
        color = (0, 0, 0)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()
