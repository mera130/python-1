import turtle 
turtle.Screen().bgcolor('#C4A484')
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()

side = 4

length = 70
angle = 360/side
polygon.color('#B87C4C')
polygon.begin_fill()

for i in range(side):
    polygon.forward(length)
    polygon.right(angle)
polygon.end_fill()
turtle.done()