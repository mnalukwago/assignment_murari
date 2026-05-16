"""
import turtle
tr = turtle.Turtle()
tr.pensize(5)
tr.color("blue")
tr.penup()
tr.goto(-110, -25)
tr.pendown()
tr.circle(60)

tr.color("black")
tr.penup()
tr.goto(0, -25)
tr.pendown()
tr.circle(60)
tr.color("red")
tr.penup()
tr.goto(110, -25)
tr.pendown()
tr.circle(60)


tr.color("yellow")
tr.penup()
tr.goto(-55, -75)
tr.pendown()
tr.circle(60)
tr.color("green")
tr.penup()
tr.goto(55, -75)
tr.pendown()
tr.circle(60)"

"""

"""
# Import turtle package
import turtle

# Creating a turtle screen object
sc = turtle.Screen()

# Creating a turtle object(pen)
pen = turtle.Turtle()

# Defining a method to form a semicircle
# with a dynamic radius and color
def semi_circle(col, rad, val):

	# Set the fill color of the semicircle
	pen.color(col)

	# Draw a circle
	pen.circle(rad, -180)

	# Move the turtle to air
	pen.up()

	# Move the turtle to a given position
	pen.setpos(val, 0)

	# Move the turtle to the ground
	pen.down()

	pen.right(180)


# Set the colors for drawing
col = ['violet', 'indigo', 'blue', 
	'green', 'yellow', 'orange', 'red']

# Setup the screen features
sc.setup(600, 600)

# Set the screen color to black
sc.bgcolor('black')

# Setup the turtle features
pen.right(90)
pen.width(10)
pen.speed(7)

# Loop to draw 7 semicircles
for i in range(7):
	semi_circle(col[i], 10*(
	i + 8), -10*(i + 1))

# Hide the turtle
pen.hideturtle()

# second method

import turtle

mypen= turtle.Turtle()
mypen.shape('turtle')
mypen.speed(10)

window= turtle.Screen()
window.bgcolor('white')
rainbow= ['red','orange','yellow','green','blue','indigo','violet']
size= 180
mypen.penup()
mypen.goto(0,-180)
for color in rainbow:
	mypen.color(color)
	mypen.fillcolor(color)
	mypen.begin_fill()
	mypen.circle(size)
	mypen.end_fill()
	size-=20

turtle.done()


import turtle
madrine = turtle.Turtle()
madrine.shape('turtle')
madrine.speed(20)

#The window variable is used to store the screen object created by turtle.Screen(). 
# turtle.Screen() creates a window where all the turtle graphics appear.
# The window variable is just a reference to this screen object.
# This allows us to customize the window, like setting the background color.

window = turtle.Screen()
window.bgcolor('white')
window.title("My Rainbow Circles")  # Adds a title to the window
window.setup(width=600, height=600) # Sets window size

rainbow= ['red','orange','yellow','green','blue','indigo','violet']
size = 180
madrine.penup()
madrine.goto(0,-180)
for color in rainbow:
	madrine.color(color)
	madrine.fillcolor(color)
	madrine.begin_fill()
	madrine.circle(size)
	madrine.end_fill()
	size-=20

turtle.done()"

import turtle

# Function to draw a branch
def draw_branch(branch_length):
    if branch_length > 5:  # Stop when the branch is too small
        turtle.forward(branch_length)
        turtle.right(20)
        draw_branch(branch_length - 15)  # Recursive call for right branch
        turtle.left(40)
        draw_branch(branch_length - 15)  # Recursive call for left branch
        turtle.right(20)
        turtle.backward(branch_length)  # Move back to the starting point

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Turtle Tree")

# Set up the turtle
turtle.speed(0)  # Fastest speed
turtle.left(90)  # Point the turtle upwards
turtle.penup()
turtle.goto(0, -250)  # Move to the base of the tree
turtle.pendown()
turtle.color("saddlebrown")  # Trunk color

# Draw the tree
draw_branch(100)

# Draw the leaves
turtle.penup()
turtle.goto(0, -150)
turtle.pendown()
turtle.color("green")
turtle.begin_fill()
turtle.circle(50)  # Simple circular foliage
turtle.end_fill()

# Finish
turtle.hideturtle()
turtle.done()
 
"""

import turtle
from time import sleep

# Part 1 : Initialize the module
t = turtle.Turtle()
t.speed(4)
turtle.bgcolor("white")
t.color("white")
turtle.title('Netflix Logo')

# Part 2 : Drawing the black background
t.up()
t.goto(-80, 50)
t.down()
t.fillcolor("black")
t.begin_fill()

t.forward(200)
t.setheading(270)
s = 360
for i in range(9):
    s = s - 10
    t.setheading(s)
    t.forward(10)

t.forward(180)
s = 270
for i in range(9):
    s = s - 10
    t.setheading(s)
    t.forward(10)

t.forward(200)
s = 180
for i in range(9):
    s = s - 10
    t.setheading(s)
    t.forward(10)

t.forward(180)
s = 90
for i in range(9):
    s = s - 10
    t.setheading(s)
    t.forward(10)
t.forward(30)
t.end_fill()

# Part 3 : Drawing the N shape
t.up()
t.color("black")
t.setheading(270)
t.forward(240)
t.setheading(0)
t.down()
t.color("red")
t.fillcolor("#E50914")
t.begin_fill()
t.forward(30)
t.setheading(90)
t.forward(180)
t.setheading(180)
t.forward(30)
t.setheading(270)
t.forward(180)
t.end_fill()
t.setheading(0)
t.up()
t.forward(75)
t.down()
t.color("red")
t.fillcolor("#E50914")
t.begin_fill()
t.forward(30)
t.setheading(90)
t.forward(180)
t.setheading(180)
t.forward(30)
t.setheading(270)
t.forward(180)
t.end_fill()
t.color("red")
t.fillcolor("red")
t.begin_fill()
t.setheading(113)
t.forward(195)
t.setheading(0)
t.forward(31)
t.setheading(293)
t.forward(196)
t.end_fill()
t.hideturtle()

sleep(10)



