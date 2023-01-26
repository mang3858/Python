#약수를 구하는 프로그램을 while문으로 작성하시오.

num = int(input("양의 정수 입력: "))

i = 1
cnt = 0
while i <= num:
    if num % i == 0:
        print(i, end = " ")
        cnt += 1
    i += 1

print()
print("약수의 갯수:", cnt)


