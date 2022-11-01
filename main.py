import turtle
from turtle import Turtle, Screen
import random
# import colorgram
# colors = colorgram.extract('image.jpg', 30)
# book = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     book.append(new_color)
# print(book)
# turtle.colormode(255)

# 1.

# screen = Screen()
# screen.setup(500, 500)
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red")
# timmy.penup()
# timmy.goto(-230, 0)
# tom = Turtle()
# tom.shape("turtle")
# tom.color("yellow")
# tom.penup()
# tom.goto(-230, 66.66)
# jerry = Turtle()
# jerry.shape("turtle")
# jerry.color("orange")
# jerry.penup()
# jerry.goto(-230, 133.32)
# samreen = Turtle()
# samreen.shape("turtle")
# samreen.color("blue")
# samreen.penup()
# samreen.goto(-230, -66.66)
# kamran = Turtle()
# kamran.shape("turtle")
# kamran.color("green")
# kamran.penup()
# kamran.goto(-230, -133.32)
# maha = Turtle()
# maha.shape("turtle")
# maha.color("black")
# maha.penup()
# maha.goto(-230, 200)
# t = screen.textinput(title = "Make a bet", prompt = "Who will win the race? Enter a color: ")
# print(t)
# cond = True
# while cond == True:
#   if timmy.xcor() > 220:
#       print("red won the race!")
#       if timmy.color == t:
#           print("Your bet was correct")
#       else:
#           print("You lost! Try another time.")
#       cond = False
#   elif tom.xcor() > 220:
#       print("yellow won the race!")
#       if tom.color == t:
#           print("Your bet was correct")
#       else:
#           print("You lost! Try another time.")
#       cond = False
#   elif samreen.xcor() > 220:
#       print("Blue won the race!")
#       if samreen.color == t:
#           print("Your bet was correct")
#       else:
#           print("You lost! Try another time.")
#       cond = False
#   elif jerry.xcor() > 220:
#       print("orange won the race!")
#       if jerry.color == t:
#           print("Your bet was correct")
#       else:
#           print("You lost! Try another time.")
#       cond = False
#   elif kamran.xcor() > 220:
#       print("green won the race!")
#       if kamran.color == t:
#           print("Your bet was correct")
#       else:
#           print("You lost! Try another time.")
#       cond = False
#   elif maha.xcor() > 220:
#       print("black won the race!")
#       if maha.color == t:
#           print("Your bet was correct")
#       else:
#           print("You lost! Try another time.")
#       cond = False
#   else:
#       timmy.forward(random.randint(1, 5))
#       tom.forward(random.randint(1, 5))
#       jerry.forward(random.randint(1, 5))
#       samreen.forward(random.randint(1, 5))
#       kamran.forward(random.randint(1, 5))
#       maha.forward(random.randint(1, 5))
# screen.exitonclick()

# 2.

# shades =[(35, 176, 169), (55, 150, 240), (210, 61, 23), (37, 139, 240), (29, 25, 114), (127, 251, 214), (170, 29, 36),
#          (245, 72, 18), (172, 42, 47), (23, 19, 89), (171, 31, 28), (107, 189, 183),
#          (68, 102, 161), (38, 173, 177), (180, 98, 103), (163, 189, 232), (239, 171, 156),
#          (151, 212, 215), (48, 149, 140)]
# timmy.hideturtle()
# timmy.penup()
# timmy.setheading(225)
# timmy.forward(320)
# timmy.setheading(0)
# timmy.pendown()
# def printi():
#   for _ in range(10):
#      j = random.choice(shades)
#      timmy.pencolor(j)
#      timmy.dot(20)
#      timmy.penup()
#      timmy.forward(50)
#      timmy.pendown()
# for _ in range(5):
#    printi()
#    timmy.penup()
#    timmy.left(90)
#    timmy.forward(50)
#    timmy.left(90)
#    timmy.forward(50)
#    printi()
#    timmy.penup()
#    timmy.right(90)
#    timmy.forward(50)
#    timmy.right(90)
#    timmy.penup()
#    timmy.forward(50)
#    timmy.pendown()

# 3.

# def move_forward():
#     timmy.forward(10[])
# def turn_right():
#     timmy.right(10)
# def turn_left():
#     timmy.left(10)
# def move_backward():
#     timmy.back(10)
# def reset():
#     timmy.reset()
# screen.listen()
# screen.onkey(key = "Up", fun = move_forward)
# screen.onkey(key = "Down", fun = move_backward)
# screen.onkey(key = "Right", fun = turn_right)
# screen.onkey(key = "Left", fun = turn_left)
# screen.onkey(key = "c", fun = reset)











