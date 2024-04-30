import turtle
def rectange (width, length):
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(length)
        turtle.left(90)

rectange(100, 50)