#3명의 학생이 4과목 시험을 봤을 때 과목별로 평균 구하기 -> 시험 문제~

studentA = [96, 84, 80, 70]
studentB = [96, 86, 76, 65]
studentC = [76, 95, 83, 77]
avg = []
for i in range(3):
    total = studentA[i] + studentB[i] + studentC[i]
    avg.append(total)
print(avg)

avg = [sum(x)/3 for x in zip(studentA, studentB, studentC)]
print(avg)
