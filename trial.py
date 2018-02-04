from ball import Ball
import time
import turtle
from turtle import *
import random
turtle.tracer(0)
turtle.hideturtle()
import math

SIZE_X=1200
SIZE_Y=680
turtle.setup(SIZE_X+20,SIZE_Y+20)
turtle.bgcolor("black")

RUNNING = True
sleep = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT =turtle.getcanvas().winfo_height()/2

MY_BALL = Ball(0,0,10,50,25,"pink")

NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 5
MAXIMUM_BALL_RADIUS = 60
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS = []
score_list=[]

# score_list=[]
# score = 0
# scoreboard = turtle.clone()
# scoreboard.goto(-SIZE_X/2 +40 ,SIZE_Y/2 - 40)
# scoreboard.penup()
# scoreboard.write('score = 0',font=("Arial", 14, "bold"))

# if MY_BALL.pos() in ball.pos():    
#     score = score+1
#     pu()
#     score_list.append(score)
#     scoreboard.clear()
#     scoreboard.write('score='+str(score),font=("Arial", 14, "bold"))


for i in range (NUMBER_OF_BALLS):
	x = random.randint(int(-SCREEN_WIDTH) + int(MAXIMUM_BALL_RADIUS) , int(SCREEN_WIDTH) - int(MAXIMUM_BALL_RADIUS))
	y = random.randint(int(-SCREEN_HEIGHT) + int(MAXIMUM_BALL_RADIUS),int(SCREEN_HEIGHT) - int(MAXIMUM_BALL_RADIUS))
	dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	if dx == 0:
		dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	if dy == 0:
		dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	color = (random.random(), random.random(), random.random())
	ball1 = Ball(x, y, dx, dy, radius, color)

	BALLS.append (ball1)

score = 0

def move_all_balls():
	for z in BALLS:
		z.move(SCREEN_WIDTH, SCREEN_HEIGHT)

def collide(ball_a, ball_b):
	ball_a_pos = ball_a.pos()
	ball_b_pos = ball_b.pos()	
	if ball_a == ball_b :
		return False
		print("GAME OVER")

	# print(ball_a.xcor())	#x1
	# print(ball_a.ycor())	#y1
	# print(ball_b.xcor())	#x2
	# print(ball_b.ycor())	#y2


	ball_a.xcor()	#x1
	ball_a.ycor()	#y1
	ball_b.xcor()	#x2
	ball_b.ycor()	#y2

	DISTANCE_BETWEEN_CENTERS = ((ball_a.xcor()-ball_b.xcor())**2 + (ball_a.ycor()-ball_b.ycor())**2)**0.5

	if DISTANCE_BETWEEN_CENTERS+10 <= ball_a.radius + ball_b.radius:
		return True
	else:
		return False
		print("GAME OVER")

def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if collide(ball_a,ball_b) == True:
				radius_a = ball_a.radius
				radius_b = ball_b.radius
				X_coordinate = random.randint(int(-SCREEN_WIDTH) + int(MAXIMUM_BALL_RADIUS) , int(SCREEN_WIDTH) - int(MAXIMUM_BALL_RADIUS))
				Y_coordinate = random.randint(int(-SCREEN_HEIGHT) + int(MAXIMUM_BALL_RADIUS),int(SCREEN_HEIGHT) - int(MAXIMUM_BALL_RADIUS))
				X_axis_speed = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				while X_axis_speed == 0:
					 X_axis_speed = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				Y_axis_speed  = random.randint(NIMUM_BALL_DY,MAXIMUM_BALL_DY)
				while Y_axis_speed  == 0:
					Y_axis_speed  = random.randint(NIMUM_BALL_DY,MAXIMUM_BALL_DY)
				radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
				r = random.randint(0,255)
				g = random.randint(0,255)
				b = random.randint(0,255)
				color = (r,g,b)
				if ball_a < ball_b:
					ball_a.goto(X_coordinate, Y_coordinate) 
					ball_a.dx = X_axis_speed 
					ball_a.dy = Y_axis_speed
					#ball_a.shapesize(radius/10)
					ball_a.color = color
					ball_a.radius += 1
					score += 1
					score_list.append(score)
					scoreboard.clear()
					scoreboard.color("white")
					scoreboard.write("score="+str(score), font=("Arial",14, "bold"))
					ball_a.shapesize(ball_a.radius/10)
					ball_b.shapesize(ball_b.radius/10)

				

				else:
					ball_b.goto(X_coordinate, Y_coordinate)
					ball_b.dx = X_axis_speed 
					ball_b.dy = Y_axis_speed
					ball_b.shapesize(radius/10)
					ball_b.color = color
					ball_a.shapesize(ball_b.radius)
					ball_b.radius += 1
					# score = score+1
					# score_list.append(score)
    	# 			scoreboard.clear()
    	# 			scoreboard.write("score=", +str(score), font=("Arial", 14, "bold"))
					ball_a.shapesize(ball_a.radius/10)
					ball_b.shapesize(ball_b.radius/10)


