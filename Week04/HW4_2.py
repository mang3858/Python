'''
컴퓨터가 생성한 두 자리 정수 덧셈 문제에 대한 정답을 사용자로부터 입력 받아 ‘맞
았다’ 또는 ‘틀렸다’를 출력한다. 맞은 개수가 5개가 되면 프로그램을 종료한다.
▪ 두 자리 정수는 난수로 생성한다
'''
import random
num1 =random.randint(1, 99)
num2 =random.randint(1, 99)

print("<< 덧셈 문제 연습 게임 >>")
print("-"*50)
cnt = 1
pass1 = 1

answer = int(input("%d + %d = " %(num1, num2)))
while pass1 != 5:
    cnt += 1
    if (answer == num1+num2):
        print("맞았다.")
        pass1 += 1
    else:
        print("틀렸다.")
        
    num1 =random.randint(1, 99)
    num2 =random.randint(1, 99)
    answer = int(input("%d + %d = " %(num1, num2)))
else:
    print("맞았다\n시도횟수 : %d" %cnt)
