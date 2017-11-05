import turtle
turtle.register_shape("arrow_thingy", ((50,0), (50,-50), (25,-75), (0,-50), (0,0) ))
turtle.shape("arrow_thingy")
turtle.left (90)
turtle.getshapes()
turtle.mainloop()
