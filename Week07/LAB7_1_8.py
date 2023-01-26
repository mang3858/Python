#정수를 입력받아 정수만큼 별(*)prin 기호를 출력하는 프로그램을 작성하시오.
#(단, 두 자리 이상의 정수는 자리수를 분리하여 하트 기호를 출력한다.)

n = input("문자열 정수 입력: ")

i = 0
for i in range(len(n)):
    heart_num = int(n[i])
    heart =""
    for j in range(heart_num):
        heart += '*'
    print(heart)



'''
n = input("문자열 정수 입력: ")

i = 0
for i in range(len(n)):
    heart_num = int(n[i])
    heart =""
    for j in range(heart_num):
        heart += '*'
    print(heart)'''
