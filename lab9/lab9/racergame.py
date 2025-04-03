import pygame
import random



pygame.init()

#screen parameters

screen_width = 1980
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Racer with Coins")
clock = pygame.time.Clock()
fps = 90

#colors

white = (255, 255, 255)
black= (0, 0, 0)

#background

background = pygame.image.load("road.png").convert()
background = pygame.transform.scale(background, (600, screen_height)) 
background_rect = background.get_rect()
background_y = 0
scroll_speed = 5

#road in the center

road_x = (screen_width - background_rect.width) // 2  

#player class

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("car.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 140))  
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width // 2
        self.rect.bottom = screen_height - 20

    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT] and self.rect.left > road_x:
            self.rect.x -= 5
        if keystate[pygame.K_RIGHT] and self.rect.right < road_x + background_rect.width:
            self.rect.x += 5

#enemy class

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 140)) 
        self.rect = self.image.get_rect()
        self.reset_position()

    def reset_position(self):
        self.rect.x = random.randrange(road_x, road_x + background_rect.width - self.rect.width)
        self.rect.y = random.randrange(-300, -100)
        self.speed_y = random.randint(5, 10)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > screen_height:
            self.reset_position()

# coin class

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))  
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(road_x, road_x + background_rect.width - self.rect.width)
        self.rect.y = random.randrange(-300, -50)
        self.value = random.choice([1, 2, 3]) # different coins value
        self.speed_y = 5

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > screen_height:
            self.kill()


# sprites group

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

#speed
enemy_speed = 5
for _ in range(3):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

#coins counter

coins_collected = 0
font = pygame.font.SysFont( "timesnewroman", 36)

#counter on the screen

def draw_text(surface, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topright = (x, y)
    surface.blit(text_surface, text_rect)

# enemy max acceleration

speed_up = 10

#game loop

running = True
coin_spawn_rate = 60
frame_count = 0

while running:
    clock.tick(fps)
    frame_count += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

    #sprite update
    all_sprites.update()

    #background scroll

    background_y += scroll_speed
    if background_y >= background_rect.height:
        background_y = 0

    # coins appearence
  
    if frame_count % coin_spawn_rate == 0:
        coin = Coin()
        all_sprites.add(coin)
        coins.add(coin)

   
    if pygame.sprite.spritecollide(player, enemies, False):
        running = False  


    coin_hits = pygame.sprite.spritecollide(player, coins, True)
    for hit in coin_hits:
        coins_collected += hit.value 

        if coins_collected % speed_up == 0:
            enemy_speed += 1
            for enemy in enemies:
                enemy.speed_y = enemy_speed


    screen.fill(white)
    screen.blit(background, (road_x, background_y))
    screen.blit(background, (road_x, background_y - background_rect.height))
    all_sprites.draw(screen)
    draw_text(screen, f"Coins: {coins_collected}", font, black, screen_width // 4, 100)

    pygame.display.flip()

pygame.quit()
