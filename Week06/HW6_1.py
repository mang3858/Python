import turtle
import random
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

def Square(t, w , h):
    wh =[w,h,w,h]
    for i in wh :
        t.forward(i)
        t.left(90)

def getRGB():
    r, g, b = 0, 0, 0
    
    r = random.random()
    g = random.random()
    b = random.random()
    
    return (r, g, b)

answer = input("색을 입히길 원하십니까?(y or n): ")
if answer == 'y':
    for i in range(8):
        Square(t,100,100)
        t.left(45)
        r, g, b = getRGB()
        t.color(r, g, b)

elif answer == 'n':
    for i in range(8):
        Square(t,100,100)
        t.left(45)
else:
    print("잘못 입력하셨습니다")

