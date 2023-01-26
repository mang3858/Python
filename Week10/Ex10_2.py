#예외처리

'''
a = 10
b = 'abc'
print(a + b) #타입 에러남'''

try:
    a = 10
    b = 'abc'
    print(a + b)
except TypeError:
    print("문자열과 숫자는 더할 수 없다")

try:
    a = 10
    #b = 'abc'
    #print(a + b)
    print(a / 0)
except :#어떤 에러가 나도 밑에 메세지를 출력함 -> 에러를 찾을 수 없음  // 어떤 에러가 날 지 생각하면서 쓰기
    print("문자열과 숫자는 더할 수 없다")

try:
    n = int(input("수 입력: "))
    a = 10
    #b = 'abc'
    #print(a + b)
    c = a / n
except ZeroDivisionError as e:#ZeroDivisionError 이 메서지를 e라는 변수로 받아
    print(e)
    print("0으로 나누면 안돼") 
except TypeError:
    print("문자열과 숫자는 더할 수 없다")
else:#정상적으로 처리되었을 때 출력하라(else에 들어감)
    print(c)
finally:#언제나 수행 되어지는 구문
    print("쉬는 시간")
