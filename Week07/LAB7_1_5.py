'''
• 3개의 방 중 한 곳에 숨어 버린 범인을 찾아라!
• 범인이 숨은 방을 맞추면 100점 추가 후 게임 종료. 
• 하지만 틀리면 범인은 다른 방에 숨고 10점 감점 후 다시 맞추기
'''
import random
criminal = random.randrange(1, 4)
num = int(input("방 번호를 입력 하세요: "))

score = 0
while criminal != num:
    print("범인이 없습니다.")
    score -= 10
    
    criminal = random.randrange(1, 4)
    num = int(input("방 번호를 입력 하세요: "))

if criminal == num:
    print("범인 체포!\n게임 종료")
    score += 100

print("점수: %d점" %score)

'''
import 코드 random
score = 0

while True:
room = random.randint(1,3)
n = int(input("방 번호를 입력 하세요: "))

if n == room :
    print("범인 체포!")
    score += 10
    break
elif n > 3:
    print(n,"번 방은 없습니다.")
else:
print("범인이 없습니다.")
'''
