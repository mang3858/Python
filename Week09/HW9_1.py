# 단어의 첫 글자만 추출하여 리스트를 생성하는 프로그램을 작성하시오.

'''
words = "The quick brown for jumps over the lazy dog"
list1 = []
for i in words.split():
    first = i[0]
    list1.append(first)
    
print(list1)
'''

words = "The quick brown for jumps over the lazy dog"
list1 = [w[0] for w in words.split()]
print(list1)

