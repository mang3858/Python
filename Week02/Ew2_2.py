#날짜를 입력받아서 초로 변환하는 프로그램

#입력문
'''
days = input("Enter a days : ")
days = int(days)
'''
days = int(input("Enter a days : "))
#파이썬에서 input에 입력값은 string 타입임 

#처리(계산)
seconds = days * (60 * 60 * 24)
#1분(60초) * 1시간(60분) * 하루(24시간)
#최소단위값을 써주기 미리 계산하지 말고

#출력
print(days, "일은 ", seconds, "초이다")
#,는 자동으로 공백이 들어감 ex)5 일은  432000 초이다
#문자열로 형변화 -> 공백없이 출력가능
print(str(days) + "일은 " + str(seconds) + "초이다")
#print문을 C언어 처럼 ,대신 % 사용
print("%d일은 %d초이다" %(days, seconds))
