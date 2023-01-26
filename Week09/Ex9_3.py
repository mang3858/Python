#2개의 문자열을 문자 단위로 결합
word_1 = "Hello"
word_2 = "World"
result = []
for i in word_1:
    for j in word_2:
        result.append(i + j)
print(result)


word_1 = "Hello"
word_2 = "World"
result = [i + j for i in word_1 for j in word_2]
print(result)
