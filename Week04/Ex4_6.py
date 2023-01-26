#10진수를 2진수로 변환하여 출력하기
#출력형식 : 13 --> 1101

x = int(input("숫자 입력:"))
y=""
print("%d" %x, end = "")

while x > 0:
    y = str(x % 2) + y
    x //= 2
    
print(" --> %s" %y)



    
