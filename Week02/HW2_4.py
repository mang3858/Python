'''
Lab2_5
list a 인덱스 3번자리에 9의 값 넣기 - - - - 9
x변수에 0의 값 넣기 0 - - - 9
list a의 인덱스 0번 자리에 인덱스 3번 자리의 값에 4를 더한 값 넣기 0 13 - - 9
list a의 인덱스 1번 자리에 인덱스 3번 자리의 값에 3을 곱한 값 넣기 0 13 27 - 9
변수 x의 값에 1 더한 값 넣기 1 13 27 - 9
list a의 인덱스 3번 자리에 인덱스 0번 자리의 값 넣기 1 13 27 - 13
list a의 인덱스 2번 자리에 인덱스 1번 자리의 값에 5를 더한 값 넣기 1 13 27 32 13
list a의 인덱스 3번 자리에 인덱스 3번 자리의 값에 1를 더한 값 넣기 1 13 27 32 14

Lab2_6
#① ['red', 'yellow', 'green']
#② ['red', 'yellow']
#③ ['red', 'orange', 'yellow']
#④ list color의 길이를 세어주지만 결과창에는 나타나지 않음

Lab2_7
#① [1, 2, 3, 4, 5]
#② 3
#③ [1, 2, 3]
#④ 5
#⑤ [3, 4]
#⑥ [4, 5]

Lab2_8
#① [50, 70, 40]
#② [40, 50, 70]
#③ [40, 80, 50, 70]
#④ [40, 80, 50]
#⑤ [40, 80, 50, 60]
#⑥ [40, 50, 60]

Lab2_9
name = input("영웅들의 이름 입력: ")
heroes.append(name)
name = input("영웅들의 이름 입력: ")
heroes.append(name)
name = input("영웅들의 이름 입력: ")
heroes.append(name)
name = input("영웅들의 이름 입력: ")
heroes.append(name)
name = input("영웅들의 이름 입력: ")
heroes.append(name)
print("-" * 50)
n1, n2, n3, n4, n5 = heroes
print(n1, n2, n3, n4, n5)
#print(heroes[0], heroes[1], heroes[2], heroes[3], heroes[4], heroes[5])
'''
scores = []
sum = 0

score = int(input("성적을 입력하시오: "))
scores.append(score)
sum = sum + score
score = int(input("성적을 입력하시오: "))
scores.append(score)
sum = sum + score
score = int(input("성적을 입력하시오: "))
scores.append(score)
sum = sum + score
score = int(input("성적을 입력하시오: "))
scores.append(score)
sum = sum + score
score = int(input("성적을 입력하시오: "))
scores.append(score)
sum = sum + score

print(scores)
print("성적의 합 = %d" %sum)  #print("성적의 합 = ", sum(scores) ) //sum 변수 선언 지우고 써야함
print("평균 = %.1f" %(sum/5))  
