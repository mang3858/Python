'''
사용자로부터 정수를 입력 받아 이 정수가 2와 3으로 나누어 떨어질 수 있는지를 판단하여 출
력하는 프로그램을 작성하시오.'''

num = int(input("정수 입력:"))

if num % 2 == 0 and num % 3 == 0:
    print("2와 3으로 나누어 떨어진다")
else:
        print("2와 3으로 나누어 떨어지지 않는다")
