list1 = ['tic', 'tac', 'toe']

for i in range(3):
    print(i, list1[i])

#리스트에 인덱스 번호 함께 출력하기
list1 = ['tic', 'tac', 'toe']
for i in list1:
    print(list1.index(i), i)

for idx, v in enumerate(list1):
    print(idx, v)

#문자열을 인덱스와 값으로 딕셔너리 만들기
str1 = "Have a nice day"
words = str1.split()
dict1 = {idx:v for idx, v in enumerate(words)}
print(dict1)
