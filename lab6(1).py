from turtle import *
colormode(225)
class Square (Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.shapesize(size)
		self.shape("square")

	def random_color(self):
		r = random.randit (0-255)
		g = random.randit (0-255)
		b = random.randit (0-255)
		self.color(r,g,b)

Square1 = Square(10)

mainloop()