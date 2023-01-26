#학생 5명의 점수를 입력 받아서 누적합을 구하기

total = 0
for i in range(5):
    score = int(input("점수를 입력하시오:"))
    total += score
else:
    print("종료")

print("누적합은 %d" %total) 
