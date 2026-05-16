"""
#Import the turtle
import turtle

#Set the turtle screen
window = turtle.Screen()
tur=turtle.Turtle()
scr=tur.getscreen()
#title of the screen
scr.title("Merry Christmas")
#backgroundcolor of screen
scr.bgcolor("Light Blue")

tur.color("green")
tur.pensize(5)
tur.begin_fill()


# Creating Right half of the tree
tur.forward(100)
tur.left(150)
tur.forward(90)
tur.right(150)
tur.forward(60)
tur.left(150)
tur.forward(60)
tur.right(150)
tur.forward(40)
tur.left(150)
tur.forward(100)
tur.end_fill()

    #left half of the tree
tur.begin_fill()
tur.left(60)
tur.forward(100)
tur.left(150)
tur.forward(40)
tur.right(150)
tur.forward(60)
tur.left(150)
tur.forward(60)
tur.right(150)
tur.forward(90)
tur.left(150)
tur.forward(133)
tur.end_fill()

#Creating the trunck of the tree
tur.color("brown")
tur.pensize(1)
tur.begin_fill()
tur.right(90)
tur.forward(80)
tur.right(90)
tur.forward(40)
tur.right(90)
tur.forward(80)
tur.end_fill()

#Creating the balls on the Christmas Tree
tur.penup()
tur.color("red")
tur.goto(110,-10)
tur.begin_fill()
tur.circle(10)
tur.end_fill()

tur.penup()
tur.color("red")
tur.goto(-120,-10)
tur.begin_fill()
tur.circle(10)
tur.end_fill()

tur.penup()
tur.color("yellow")
tur.goto(100,40)
tur.begin_fill()
tur.circle(10)
tur.end_fill()



tur.penup()
tur.color("yellow")
tur.goto(-105,38)
tur.begin_fill()
tur.circle(10)
tur.end_fill()

tur.penup()
tur.color("red")
tur.goto(85,70)
tur.begin_fill()
tur.circle(7)
tur.end_fill()

tur.penup()
tur.color("red")
tur.goto(-95,70)
tur.begin_fill()
tur.circle(7)
tur.end_fill()

#Drawing the bells using turtle.
tur.shape("triangle")
tur.fillcolor("yellow")
tur.goto(-20,30)
tur.setheading(90)
tur.stamp()
tur.fillcolor("red")
tur.goto(20,60)
tur.setheading(90)
tur.stamp()
tur.goto(-40,75)
tur.setheading(90)
tur.stamp()

# Printing the star using for loop
tur.speed(1)
tur.penup()
tur.color("yellow")
tur.goto(-20,110)
tur.begin_fill()
tur.pendown()

for i in range(5):
    tur.forward(40)
    tur.right(144)

tur.end_fill()

# Display the message on the screen
tur.penup()
message="Merry Christmas!!!"
tur.goto(-10,-180)
tur.color("Green")
tur.pendown()
tur.write(message,move=False,align="center",font=("Arial",15,"bold"))
tur.hideturtle()
turtle.done"

import turtle

# Function to draw the tree
def tree(d, s):
    if d <= 0:  # Base case: Stop recursion when depth is 0
        return
    
    turtle.forward(s)  # Move forward
    turtle.left(30)  # Turn left for left branch
    tree(d - 1, s * 0.7)  # Recursive call for left branch
    
    turtle.right(60)  # Turn right for right branch
    tree(d - 1, s * 0.7)  # Recursive call for right branch
    
    turtle.left(30)  # Reset angle
    turtle.backward(s)  # Move back to previous position

# Set up the turtle screen
turtle.speed("fastest")  # Set drawing speed
turtle.bgcolor("white")  # Background color

# Position turtle to start drawing the tree
turtle.left(90)
turtle.penup()
turtle.goto(0, -200)  # Move to starting position
turtle.pendown()
turtle.color("brown")

# Draw the tree
tree(10, 100)

# Draw the star at the top
turtle.penup()
turtle.goto(0, 100)  # Move to the top of the tree
turtle.pendown()
turtle.color("orange", "yellow")
turtle.begin_fill()

for _ in range(5):
    turtle.forward(20)
    turtle.right(144)
    turtle.forward(20)
    turtle.left(72)

turtle.end_fill()  # Fill the star shape

# Complete the drawing
turtle.hideturtle()
turtle.done()


import turtle

# Function to draw the tree with more branches
def tree(depth, branch_length):
    if depth <= 0:  # Base case: stop when depth is zero
        return

    # Draw the main branch
    turtle.forward(branch_length)

    # Left branch
    turtle.left(25)  
    tree(depth - 1, branch_length * 0.7)  
    turtle.right(25)  

    # Middle branch (new!)
    turtle.right(15)
    tree(depth - 1, branch_length * 0.6)
    turtle.left(15)

    # Right branch
    turtle.right(25)  
    tree(depth - 1, branch_length * 0.7)  
    turtle.left(25)  

    # Move back to previous position
    turtle.backward(branch_length)

# Setup the screen
turtle.speed("fastest")  
turtle.bgcolor("white")  

# Move turtle to starting position
turtle.left(90)
turtle.penup()
turtle.goto(0, -250)  
turtle.pendown()
turtle.color("saddlebrown")  # Tree trunk color

# Draw the tree with more branches
tree(6, 100)  # Depth of 6, initial branch length 100

# Draw the leaves (green dots at the end of branches)
turtle.color("green")
turtle.penup()
for _ in range(30):  # Create random leaf effect
    x = turtle.xcor() + turtle.random.randint(-40, 40)
    y = turtle.ycor() + turtle.random.randint(-40, 40)
    turtle.goto(x, y)
    turtle.dot(10)  # Draw small green dots as leaves

# Draw the star at the top
turtle.goto(0, 100)  # Position at top of tree
turtle.color("orange", "yellow")
turtle.pendown()
turtle.begin_fill()

for _ in range(5):
    turtle.forward(20)
    turtle.right(144)
    turtle.forward(20)
    turtle.left(72)

turtle.end_fill()  # Fill the star

# Complete the drawing
turtle.hideturtle()
turtle.done()


        


import turtle


tur = turtle.Turtle()
tur.speed(20)
tur.color("black", "orange")
tur.begin_fill()

for i in range(50):
	tur.forward(300)
	tur.left(170)

tur.end_fill()
turtle.done()


import turtle

# Set initial position
turtle.penup ()
turtle.left (90)
turtle.fd (200)
turtle.pendown ()
turtle.right (90)

# flower base
turtle.fillcolor ("red")
turtle.begin_fill ()
turtle.circle (10,180)
turtle.circle (25,110)
turtle.left (50)
turtle.circle (60,45)
turtle.circle (20,170)
turtle.right (24)
turtle.fd (30)
turtle.left (10)
turtle.circle (30,110)
turtle.fd (20)
turtle.left (40)
turtle.circle (90,70)
turtle.circle (30,150)
turtle.right (30)
turtle.fd (15)
turtle.circle (80,90)
turtle.left (15)
turtle.fd (45)
turtle.right (165)
turtle.fd (20)
turtle.left (155)
turtle.circle (150,80)
turtle.left (50)
turtle.circle (150,90)
turtle.end_fill ()

# Petal 1
turtle.left (150)
turtle.circle (-90,70)
turtle.left (20)
turtle.circle (75,105)
turtle.setheading (60)
turtle.circle (80,98)
turtle.circle (-90,40)

# Petal 2
turtle.left (180)
turtle.circle (90,40)
turtle.circle (-80,98)
turtle.setheading (-83)

# Leaves 1
turtle.fd (30)
turtle.left (90)
turtle.fd (25)
turtle.left (45)
turtle.fillcolor ("green")
turtle.begin_fill ()
turtle.circle (-80,90)
turtle.right (90)
turtle.circle (-80,90)
turtle.end_fill ()
turtle.right (135)
turtle.fd (60)
turtle.left (180)
turtle.fd (85)
turtle.left (90)
turtle.fd (80)

# Leaves 2
turtle.right (90)
turtle.right (45)
turtle.fillcolor ("green")
turtle.begin_fill ()
turtle.circle (80,90)
turtle.left (90)
turtle.circle (80,90)
turtle.end_fill ()
turtle.left (135)
turtle.fd (60)
turtle.left (180)
turtle.fd (60)
turtle.right (90)
turtle.circle (200,60)
turtle.done()



import turtle

window = turtle.Screen()
window.bgcolor('black')
window.title("Galactic Flower made for Follow Tutorials")

galatic = turtle.Turtle()
galatic.speed(20)
galatic.color('white')

rotate=int(180)

def Circles(t,size):
    for i in range(10):
        t.circle(size)
        size=size-4

def drawCircles(t,size,repeat):
  for i in range (repeat):
    Circles(t,size)
    t.right(360/repeat)

drawCircles(galatic,150,10)

t1 = turtle.Turtle()
t1.speed(20)
t1.color('yellow')

rotate=int(90)

def Circles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-10

def drawCircles(t,size,repeat):
    for i in range (repeat):
        Circles(t,size)
        t.right(360/repeat)
drawCircles(t1,130,10)
t2= turtle.Turtle()
t2.speed(20)
t2.color('blue')

rotate=int(80)

def Circles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-5

def drawCircles(t,size,repeat):
    for i in range (repeat):
        Circles(t,size)
        t.right(360/repeat)

drawCircles(t2,110,10)
t3 = turtle.Turtle()
t3.speed(20)
t3.color('red')

rotate=int(90)

def Circles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-19

def drawCircles(t,size,repeat):
    for i in range (repeat):
        Circles(t,size)
        t.right(360/repeat)

drawCircles(t3,80,10)
t4= turtle.Turtle()
t4.speed(20)
t4.color('green')

rotate=int(90)

def Circles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-20

def drawCircles(t,size,repeat):
    for i in range (repeat):
        Circles(t,size)
        t.right(360/repeat)

drawCircles(t4,40,10)

turtle.done()

"""
#Imported turtle
import turtle

