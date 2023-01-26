#turtle을 이용해서 사각형 4개 그리기
import turtle
import random

t1 = turtle.Turtle()
t1.shape("turtle")


for j in range(4):
    x = random.randint(0, 300)
    y = random.randint(0, 300)
    for i in range(4):
        t1.forward(200)
        t1.right(90)
    t1.goto(x, y)
    #t1.forward(200)
    
    
