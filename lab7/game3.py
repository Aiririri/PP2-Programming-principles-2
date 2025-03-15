import pygame


pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("Interactive Red Circle")


white = (255, 255, 255)
red = (255, 0, 0)


circle_radius = 25
circle_center_x = screen_width // 2
circle_center_y = screen_height // 2
movement_speed = 0.2


running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()

    
    if keys[pygame.K_UP] and circle_center_y - circle_radius - movement_speed >= 0:
        circle_center_y -= movement_speed
    if keys[pygame.K_DOWN] and circle_center_y + circle_radius + movement_speed <= screen_height:
        circle_center_y += movement_speed
    if keys[pygame.K_LEFT] and circle_center_x - circle_radius - movement_speed >= 0:
        circle_center_x -= movement_speed
    if keys[pygame.K_RIGHT] and circle_center_x + circle_radius + movement_speed <= screen_width:
        circle_center_x += movement_speed

    
    screen.fill(white)
    pygame.draw.circle(screen, red, (circle_center_x, circle_center_y), circle_radius)
    pygame.display.flip()


pygame.quit()
