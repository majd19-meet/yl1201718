import turtle 
turtle.speed(100)
turtle.pensize(10)

angle = 20
for i in range (18):
	
	turtle.left(angle)
	
	turtle.forward (120)
	turtle.left (90)
	turtle.color ("lightpink")

	turtle.forward (120)
	turtle.left (90)
	turtle.color ("grey")

	turtle.forward (120)
	turtle.left (90)
	turtle.color ("lightblue")

	turtle.forward (120)
	turtle.left (90)
	turtle.color ("lightgreen")

turtle.mainloop()

