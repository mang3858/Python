#문자열 입력 받아 역순 출력

str1 = input("문자열 입력:")

#방법1
reverse =""
for i in str1:
    reverse = i + reverse
print(reverse)

#방법2
print(str1[::-1])

#방법3
length = len(str1)
for i in range(length-1, -1, -1):
    print(str1[i], end="")
print() #줄바꿈

##문자열을 입력받아 알파벳의 수를 세어서 출력하시오. (단, 인덱싱의 원리를 쓰지 않는다)
str1 = input("문자열 입력:")

cnt=0
for ch in str1:
    if ch >= 'A' and ch <= 'Z':
       cnt += 1
    elif ch >= 'a' and ch <='z':
         cnt += 1
print(cnt)
