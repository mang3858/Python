#세명의 학생이 2과목 시험 본 점수를 2차원 리스트에 보관하기

scores = [["kim", 70, 80], ["hong", 100, 50], ["shin", 80, 90]]
print(scores[0][0], scores[1][0], scores[2][0]) #이름만 출력

#다른 방법
studentA = ["kim", 70, 80]
studentB = ["hong", 100, 50]
studentC = ["shin", 80, 90]
student_scores = [studentA, studentB, studentC]
print(studentA[0])
print(student_scores[0][0])


