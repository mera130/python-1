import turtle
turtle.Screen().bgcolor("#BBC863")
turtle.Screen().title("TURTLE")
my_pen = turtle.Turtle()
size =0
while True:
    for i in range(4):
        my_pen.fd(size +1)
        my_pen.left(90)
        size -= 5
    size += 1
turtle.done()