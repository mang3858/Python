#양의 정수로 점수를 입력받아 학점을 구분하자
#90점이상 A, 80점이상 B, 70점이상 C, 60점이상 D, 60점 미민 F
#단, 점수는 0에서 100점 사이라고 가정한다.

score = int(input("점수를 입력하시오: "))

if score >= 90:
    grade = 'A'
elif score >= 80: #score < 90 and score >= 80
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else 
    grade = 'F'

print("점수 %d의 당신의 학점은 %s입니다." %(score, grade))

#elif문 대신 if문를 쓴다면 이미 그 조건이 맞는데도 불구하고 조건식을 다 돌고 끝나서 좋은 프로그램이 아님
#elif문을 쓴다면 그 조건식이 맞다면 나옴
