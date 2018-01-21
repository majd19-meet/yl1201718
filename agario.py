from ball import Ball
import time
from turtle import *
import random
turtle.tracer(0)
turtle.hideturtle()

RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT =turtle.getcanvas().winfo_height()/2

MY_BALL = Ball(0,0,10,50,100,"lightpink")


NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS = []

for i in range (NUMBER_OF_BALLS):
	x = random.randint(int(-SCREEN_WIDTH) + int(MAXIMUM_BALL_RADIUS) , int(SCREEN_WIDTH) - int(MAXIMUM_BALL_RADIUS))
	y = random.randint(int(-SCREEN_HEIGHT) + int(MAXIMUM_BALL_RADIUS),int(SCREEN_HEIGHT) - int(MAXIMUM_BALL_RADIUS))
	dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	if dx = 0:
		dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	dy = random.randint(NIMUM_BALL_DY,MAXIMUM_BALL_DY)
	if dy = 0:
		dy = random.randint(NIMUM_BALL_DY,MAXIMUM_BALL_DY)
	radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	color = (random.random(), random.random(), random.random())
	ball1 = Ball(self, x, y, dx, dy, radius, color)
	BALLS.append (ball1)


def move_all_balls():
	for z in BALLS:
		z.move(SCREEN_WIDTH, SCREEN_HEIGHT)

def collide(ball_a, ball_b):
	if ball_a = ball_b :
		return False
	DISTANCE_BETWEEN_CENTERS = int(ball_a.pos()) - int(ball_b.pos())
	if DISTANCE_BETWEEN_CENTERS+10 <= ball_a.radius + ball_b.radius:
		return True
	else:
		return False
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
					ball_a = Ball(X_coordinate, Y_coordinate, X_axis_speed, Y_axis_speed, radius, color)
					ball_b







