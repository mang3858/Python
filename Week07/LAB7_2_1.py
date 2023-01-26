'''
리스트에 저장된 색상으로 정삼각형을 랜덤한 위치에 랜덤한 크기의 10개 그리는 프로그
램을 작성하시오.
✓색상 : red, green, blue, orange, yellow, purple
✓다각형의 위치 : -300 ~ 300
✓다각형의 한 변 의 길이 : 10 ~ 100
'''
import turtle
import random

t = turtle.Turtle()
t.width(4) #펜의 두께 ==> t,pensize(4)
colors=['red', 'green', 'blue', 'orange', 'yellow', 'purple']

for i in range(10):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(10, 200)
    t.penup() #t.up()
    t.goto(x, y)
    t.pendown() #t.down()
    index = random.randint(0, 5)
    color = colors[index]

    for i in range(3):
        t.color(color)
        t.forward(length)
        t.left(360/3) #360/각형 수
