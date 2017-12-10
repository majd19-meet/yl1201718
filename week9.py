from turtle import *
import random
import math

class Rectangle(Turtle):
	def __init__(self, width, height, color):
		Turtle.__init__(self)
		self.shape("rectangle")
		self.width(width)
		self.height(height)
		self.color(color)

rec1 = Rectangle(10,7,"black")
rec2 = Rectangle(13,10,"red")


mainloop()