#set the turtle object
t=turtle.Turtle()
scr=t.getscreen()
scr.bgcolor("Light Blue")

#Drawing the face of the dog
t.pencolor("tan1")
t.color("tan1")
t.pensize(3)
t.penup()
t.setheading(90)
t.goto(30,-30)
t.pendown()
t.begin_fill()
t.circle(45,180)
t.right(90)
t.goto(-45,-30)
t.circle(35,190)
t.setheading(0)
t.forward(55)
t.penup()
t.setheading(0)
t.pendown()
t.circle(35,170)
t.penup()
t.end_fill()

#Create the tongue of the dog
t.pencolor("DeepPink1")
t.color("Pink")
t.setheading(270)
t.goto(-10,-90)
t.right(60)
t.pendown()
t.begin_fill()
t.forward(15)
t.left(60)
t.forward(10)
t.circle(10,180)
t.forward(10)
t.left(60)
t.forward(15)
t.end_fill()

#line on the tongue
t.pensize(1)
t.pencolor("DeepPink")
t.goto(-13,-90)
t.setheading(270)
t.forward(17)
t.circle(4,180)
t.penup()
t.left(90)
t.forward(8)
t.goto(-13,-107)
t.setheading(270)
t.left(180)
t.pendown()
t.circle(4,-180)



