#학년 구하기
#8세 ~ 13세: 초등학생, 14세 ~ 16세: 중학생, 17 ~ 19세: 고등학생으로 출력하기
#이름과 현재년도와 태어난 년도를 입력받아 나이를 구한 후
#나이에 따라 학년을 출력하는 프로그램 작성하기
#나이 구하기 = 현재년도 - 태어난 년도 + 1

name = input("당신의 이름을 입력하시오: ")
year = int(input("현재 년도를 입력하시오: "))
birth = int(input("현재 년도를 입력하시오: "))
age = year - birth + 1

if age >= 8 and age <= 13:
    schoolYear = '초등학생'
elif age >= 13 and age <= 16:
    schoolYear = '중학생'
elif age >= 17 and age <= 19:
    schoolYear = '고등학생'
else:
    schoolYear = '기타 등등'

print("%s님의 학년은 %s입니다." %(name, schoolYear))
    
