import pygame

pygame.init()
pygame.mixer.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Keyboard Music Player")


pygame.font.init()
font = pygame.font.Font(None, 36)  


playlist = ["genshin.mp3", "friendzona5.mp3", "nabitanuma.mp3"]  
current_song_index = 0

def play_song(index):
    
    try:
        pygame.mixer.music.load(playlist[index])
        pygame.mixer.music.play()
    except pygame.error as e:
        print(f"Error loading music file: {e}")

play_song(current_song_index)

running = True
while running:
    screen.fill((0, 0, 0))    

    
    text = font.render(f"Playing: {playlist[current_song_index]}", True, (255, 255, 255))
    instructions = font.render("SPACE: Play/Pause | UP: Previous | DOWN: Next", True, (200, 200, 200))
    screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - 20))
    screen.blit(instructions, (screen_width // 2 - instructions.get_width() // 2, screen_height // 2 + 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_DOWN:  
                current_song_index = (current_song_index + 1) % len(playlist)
                play_song(current_song_index)
            elif event.key == pygame.K_UP:  
                current_song_index = (current_song_index - 1) % len(playlist)
                play_song(current_song_index)

    pygame.display.update()

pygame.quit()
