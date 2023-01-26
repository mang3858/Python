#1. 매개변수는 있고 리턴은 없는 함수
#   주민번호를 매개변수로 전달받아 성별을 구하여 출력하는 함수 작성

#주민등록번호를 8자리를 입력받아 성별과 나이를 구해서 리턴하라
#단, 출력은 main에서 출력한다
#입력형식 : yymmdd-f
#f자리가 1, 2이면 1900년대 3,4면 2000년대

def get_gender(str1):
    if str1[7] == '1' or str1[7] == '3':
        print("남자")
    elif str1[7] == '2' or str1[7] == '4':
        print("여자")
        
def get_age(str1):
    today = 2022
    
    if str1[7] == '1' or str1[7] == '2':
         year = 1900 + int(str1[:2])
    elif str1[7] == '3' or str1[7] == '4':
        year = 2000 + int(str1[:2])
        
    age = today - year + 1
    return age
    
no = input("주민등록번호 일부를 입력하시오(yymmdd-f): ")
get_gender(no)
print("당신의 나이는", get_age(no), "살이다.")

#2. 매개변수와 리턴이 있는 함수
#   주민번호를 매개변수로 전달받아 나이를 구하여 반환하는 함수 작성하기
    
