import turtle
wn=turtle.Screen()
wn.title("ping powered by pallav")
wn.bgcolor("black")
wn.setup(800,600)
wn.tracer(0)
#player_1
player_1=turtle.Turtle()
player_1.speed(0)
player_1.shape("square")
player_1.color("yellow")
player_1.shapesize(5,1)
player_1.penup()
player_1.goto(350,0)
#player2
player_2=turtle.Turtle()
player_2.speed(0)
player_2.shape("square")
player_2.color("blue")
player_2.shapesize(5,1)
player_2.penup()
player_2.goto(-350,0)
#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("pink")
ball.shapesize(1,1)
ball.penup()
ball.goto(0,0)
ball.dx=0.25
ball.dy=0.25
def paddle_up_1():
    y=player_1.ycor()
    y+=20
    player_1.sety(y)
def paddle_down_1():
    y=player_1.ycor()
    y-=20
    player_1.sety(y)
def paddle_up_2():
    y=player_2.ycor()
    y+=15
    player_2.sety(y)
def paddle_down_2():
    y=player_2.ycor()
    y-=15
    player_2.sety(y)
wn.listen()
wn.onkeypress(paddle_up_1, "w")
wn.onkeyrelease(paddle_up_1, "w")
wn.onkeypress(paddle_down_1, "s")
wn.onkeyrelease(paddle_down_1, "s")
wn.onkeypress(paddle_up_2, "Up")
wn.onkeyrelease(paddle_up_2, "Up")
wn.onkeypress(paddle_down_2, "Down")
wn.onkeyrelease(paddle_down_2, "Down")
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
score_1=0
score_2=0
while True:
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if ball.xcor()<350 and ball.xcor()>340 and (ball.ycor()-player_1.ycor()<50 and ball.ycor()-player_1.ycor()>-50):
        ball.setx(340)
        ball.dx*=-1
    if ball.xcor() >-350 and ball.xcor() <-340 and (ball.ycor()-player_2.ycor() < 50 and ball.ycor()-player_2.ycor() > -50):
        ball.setx(-340)
        ball.dx*=-1
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
    if ball.xcor()>390:
        score_2+=1
        ball.setx(390)
        ball.dx*=-1
    if ball.xcor()<-390:
        score_1+=1
        ball.setx(-390)
        ball.dx*=-1
    '''
    if player_1.ycor()>240:
        player_1.ycor=240
    if player_1.ycor() <-240:
        player_1.ycor =-240
    if player_2.ycor() > 240:
        player_2.ycor()=240
    if player_2.ycor() <-240:
        player_2.ycor()= -240
    '''
    pen.clear()
    pen.write("player 2:{} player 1:{}".format(score_2,score_1),align="center",font=("courier",18,"normal"))
