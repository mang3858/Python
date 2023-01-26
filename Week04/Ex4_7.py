#내가 1~99사이의 있는 어떤 수를 생각하고 있어
#이 수를 맞추는 게임 만들기
#힌트)보다 큰수를 말해 봐, 보다 작은 수를 말해 봐
#출력 몇 번만에 맞추었는지 시도 횟수를 출력한다

import random
#num =random.randint(1, 99) #1~99사이의 정수 난수 발생
num = 57
cnt = 1

answer = int(input("숫자를 적으시오: "))
while num != answer:
    if (num >answer):
        print("%d보다 큰 수를 말해봐" %answer)
    else:
        print("%d보다 작은 수를 말해봐" %answer)
    cnt += 1
    answer = int(input("숫자를 적으시오"))
else:
    print("정답입니다 %d번 수행" %cnt)
        
        
