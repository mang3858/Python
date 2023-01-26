#입력받은 수가 소수인지를 판단하는 프로그램을 작성하시오.

num = int(input("양의 정수 입력: "))

flag = 0
for i in range(2, num):
    if num % i == 0:
        flag = 1
        break
    
if flag == 0:
    print(num, "은 소수이다")
else:
    print(num, "은 소수가 아니다")

'''
n = int(input("양의 정수 입력: "))

i = 2
while i < n:
    if n % i == 0:
        break
    i += 1

if i == n:
    print(n, "은 소수이다")
else:
    print(n, "은 소수가 아니다")
'''
