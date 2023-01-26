#1부터 100까지 1씩 증가하는 자연수에 대해서 369게임을 진행하는 프로그램 작성


'''
#방법1
def game369(num):
    if num % 10 == 3 or num % 10 == 6 or num % 10 == 9:
        return "짝"
    elif num // 10 == 3 or num // 10 == 6 or num // 10 == 9:
        return "짝"
    else:
        return num

for i in range(1, 101):
    print(game369(i), end=" ")
    if i % 10 == 0:
        print("")

#방법2
def game369(num):
    a = num // 10
    b = num % 10
    
    if a != 0 and a % 3 == 0:
        return "짝"
    elif b != 0 and b % 3 == 0:
        return "짝"
    else:
        return num

for i in range(1, 101):
    print(game369(i), end=" ")
    if i % 10 == 0:
        print("")
        '''

#방법3
def game369(num):
    tmp = num
    flag = 0
    while tmp > 0:
        if tmp % 10 == 3 or tmp % 10 == 6 or tmp % 10 == 9:
            return "짝"
        tmp //= 10
    return num

for i in range(1, 101):
    print(game369(i), end=" ")
    if i % 10 == 0:
        print("")
