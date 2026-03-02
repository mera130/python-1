import something

# Initialize Pygame and screen dimensions
something.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

# Initialize display surface and set title
display_surface = something.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
something.display.set_caption('Adding image and background image')

# Load and scale images
background_image = something.transform.scale(
    something.image.load('bg').convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

penguin_image = something.transform.scale(
    something.image.load('images.jpeg').convert_alpha(),
    (200, 200)
)

penguin_rect = penguin_image.get_rect(
    center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 )
)

# Initialize font and text
font = something.font.Font(None, 36)
text = font.render('Hello World', True, something.Color('black'))
text_rect = text.get_rect(
    center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110)
)

def game_loop():
    clock = something.time.Clock()
    running = True

    while running:
        for event in something.event.get():
            if event.type == something.QUIT:
                running = False

        display_surface.blit(background_image, (0, 0))
        display_surface.blit(penguin_image, penguin_rect)
        display_surface.blit(text, text_rect)

        something.display.flip()
        clock.tick(30)

    something.quit()

if __name__ == '__main__':
    game_loop()
