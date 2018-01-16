from turtle import *
import random
import turtle
turtle.hideturtle()
colormode(255)
SCREEN_SIZE = 640,480



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
			top_side_ball = new_y + radius
			bottom_side_ball = new_y - radius
			self.goto (new_x , new_y)

			if right_side_ball >= screen_width:
				self.dx = -self.dx
			
			if left_side_ball <= -screen_width:
				self.dx = -self.dx
			
			#-self.dx = self.dx

			if top_side_ball >= screen_height:
				self.dy = -self.dy

			if bottom_side_ball <= -screen_height:
				self.dy = -self.dy
			
