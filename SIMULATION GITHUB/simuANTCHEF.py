import turtle
from turtle import Screen, Turtle
from random import choice, randint
from math import atan,sin,cos
BALL_DIAMETER = 10
WIDTH, HEIGHT = 600, 600
collisions = 0
first = 1
line = 1

balls = []

COLORS = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan', 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'gray', 'white']

INITIAL_BALLS = int(input("Enter Number of balls : "))

GRAVITY = 0.1

CURSOR_SIZE = 50

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.clear()
pen.write("Collisions : {}".format(collisions), align="center", font=("Courier", 24, "normal"))

def distance(ball1,ball2):
    x1 = ball1.xcor()
    x2 = ball2.xcor()
    y1 = ball1.ycor()
    y2 = ball2.ycor()

    return ( (x1-x2)**2 + (y1-y2)**2 )**0.5

def addBall():
    global balls
    ball = Turtle('circle')
    ball.shapesize(0.5)
    ball.color(choice(COLORS))
    ball.penup()
    ball.speed('fastest')
    x, y = map(int,input().split())
    if(x!=0 and y!=0):
        raise Exception("Sorry, One of the co-ordinates must be zero!")
    if(x==0 and y==0):
        raise Exception("Sorry, One of the co-ordinates must be non-zero!")
    ball.goto(x, y)
    ball.dy = 0
    ball.dx = 0

    balls.append(ball)

    numOfBalls = len(balls)


screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor('black')
screen.tracer(False)
screen.title("ANTCHEF simulation")



for _ in range(INITIAL_BALLS):
    addBall()

screen.onkey(addBall, 'a')
screen.onkey(screen.bye, 'q')

screen.listen()

def tick():
    global collisions,pen,first,balls
    if(first):
        for ball in balls:
            if(ball.xcor()==0 or ball.ycor()==0):
                if(ball.xcor()!=0):
                    if(ball.xcor()>0):
                        ball.dx = -0.5
                    else:
                        ball.dx = 0.5

                else:
                    if(ball.ycor()>0):
                        ball.dy = -0.5
                    else:
                        ball.dy = 0.5
            ball.sety(ball.ycor() + ball.dy)

            ball.setx(ball.xcor() + ball.dx)
        first = 0
    d = dict()
    for ball in balls:
        if (ball.ycor() < -HEIGHT/2 or ball.xcor() > WIDTH/2 or ball.xcor() < -WIDTH/2 or ball.ycor() > HEIGHT/2):
            ball.hideturtle()
            balls.remove(ball)
            print("here")
            continue
        if((ball.xcor(),ball.ycor()) in d):
            d[(ball.xcor(),ball.ycor())]+=1
        else:
            d[(ball.xcor(),ball.ycor())]=1
        
    for x in d:
        if(d[x]>1):
            collisions+=1
            print(x)
            pen.clear()
            pen.write("Collisions : {}".format(collisions), align="center", font=("Courier", 24, "normal"))
            for i in balls:
                if((i.xcor(),i.ycor())==x):
                    i.dx*=-1
                    i.dy*=-1

    for x in balls:
        x.sety(x.ycor() + x.dy)
        x.setx(x.xcor() + x.dx)
    screen.update()
    screen.ontimer(tick, 40)



tick()
screen.mainloop()
