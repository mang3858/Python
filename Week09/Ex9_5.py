words = "The quick brown for jumps over the lazy dog"

'''
list1 = []
for i in words.split():
    #대문자, 소문자, 문자열의 길이를 1차원 리스트로 만들기
    temp = []
    temp.append(i.upper())
    temp.append(i.lower())
    temp.append(len(i))
    #1차원 리스트를 모아서 2차원 리스트로 만들
    list1.append(temp)
print(list1)
'''

#comprehension
list1 = [[w.upper(), w.lower(), len(w)] for w in words.split()]
print(list1)

    
