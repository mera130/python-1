import turtle 
turtle.Screen().bgcolor('#53629E')
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()

side = 6
length = 70
angle = 360/side
polygon.color('blue')
polygon.begin_fill()

for i in range(side):
    polygon.forward(length)
    polygon.right(angle)
polygon.end_fill()
turtle.done()