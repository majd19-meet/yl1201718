from turtle import *
import random
import color

colormode(255)

class Ball(Turtle):
	def __init__(self, x, y, dx, dy, radius, color):
		Turtle.__init__(self)
		self.pu()
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
		self.shapesize(radius/10)
		self.shape = ("circle")


		r = random.randint (0,255)
		g = random.randint (0,255)
		b = random.randint (0,255)
		self.color(r,g,b)

	def move(self, screen_width, screen_height):
			current_x = self.xcor()
			current_y = self.ycor()
			new_x = current_x + self.dx
			new_y = current_y + self.dy
			right_side_ball = new_x + radius
			left_side_ball = new_x - radius
			self.goto (current_x + self.dx , current_y + self.dy)


		