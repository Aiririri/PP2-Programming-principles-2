import pygame
import random

pygame.init()

# Constants for window size
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
SNAKE_COLOR = (0, 122, 41)
BG_COLOR = (0, 0, 0)

# Food types with colors, points, and lifespan
FOOD_TYPES = {
    "small": ((235, 89, 16), 1, 300),  # +1 point, disappears after 300 cycles
    "medium": ((0, 200, 255), 2, 200),  # +2 points, disappears after 200 cycles
    "big": ((255, 255, 0), 3, 100)  # +3 points, disappears after 100 cycles
}

# Movement directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Game settings
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Initial snake parameters
snake = [(WIDTH // 2, HEIGHT // 2)]
direction = RIGHT

# Function to generate food
def generate_food():
    food_type = random.choice(list(FOOD_TYPES.keys()))  # Randomly select food type
    position = (random.randrange(0, WIDTH, GRID_SIZE), random.randrange(0, HEIGHT, GRID_SIZE))
    return {"pos": position, "color": FOOD_TYPES[food_type][0], "value": FOOD_TYPES[food_type][1], "timer": FOOD_TYPES[food_type][2]}

food = generate_food()
score = 0
level = 1
speed = 10

running = True
while running:
    screen.fill(BG_COLOR)

    # Event handling
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

    # Move the snake
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0] * GRID_SIZE, head_y + direction[1] * GRID_SIZE)

    # Check for collisions with walls
    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
        running = False
        continue

    # Check for collisions with itself
    if new_head in snake:
        running = False
        continue

    # Add new head to the snake
    snake.insert(0, new_head)

    # Check if food is eaten
    if new_head == food["pos"]:
        score += food["value"]
        food = generate_food()
        if score % 5 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()  # Remove last segment if food was not eaten

    # Draw food
    pygame.draw.rect(screen, food["color"], (*food["pos"], GRID_SIZE, GRID_SIZE))
    
    # Decrease food timer, generate new food if expired
    food["timer"] -= 1
    if food["timer"] <= 0:
        food = generate_food()

    # Draw the snake
    for segment in snake:
        pygame.draw.rect(screen, SNAKE_COLOR, (*segment, GRID_SIZE, GRID_SIZE))

    # Display score and level
    font = pygame.font.Font(None, 24)
    score_text = font.render(f"Score: {score}  Level: {level}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()