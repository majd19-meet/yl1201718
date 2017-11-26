from turtle import *
import random
colormode(255)
r = random.randint (0,255)
g = random.randint (0,255)
b = random.randint (0,255)
#class Square(Turtle):
#	def __init__(self,size):
#		Turtle.__init__(self)
#		self.shapesize(size)
#		self.shape("square")

#	def random_color(self):
#		self.color(r,g,b)

#square1 = Square(10)
#square1.random_color()
random.randint(0,225)
#import turtle

class Rectangle(Turtle):
	def __init__(self,width,height):
		Turtle.__init__(self)
		self.width = 90
		self.height = 50

		register_shape("Rectangle",((self.width,0),(self.width,self.height),(0,self.height),(0,0)))
		self.shape("Rectengle")
		self.setheading(90)

class Square(Rectengle):
	def __init__(self,)


getshapes()

mainloop()

#mainloop()


