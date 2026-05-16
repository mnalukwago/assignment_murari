"""
import turtle
# turle is an in-built module which comes with python 
tr = turtle.Turtle() # has a class called turtle
tr.pensize(5)
tr.color("blue")
tr.penup()
tr.goto(-110, -25)
tr.pendown()
tr.circle(45)

tr.color("black")
tr.penup()
tr.goto(0, -25)
tr.pendown()
tr.circle(45)

tr.color("red")
tr.penup()
tr.goto(110, -25)
tr.pendown()
tr.circle(45)

tr.color("yellow")
tr.penup()
tr.goto(-55, -75)
tr.pendown()
tr.circle(45)

tr.color("green")
tr.penup()
tr.goto(55, -75)
tr.pendown()
tr.circle(45)

turtle.done()"


# Python program to draw hexagon 
# using Turtle Programming 
import turtle 
polygon = turtle.Turtle() 

num_sides = 6
side_length = 70
angle = 360.0 / num_sides 

for i in range(num_sides): 
	polygon.forward(side_length) 
	polygon.right(angle) 
	
turtle.done() 

"""
# Python program to draw 
# Rainbow Benzene 
# using Turtle Programming 
import turtle 
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
t = turtle.Pen() 
turtle.bgcolor('black') 
for x in range(360): 
	t.pencolor(colors[x%6]) 
	t.width(x//100 + 1) 
	t.forward(x) 
	t.left(59) 
