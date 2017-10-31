import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
sides = int(input("how many sides"))
long = int(input("how long"))
for i in range(sides):
    alex.forward(long)
    alex.left(360/sides)
    