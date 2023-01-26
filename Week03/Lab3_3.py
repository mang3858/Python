#양수, 음수, 0 판별하기

num = int(input("정수를 입력하시오: "))

if num > 0:
    result = '양의 정수'
elif num < 0:
    result = '음의 정수'
else:
    result = 0

print("%d는 %s입니다." %(num, result))
