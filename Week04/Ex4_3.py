#n을 입력받아 팩토리얼을 계산하여 출력하기
#5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input("숫자를 입력하시오:"))
result = 1

print("%d! =" %num, end ='')
for i in range(num, 1, -1):
    print(" %d x " %i, end = '')
    result *= i

print("1 = %d" %result)
