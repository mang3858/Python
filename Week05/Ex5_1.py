'''
#문자열 실습:
str1 = "hello world hi xyz day def"
words = str1.split(" ") #공백을 기준으로 분리하겠다
print(words)

#세개의 단어를 결합시켜서 암호문으로 만들겠다
#result = ''.join(words[0])
#result = result.join(words[3])
result = '-'.join(words)
print(result)

import random
pwd = random.sample(words, 3)
pwds = ''.join(pwd)
print(pwds)'''

#주민등록번호를 8자리 입력받아서 성별과 나이를 구하시오.
#입력형식 : yymmdd-f
#f자리가 1, 2이면 1900년대 3,4면 2000년대
today = 2022
id = input("주민등록번호 일부를 입력하시오(yymmdd-f): ")

if id[7] == '1' or id[7] == '3':
    gender = "남자"
elif id[7] == '2' or id[7] == '4':
    gender = "여자"
print("당신의 성별은 %s이군요" %gender)

#010519
if id[7] == '1' or id[7] == '2':
     year = 1900 + int(id[:2])
     age = today - year + 1
elif id[7] == '3' or id[7] == '4':
    year = 2000 + int(id[:2])
    age = today - year + 1
print("당신의 나이는 %d이군요" %age)
