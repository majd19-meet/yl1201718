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

Ball1 = Ball(5,"blue",10)
Ball2 = Ball(7,"green",10)

def check_collision(Ball1, Ball2):
	if Ball1.radius+Ball2.radius > 
