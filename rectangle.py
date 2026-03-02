import something
something.init()
screen = something.display.set_mode((400,300))
done = False 
while not done:
    for event in something.event.get():
     if event.type == something.QUIT:
         done = True
    something.draw.rect(screen,(0,125,125,), something.rect(30,30,60,60))
    something.display.flip()
        
