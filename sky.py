import turtle
import os
import random
import time

score = 0
lives = 3

wn = turtle.Screen()
wn.title("Falling Skies")
wn.bgcolor("green")
wn.bgpic("background.gif")
wn.setup(width=800, height=600)
wn.tracer(0)

wn.register_shape("sphere.gif")
wn.register_shape("flower.gif")
wn.register_shape("diamond.gif")

player = turtle.Turtle()
player.speed(0)
player.shape("diamond.gif")
player.color("white")
player.penup()
player.goto(0, -250)
player.speed = 0.2
player.direction = "stop"

good_guys = []

for _ in range(20):
	good_guy = turtle.Turtle()
	good_guy.speed(0)
	good_guy.shape("flower.gif")
	good_guy.color("blue")
	good_guy.penup()
	good_guy.goto(-100, 250)
	good_guy.speed = random.uniform(0.1, 1)
	good_guys.append(good_guy)

bad_guys = []

for _ in range(20):
	bad_guy = turtle.Turtle()
	bad_guy.speed(0)
	bad_guy.shape("sphere.gif")
	bad_guy.color("red")
	bad_guy.penup()
	bad_guy.goto(100, 250)
	bad_guy.speed = random.uniform(0.1, 1)
	bad_guys.append(bad_guy)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.goto(0, 260)
font = ("Courier", 24, "normal")
pen.write("Dharma: {}  Kharma: {}".format(score, lives), align="center", font=font)

def go_left():
	player.direction = "left"

def go_right():
	player.direction = "right"

def move_player():
	x = player.xcor()
	x += player.speed
	if x < -350:
		x = -350
	if x > 350:
		x = 350
	player.setx(x)

def play_sound(sound_file, time = 0):
	os.system("aplay -q {}&".format(sound_file))

wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

while True:

	wn.update()
	move_player()

	if player.direction == "left":
		x = player.xcor()
		x -= 3
		player.setx(x)

	if player.direction == "right":
		x = player.xcor()
		x += 3
		player.setx(x)

	for good_guy in good_guys:
		y = good_guy.ycor()
		y -= good_guy.speed
		good_guy.sety(y)

		if y < -300:
			x = random.randint(-380, 380)
			y = random.randint(300, 400)
			good_guy.goto(x, y)

		if good_guy.distance(player) < 40:
			os.system("aplay laser2.wav&")
			x = random.randint(-380, 380)
			y = random.randint(300, 400)
			good_guy.goto(x, y)
			score += 10
			pen.clear()
			pen.write("Dharma: {}  Kharma: {}".format(score, lives), align="center", font=font)

	for bad_guy in bad_guys:
		y = bad_guy.ycor()
		y -= bad_guy.speed
		bad_guy.sety(y)

		if y < -300:
			x = random.randint(-380, 380)
			y = random.randint(300, 400)
			bad_guy.goto(x, y)

		if bad_guy.distance(player) < 40:
			os.system("aplay explosion2.wav&")
			x = random.randint(-380, 380)
			y = random.randint(300, 400)
			bad_guy.goto(x, y)
			score -= 10
			lives -= 1
			pen.clear()
			pen.write("Dharma: {}  Kharma: {}".format(score, lives), align="center", font=font)

wn.mainloop()