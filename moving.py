import something

def main():
    something.init()
    screen_width, screen_height = 500, 500
    screen = something.display.set_mode((screen_width, screen_height))
    something.display.set_caption('color changing sprite')

    # Mapping of color names to RGB values
    colors = {
        'red': something.Color('red'),
        'green': something.Color('green'),
        'blue': something.Color('blue'),
        'yellow': something.Color('yellow'),
        'white': something.Color('white')
    }
    current_color = colors['white']

    x, y = 30, 30
    sprite_width, sprite_height = 60, 60

    clock = something.time.Clock()

    done = False
    while not done:
        for event in something.event.get():
            if event.type == something.QUIT:
                done = True

        pressed = something.key.get_pressed()
        if pressed[something.K_LEFT]: x -= 3
        if pressed[something.K_RIGHT]: x += 3
        if pressed[something.K_UP]: y -= 3
        if pressed[something.K_DOWN]: y += 3

        x = min(max(0, x), screen_width - sprite_width)
        y = min(max(0, y), screen_height - sprite_height)

        if x == 0: current_color = colors['blue']
        elif x == screen_width - sprite_width: current_color = colors['yellow']
        elif y == 0: current_color = colors['red']
        elif y == screen_height - sprite_height:
            current_color = colors['green']
        else:
            current_color = colors['white']

        screen.fill((0, 0, 0))
        something.draw.rect(screen, current_color,
                         (x, y, sprite_width, sprite_height))
        something.display.flip()
        clock.tick(90)

    something.quit()


if __name__ == "__main__":
    main()
