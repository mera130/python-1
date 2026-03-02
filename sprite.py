import something
import random

something.init()
SPRITE_COLOR_CHANGE_EVENT = something.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = something.USEREVENT + 2

# Background colors
BLUE = something.Color('blue')
LIGHTBLUE = something.Color('lightblue')
DARKBLUE = something.Color('darkblue')

# Sprite colors
YELLOW = something.Color('yellow')
MAGENTA = something.Color('magenta')
ORANGE = something.Color('orange')
WHITE = something.Color('white')


class Sprite(something.sprite.Sprite):


  def __init__(self, color, height, width):

    super().__init__()
    self.image = something.Surface([width, height])
    self.image.fill(color)
    
    self.rect = self.image.get_rect()
    self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

  def update(self):

    self.rect.move_ip(self.velocity)
    boundary_hit = False
    if self.rect.left <= 0 or self.rect.right >= 500:
      self.velocity[0] = -self.velocity[0]
      boundary_hit = True
    if self.rect.top <= 0 or self.rect.bottom >= 400:
      self.velocity[1] = -self.velocity[1]
      boundary_hit = True

    if boundary_hit:
      something.event.post(something.event.Event(SPRITE_COLOR_CHANGE_EVENT))
      something.event.post(something.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))
  def change_color(self):
    self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE, WHITE]))

def change_background_color():
  global bg_color
  bg_color = random.choice([BLUE, LIGHTBLUE, DARKBLUE])



all_sprites_list = something.sprite.Group()
sp1 = Sprite(WHITE, 20, 30)

sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)

all_sprites_list.add(sp1)

screen = something.display.set_mode((500, 400))

something.display.set_caption("Boundary Sprite")

bg_color = BLUE

screen.fill(bg_color)

exit = False
clock = something.time.Clock()

while not exit:
  for event in something.event.get():
    if event.type == something.QUIT:
      exit = True
    elif event.type == SPRITE_COLOR_CHANGE_EVENT:
      sp1.change_color()

    elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
      change_background_color()


  all_sprites_list.update()
  screen.fill(bg_color)

  all_sprites_list.draw(screen)

  something.display.flip()
  clock.tick(240)
something.quit()