#right ear
t.penup()
t.goto(42,-45)
t.pencolor("black")
t.color("sienna")
t.setheading(0)
t.pendown()
t.begin_fill()
t.forward(10)
t.left(60)
t.circle(35,145)
t.end_fill()

#left ear
t.penup()
t.goto(-70,-45)
t.pendown()
t.setheading(180)
t.begin_fill()
t.forward(10)
t.left(-240)
t.circle(35,-145)
t.end_fill()
t.penup()


#eyes
t.pencolor("black")
t.color("black")
t.goto(-5,-45)
t.setheading(270)
t.pendown()
t.begin_fill()
t.circle(10,180)
t.forward(5)
t.circle(10,180)
t.forward(5)
t.end_fill()
t.penup()

t.pencolor("black")
t.color("black")
t.goto(-45,-45)
t.setheading(270)
t.pendown()
t.begin_fill()
t.circle(10,180)
t.forward(5)
t.circle(10,180)
t.forward(5)
t.end_fill()
t.penup()

# Inner white dots in the eye
t.color("white")
t.goto(-2,-44)
t.begin_fill()
t.circle(6)
t.end_fill()

t.color("white")
t.goto(-40,-44)
t.begin_fill()
t.circle(6)
t.end_fill()

#Nose of the dog
t.color("black")
t.goto(-25,-75)
t.begin_fill()
t.circle(10)
t.end_fill()
t.goto(-14,-73)
t.color("white")
t.begin_fill()
t.circle(2)
t.end_fill()
t.goto(-20,-73)
t.color("white")
t.begin_fill()
t.circle(2)
t.end_fill()
t.goto(-17,-77)
t.color("white")
t.begin_fill()
t.circle(2)
t.end_fill()
t.hideturtle()
turtle.done()

