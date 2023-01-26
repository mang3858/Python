import turtle
t = turtle.Turtle() #거북이 한마리 생성
t.shape("turtle")#거북이 모양으로 변경
t.speed(1) #속도가 가장 느림 0: 속도가 가장 빠름

t.color("red")
t.forward(100) #거북이가 보는 방향으로 거리만큼 앞으로 이동
#t.fd(100) 전진하다.
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)

t.penup()
t.color("blue")
t.goto(200, 200) #좌표값(좌표x, y좌표)을 줌 가운데가 0, 0 위 오른쪽 + 아래 왼쪽 -
t.pendown() #펜 내리기
t.width(4)
t.setheading(270) #거북이의 머리 모양 바꿈
t.circle(80) #반지름 80만큼 원 그림

