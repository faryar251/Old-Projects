import turtle
import winsound

# starting
wn=turtle.Screen()
wn.title("PONG GAME")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
b_speed = 0.2

#Score
SA=0
SB=0


# Paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


# Paddle B 
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)


# Ball 
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = b_speed
ball.dy = b_speed


#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A : {}	  Player B : {}".format(SA,SB), align = "center", font = ("Courier",24,"normal"))

#Game Over
Fin = turtle.Turtle()
Fin.speed(0)
Fin.color("red")
Fin.penup()
Fin.hideturtle()
Fin.goto(0,0)
#Fin.write("GO", align = "center", font = ("Courier",24,"normal"))

#function
def paddle_a_up():
	y = paddle_a.ycor()
	y+=20
	paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor()
	y-=20
	paddle_a.sety(y)

def paddle_b_up():
	y = paddle_b.ycor()
	y+=20
	paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor()
	y-=20
	paddle_b.sety(y)




#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


#main game loop
while True:
	wn.update()

	# Move the ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	# Border Checking
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1
		winsound.PlaySound("C:/Users/ASUS/OneDrive/Desktop/webp/Python projects/Sounds/bounce.wav", winsound.SND_ASYNC)

	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1
		winsound.PlaySound("C:/Users/ASUS/OneDrive/Desktop/webp/Python projects/Sounds/bounce.wav", winsound.SND_ASYNC)

	if ball.xcor() > 390:
		ball.goto(0,0)
		ball.dx *= -1
		SA+=1
		pen.clear()
		pen.write("Player A : {}	  Player B : {}".format(SA,SB), align = "center", font = ("Courier",24,"normal"))

	if ball.xcor() < -390:
		ball.goto(0,0)
		ball.dx *= -1
		SB+=1
		pen.clear()
		pen.write("Player A : {}	  Player B : {}".format(SA,SB), align = "center", font = ("Courier",24,"normal"))

	# paddle and ball collision

	if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
		ball.setx(340)
		ball.dx *= -1
		winsound.PlaySound("C:/Users/ASUS/OneDrive/Desktop/webp/Python projects/Sounds/bounce.wav", winsound.SND_ASYNC)

	if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
		ball.setx(-340)
		ball.dx *= -1
		winsound.PlaySound("C:/Users/ASUS/OneDrive/Desktop/webp/Python projects/Sounds/bounce.wav", winsound.SND_ASYNC)

	if SA >2 or SB >2:
		SA, SB = 0 , 0
		pen.clear()
		pen.write("Player A : {}	  Player B : {}".format(SA,SB), align = "center", font = ("Courier",24,"normal"))
		b_speed+=0.1

	if b_speed >=0.6:
		ball.goto(0,0)
		ball.hideturtle()
		paddle_a.hideturtle()
		pen.clear()
		paddle_b.hideturtle()
		pen.clear()
		Fin.clear()
		Fin.write("GAME OVER", align = "center", font = ("Courier",30,"normal"))
	



