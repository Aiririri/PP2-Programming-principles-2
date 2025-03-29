import pygame
import random


pygame.init()

WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
SNAKE_COLOR = (0, 122, 41)
FOOD_COLOR = (235, 89, 16)
BG_COLOR = (0, 0, 0)


UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

snake = [(WIDTH // 2, HEIGHT // 2)]
direction = RIGHT
food = (random.randrange(0, WIDTH, GRID_SIZE), random.randrange(0, HEIGHT, GRID_SIZE))
score = 0
level = 1
speed = 10


def generate_food():
    while True:
        new_food = (random.randrange(0, WIDTH, GRID_SIZE), random.randrange(0, HEIGHT, GRID_SIZE))
        if new_food not in snake:
            return new_food


running = True
while running:
    screen.fill(BG_COLOR)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != DOWN:
                direction = UP
            elif event.key == pygame.K_DOWN and direction != UP:
                direction = DOWN
            elif event.key == pygame.K_LEFT and direction != RIGHT:
                direction = LEFT
            elif event.key == pygame.K_RIGHT and direction != LEFT:
                direction = RIGHT
    
   
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0] * GRID_SIZE, head_y + direction[1] * GRID_SIZE)
    
    
    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
        running = False
        continue
    
    
    if new_head in snake:
        running = False
        continue
    
   
    snake.insert(0, new_head)
    
    
    if new_head == food:
        score += 1
        food = generate_food()
        
        if score % 3 == 0:
            level += 1
            speed += 2  
    else:
        snake.pop()  
    
    
    pygame.draw.rect(screen, FOOD_COLOR, (*food, GRID_SIZE, GRID_SIZE))
    
   
    for segment in snake:
        pygame.draw.rect(screen, SNAKE_COLOR, (*segment, GRID_SIZE, GRID_SIZE))
    
    
    font = pygame.font.Font(None, 24)
    score_text = font.render(f"Score: {score}  Level: {level}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
