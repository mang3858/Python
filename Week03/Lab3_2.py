#홀수, 짝수 판별하

num = int(input("정수를 입력하시오: "))

if num % 2 == 0:
    result = '짝수'
else:
    result = '홀수'

print("%s입니다." %result)
