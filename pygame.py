import pygame 
import random
screen_width , screen_height = 500,400
movement_speed = 5
font_size = 75
pygame.init()
backgroun_image = pygame.transform.scale(pygame.image.load('mario.jpg'), (screen_height,screen_width))
font = pygame.font.Sysfont('times new roman', font_size)
class sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.surface([width, height])
        self.image.fill(
            pygame.color('dodgerblue')
        )
        pygame.draw.rect(self.image, color, pygame(0,0,height,width))
        self,rect = self.image.get_rect()
    
    def move(self, x_change, y_change):
        self.rect.x = max(
            min(self.rect.x + x_change,screen_width - self.rect.width ), 0
        )
        self.rect.y = max(
            min(self.rect.y + y_change,screen_height - self.rect.height ), 0
        )
screen = pygame.display.set_mode((screen_height,screen_width))
pygame.display.set_caption('sprite collision')
all_sprites = pygame.sprite.group()
sprite1 = sprite(pygame.color('black'),20,30)
sprite1.rect.x , sprite1.rect.y = random.randint(
    0, screen_width - sprite1.rect.width), random.randint(
        0, screen_height - sprite1.rect.height
    )
all_sprites.add(sprite1)

sprite2 = sprite(pygame.color('darkred'),20,30)
sprite2.rect.x , sprite2.rect.y = random.randint(
    0, screen_width - sprite2.rect.width), random.randint(
        0, screen_height - sprite2.rect.height
    )
all_sprites.add(sprite2)
running, won = True, False
clock = pygame.time.clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.K_x):
            running = False
    
    if not won :
        keys = pygame.key.get.pressed()
        x_change = (keys[pygame.K_RIGHT- pygame.K_LEFT])* movement_speed
        y_change = (keys[pygame.K_UP- pygame.K_DOWN])* movement_speed
        sprite1.move(x_change,y_change)
    if sprite1.rect.colliderect(sprite2.rect):
            all_sprites.remove(sprite2)
            all_sprites.remove(sprite1)
            won = True

    # Drawing
    screen.blit('mario.jpg', (0, 0))
    all_sprites.draw(screen)

    # Display win message
    if won:
        win_text = font.render("You win!", True, pygame.Color('black'))
        screen.blit(win_text, ((screen_width - win_text.get_width()) // 2,
                               (screen_height - win_text.get_height()) // 2))

    pygame.display.flip()
    clock.tick(90)

pygame.quit()

