import pygame
import random
pygame.init()
SPRITE_COLOR_EVENT_CHANGE = pygame.USEREVENT+1
background_COLOR_EVENT_CHANGE = pygame.USEREVENT+2
blue = pygame.color('blue')
light_blue = pygame.color('light blue')
dark_blue = pygame.color('dark blue')

yellow = pygame.color('yellow')
magenta = pygame.color('megenta')
orange = pygame.color('orange')
white = pygame.color('white')

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.surface([height,width])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice(-1,1), random.choice(-1,1)]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False
        if self.rect.left <= self.rect.right >= 500:
            self.velocity[0] = self.velocity[0]
            boundary_hit = True
        if self.rect.top <= self.rect.bottom >= 400:
          self.velocity[1] = self.velocity[1]
          boundary_hit = True
        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_EVENT_CHANGE))
            pygame.event.post(pygame.event.Event(background_COLOR_EVENT_CHANGE))
    def color_change(self):
        self.image.fill(random.choice([yellow, magenta, orange,white]))
        
def change_background_color():
    global bg_color
    bg_color = random.choice([blue, light_blue, dark_blue])
    
all_sprite_list = pygame.sprite.group()
sp1 = Sprite(white,20,30)
sp1.rect.x = random.randint
