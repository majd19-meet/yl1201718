import turtle
import random

##HEAD
print('choose your player')
print('adam, doudou, amir, kayvon, jan, alex')
chose=input()
chose.lower()

turtle.bgcolor("Lavender")
fatman = turtle.clone()
fatman.penup()
turtle.register_shape('adam.gif')
turtle.register_shape('dou_dou.gif')
turtle.register_shape('amir.gif')
turtle.register_shape('kayvon.gif')
turtle.register_shape('jan.gif')
turtle.register_shape('alex.gif')

turtle.register_shape('grapes.gif')
turtle.register_shape('orange.gif')
turtle.register_shape('watermelon.gif')
turtle.register_shape('banana.gif')
turtle.register_shape('apple.gif')
turtle.register_shape('cherries.gif')
turtle.register_shape('poop.gif')
food_types = ['grapes.gif','orange.gif','watermelon.gif','banana.gif','apple.gif','cherries.gif']

if chose=='adam':
    fatman.shape('adam.gif')
elif chose=='doudou':
    fatman.shape('dou_dou.gif')
elif chose=='amir':
    fatman.shape('amir.gif')
elif chose=='kayvon':
    fatman.shape('kayvon.gif')
elif chose=='jan':
    fatman.shape('jan.gif')
elif chose=='alex':
    fatman.shape('alex.gif')
    




###af566edc26b76e655e984c42088f41b0e475851e

    
turtle.tracer(1,0)

SIZE_X=1200
SIZE_Y=680
turtle.setup(SIZE_X+20,SIZE_Y+20)

turtle.penup()

SQUARE_SIZE=20
START_LENGTH=1
food_time=[]
shape_list=[]
score_list=[]
pos_list=[]
stamp_list=[]
score = 0
rot_time = 11

turtle.hideturtle()

for i in range(START_LENGTH):
    x_pos=fatman.pos()[0]
    y_pos=fatman.pos()[1]

    my_pos=(x_pos,y_pos)

    pos_list.append(my_pos)

    stamp1=fatman.stamp()
    stamp_list.append(stamp1)


UP_ARROW="Up"
LEFT_ARROW="Left"
DOWN_ARROW="Down"
RIGHT_ARROW="Right"
TIME_STEP=100
SPACEBAR='space'
##global score
UP=0
DOWN=1
LEFT=2
RIGHT=3


time_count = []
wall_pos=[]
box=turtle.clone()
box.shape('square')
box.hideturtle()
box.penup()
scoreboard = turtle.clone()
scoreboard.goto(-SIZE_X/2 +40 ,SIZE_Y/2 - 40)
scoreboard.penup()

scoreboard.write('score = 0',font=("Arial", 14, "bold"))
#wall maker
def wall_maker(left_corner,hight,width):
    box.goto(left_corner[0],left_corner[1]-SQUARE_SIZE)
    box.color("SteelBlue")
    for i in range(hight):
        box.goto(box.pos()[0], box.pos()[1]+SQUARE_SIZE)
        box.stamp()
        wall_pos.append(box.pos())
    for i in range(width-1):
        box.goto(box.pos()[0]+SQUARE_SIZE,box.pos()[1])
        box.stamp()
        wall_pos.append(box.pos())
    for i in range (hight-1):
        box.goto(box.pos()[0],box.pos()[1]-SQUARE_SIZE)
        box.stamp()
        wall_pos.append(box.pos())
    for i in range(width-2):
        box.goto(box.pos()[0]-SQUARE_SIZE,box.pos()[1])
        box.stamp()
        wall_pos.append(box.pos())
    

def draw_box(left_corner, height, width):
    start_x, start_y = left_corner
    box.goto(left_corner)
    for h in range(height):
        # draw horizontal line
        for w in range(width):
            old_x, old_y = box.pos()
            box.goto(old_x + SQUARE_SIZE, old_y)
            box.stamp()
            wall_pos.append(box.pos())
        box.goto(start_x, start_y - ((h+1) * SQUARE_SIZE))
        
left_corner=(-600,-340)
wall_maker(left_corner,35,61)
###maze
##

width=12
hight=12
box.color("LightBlue")
draw_box((-460,260), hight, width)
draw_box((-460, -40), hight, width)
draw_box((220, 260), hight, width)
draw_box((220, -40), hight, width)

width=6
hight=6
box.color("AntiqueWhite4")
draw_box((60, 20), hight, width)
draw_box((-160, -80), hight, width)
draw_box((-160, 180), hight, width)
UP_EDGE=SIZE_Y/2
DOWN_EDGE=-SIZE_Y/2
RIGHT_EDGE=SIZE_X/2
LEFT_EDGE=-SIZE_X/2


direction=0

def up():
    global direction
    x_pos=fatman.pos()[0]
    y_pos=fatman.pos()[1]
    new_pos=(x_pos,y_pos+SQUARE_SIZE)
    if new_pos not in wall_pos:
        direction=UP

    #print("You pressed the up key!")

