'''
n개의 수강 과목의 점수를 입력받아 리스트에 저장하고, ‘합격’과 ‘불합격’ 한 과목의
수를 각각 출력하시오.(합격 기준: 80점 이상)'''

num = int(input("수강 과목 수 입력 : "))
pass1 = 0
fail = 0
scores = []

for i in range(1, num + 1):
    score = int(input("score %d : " %i))
    scores.append(score)

for sc in scores:
    if sc >= 80:
        pass1 += 1
    elif sc < 80:
        fail += 1

print("-"*50)
print("합격과목 수 : %d" %pass1)
print("불합격과목 수 %d" %fail)

