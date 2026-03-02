import something
something.init()
screen = something.display.set_mode((1080,720))
done = False
while not done:
    for event in something.event.get():
        if event.type == something.QUIT:
            something.quit()
    something.display.flip()
    