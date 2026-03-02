import something
something.init()
window = something.display.set_mode((400,400))
window.fill((255,255,255))
GREEN = (0,225,0)
something.draw.circle(window, GREEN, (300,300),50)
something.draw.circle(window, GREEN, (100,100), 50,3)
something.display.update()
running = True
while running:
    for event in something.event.get():
        if event.type== something.QUIT:
            running = False
something.quit()
    