def check_myball_collision():
	for i in BALLS:
		if collide(i,MY_BALL) == True:
			radius_i = i.radius
			radius_MY_BALL= MY_BALL.radius
			ball_a = MY_BALL
			ball_b = i
			if MY_BALL.radius < i.radius:
				return False
				print("GAME OVER")

			else:
				X_coordinate = random.randint(int(-SCREEN_WIDTH) + int(MAXIMUM_BALL_RADIUS) , int(SCREEN_WIDTH) - int(MAXIMUM_BALL_RADIUS))
				Y_coordinate = random.randint(int(-SCREEN_HEIGHT) + int(MAXIMUM_BALL_RADIUS),int(SCREEN_HEIGHT) - int(MAXIMUM_BALL_RADIUS))
				X_axis_speed = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				while X_axis_speed == 0:
					X_axis_speed = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				Y_axis_speed  = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				while Y_axis_speed  == 0:
					Y_axis_speed  = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
				r = random.randint(0,255)
				g = random.randint(0,255)
				b = random.randint(0,255)
				color = (r,g,b)

			
				ball_b.goto(X_coordinate, Y_coordinate)
				ball_b.dx = X_axis_speed 
				ball_b.dy = Y_axis_speed
				ball_b.shapesize(radius/10)
				ball_b.color(color)
				ball_a.radius = ball_a.radius+1 
				ball_a.shapesize(ball_a.radius/10)

				# ball_a.radius > ball_b.radius:
				# ball_a.goto(X_coordinate,Y_coordinate)
				# ball_b.goto(X_coordinate,Y_coordinate)

	return True

# score_list=[]
# score = 0
# scoreboard = turtle.clone()
# scoreboard.goto(-SIZE_X/2 +40 ,SIZE_Y/2 - 40)
# scoreboard.penup()
# scoreboard.write('score = 0',font=("Arial", 14, "bold"))

# if MY_BALL.pos() in i.pos():    
# score += 1
# score_list.append(score)
# scoreboard.clear()
# scoreboard.write('score='+str(score),font=("Arial", 14, "bold"))

# if speed > MY_BALL.radius:
# 	score += 1
# 	temp = MY_BALL.radius
# 	print("WOOHOOO!")
# 	turtle.write(score, move=False, align="left", font=("Arial", 50, "bold"))


def movearound(event):
	NEW_X_coordinate = event.x - SCREEN_WIDTH
	NEW_Y_coordinate = -(event.y - SCREEN_HEIGHT)
	MY_BALL.goto(NEW_X_coordinate, NEW_Y_coordinate)
turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()


speed=MY_BALL.radius

while RUNNING == True:
	if SCREEN_WIDTH!=turtle.getcanvas().winfo_width()/2 or SCREEN_HEIGHT!=turtle.getcanvas().winfo_height()/2 :
		SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2 
		SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2

if speed > MY_BALL.radius:
	score += 1
	temp = MY_BALL.radius
	print("WOOHOOO!")
	turtle.write(score, move=False, align="left", font=("Arial", 50, "bold"))


		
	move_all_balls()
	check_myball_collision()

	getscreen().update()
	time.sleep(sleep)
	

mainloop()
	