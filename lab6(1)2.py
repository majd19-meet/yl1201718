from turtle import *
import random
import math

class Ball(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius)
		self.color(color)
		self.speed(speed)

ball1 = Ball(7,"blue",10)
ball2 = Ball(5,"green",10)

def check_collision(ball1, ball2):
	x1 = ball1.xcor()
	y1 = ball1.ycor()
	x2 = ball2.xcor()
	y2 = ball2.ycor()

	dx = math.pow(x2-x1,2)
	dy = math.pow(y2-x2,2)

	d = dx+dy

	if ball1.shapesize()[0]+ball2.shapesize()[0] > d:
		ball1.color ("black")
		ball2.color("red")

check_collision(ball1, ball2)
mainloop()

