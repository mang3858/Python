#version1

'''
print("Enter your name: ")
somebody = input()
print("Hi", somebody, "How are you today?")
'''

'''
주석 여러줄
'''

#version2
'''
somebody = input("Enter your name: ")
print("Hi", somebody, "How are you today?")
'''

#version3 - print()함수 줄바꿈 없애기
print("Enter your name: ", end = '') #print함수의 자동 줄바꿈 해지
somebody = input()
print("Hi", somebody, "How are you today?")
