#반복문을 이용하여 누적합 구하기

scores = [50, 60, 100, 90, 70]
total = 0

#for 변수 in 리스트
for i in scores:
    total += i
    
print("합은 = %d" %total)
