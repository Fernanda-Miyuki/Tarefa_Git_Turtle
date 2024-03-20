from turtle import *

speed()

bgcolor("green")

#céu
penup()
goto(-400,-100)
pendown()
color("deepskyblue")
begin_fill()
for i in range(2):
    forward(900)
    left(90)
    forward(900)
    left(90)
end_fill()

#sol
penup()
goto(-300,225)
pendown()
color("yellow")
begin_fill()
circle(40)
end_fill()

#base da casa
penup()
goto(-100,-100)
pendown()
pensize(3)
color("yellow")
begin_fill()
for i in range(4):
    forward(170)
    left(90)
end_fill()

#chaminé
penup()
goto(20,130)
pendown()
color("red")
begin_fill()
for i in range(2):
    forward(40)
    left(90)
    forward(100)
    left(90)
end_fill()

#telhado
penup()
goto(-127,70)
pendown()
begin_fill()
for i in range(3):
    forward(225)
    left(120)
end_fill()

#janela
penup()
goto(0,0)
pendown()
color("black", "white")
begin_fill()
for i in range(4):
    forward(50)
    left(90)
end_fill()

penup()
goto(0,25)
pendown()
color("black")
forward(50)

penup()
goto(25,0)
pendown()
left(90)
forward(50)

#outra janela
penup()
goto(-80,0)
pendown()
right(90)
color("black", "white")
begin_fill()
for i in range(4):
    forward(50)
    left(90)
end_fill()

penup()
goto(-80,25)
pendown()
color("black")
forward(50)

penup()
goto(-55,0)
pendown()
left(90)
forward(50)

#porta
penup()
goto(-40,-97)
pendown()
right(90)
color("red")
begin_fill()
for i in range(2):
    forward(50)
    left(90)
    forward(80)
    left(90)
end_fill()

penup()
goto(-30,-60)
pendown()
color("black")
begin_fill()
circle(5)
end_fill()

hideturtle()
done()
