from turtle import Turtle, Screen, colormode
from random import randint, choice

mbe = Turtle()
mbe.shape("classic")
mbe.speed(100)
colormode(255)
# mbe.color((24, 131, 243))

# Draw a square
# for _ in range(4):
#     mbe.forward(100)
#     mbe.right(90)

# Draw a dashed line
# for _ in range(10):
# mbe.forward(10)
# mbe.penup()
# mbe.forward(10)
# mbe.pendown()

# Draw Shapes having 3 - 10 sides on the same base with each shape's side having a random color
# for i in range(3, 11):
#     angle = 360 / i
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     mbe.color((r, g, b))
#     for _ in range(i):
#         mbe.forward(100)
#         mbe.right(angle)

# Draw a random walk
# turns = [
#     0,
#     90,
#     180,
#     270,
# ]
# for i in range(200):
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     mbe.color((r, g, b))
#     mbe.forward(10)
#     mbe.setheading(choice(turns))

# Draw a spirograph
# gap = 2
# for _ in range(int(360 / gap)):
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     mbe.color((r, g, b))
#     mbe.circle(100)
#     mbe.setheading(mbe.heading() + gap)


# Event Listeners
# Etch-A-Sketch app
def move_forward():
    mbe.forward(10)


def move_backward():
    mbe.backward(10)


def clockwise():
    mbe.right(5)


def counter_clockwise():
    mbe.left(5)


def clear():
    mbe.reset()


# Don't Write any code below this
screen = Screen()
# Event listeners start
screen.listen()
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_backward, "s")
screen.onkeypress(clockwise, "d")
screen.onkeypress(counter_clockwise, "a")
screen.onkeypress(clear, "c")
# Event listeners ends
screen.exitonclick()