def down():
    global direction
    x_pos=fatman.pos()[0]
    y_pos=fatman.pos()[1]
    new_pos=(x_pos,y_pos-SQUARE_SIZE)
    if new_pos not in wall_pos:
        direction=DOWN
    #print("You pressed the down key!")

def left():
    global direction
    x_pos=fatman.pos()[0]
    y_pos=fatman.pos()[1]
    new_pos=(x_pos-SQUARE_SIZE,y_pos)
    if new_pos not in wall_pos:
        direction=LEFT
    #print("You pressed the left key!")

def right():
    global direction
    x_pos=fatman.pos()[0]
    y_pos=fatman.pos()[1]
    new_pos=(x_pos+SQUARE_SIZE,y_pos)
    if new_pos not in wall_pos:
        direction=RIGHT
    #print("You pressed the right key!")



turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.listen()

food=turtle.clone()
food.shape("orange.gif")
food.hideturtle()
food_pos=[]
food_stamps=[]


def make_food():
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+2
    max_x=int(SIZE_X/2/SQUARE_SIZE)-2
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+2
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-2
    temp_pos = wall_pos[10]
    choice = random.choice(food_types)
    food.shape(choice)
    while temp_pos in wall_pos:
        food_x=random.randint(min_x,max_x)*SQUARE_SIZE
        food_y=random.randint(min_y,max_y)*SQUARE_SIZE
        temp_pos= (food_x,food_y)
    
    else:
        food.goto(food_x,food_y)
        food_pos.append((food_x,food_y))
        ran_food_stamp=food.stamp()
        food_stamps.append(ran_food_stamp)
        food_time.append(0)
        shape_list.append(choice)

    TIME_STEP2=7000
   # turtle.ontimer(make_food,TIME_STEP2)

##def rottime():
##    for i in range(len(food_time)):
##        food_time[i] += 1
     #   if food_time[i] > rot_time:
      #      shape_list[i] = "poop.gif"
       #     food.shape("poop.gif")
            
    #turtle.ontimer(rottime, 1000)
##def rottime():
##    for i in range(len(food_time)):
##        food_time[i] += 1
##        if food_time[i] > rot_time:
##            food.shape("poop.gif")
##            
##    turtle.ontimer(rottime, 1000)
rot_time = 50
rotfood= turtle.clone()
rotfood.shape('poop.gif')
rotfood.ht()
rotfood.pu()
rotfoodpos = []

def move_fatman():
    global score

    my_pos=fatman.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]


    if direction==RIGHT:
        new_pos=(x_pos+SQUARE_SIZE,y_pos)
        if new_pos not in wall_pos:
            fatman.goto(new_pos)

    if direction==LEFT:
        new_pos=(x_pos-SQUARE_SIZE,y_pos)
        if new_pos not in wall_pos:
            fatman.goto(new_pos)

    if direction==UP:
        new_pos=(x_pos,y_pos+SQUARE_SIZE)
        if new_pos not in wall_pos:
            fatman.goto(new_pos)

    if direction==DOWN:
        new_pos=(x_pos,y_pos-SQUARE_SIZE)
        if new_pos not in wall_pos:
            fatman.goto(new_pos)



    my_pos=fatman.pos()
    pos_list.append(my_pos)
    new_stamp=fatman.stamp()
    stamp_list.append(new_stamp)
    old_stamp=stamp_list.pop(0)
    fatman.clearstamp(old_stamp)
    pos_list.pop(0)



    if fatman.pos() in food_pos:
        food_ind=food_pos.index(fatman.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        food_time.pop(food_ind)
        score = score+1
        score_list.append(score)
        scoreboard.clear()
        scoreboard.write('score='+str(score),font=("Arial", 14, "bold"))
        print('you have eaten the food')
        make_food()
    rotten_food = []
    did_food_rot = False
    for i in range(len(food_time)):
        time = food_time[i]
        food_time[i] = time + 1
        if food_time[i] >= rot_time:
            print(i)
            pos = food.pos()
            food_pos.pop(i)
            old_stamp = food_stamps.pop(i)
            food.clearstamp(old_stamp)
            rotten_food.append(i)
            rotfood.goto(pos)
            rotfood.stamp()
            rotfoodpos.append(pos)
            did_food_rot = True

    for rottime in rotten_food:
        food_time.pop(rottime)

    if did_food_rot:
        make_food()
        score=score-1
        scoreboard.clear()
        scoreboard.write('score='+str(score),font=("Arial", 14, "bold"))
        print('food started to rot!')
    
    if fatman.pos() in rotfoodpos:
        quit()
    elif score==-2:
        quit()

    turtle.ontimer(move_fatman, TIME_STEP)
    
move_fatman()
make_food()