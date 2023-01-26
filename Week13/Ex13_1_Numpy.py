import numpy as np

#datas에 있는 값에 10씩 더하여 새로운 리스트 만들기
datas  = [1, 2, 3, 4, 5]
result = []
for i in datas:
    result.append(i + 15)
print(result) #[16, 17, 18, 19, 20]

#Numpy를 이용하자
arr = np.array(datas)
result1 = arr + 10#배열(행렬의 개념은)은 리스트,와 달리 ,가 들어가지 않음
print(result1) #[11 12 13 14 15]

result1_bool = result1 % 2 == 0 #짝수일 때 True이고 아니면 False 저장
print(result1_bool) #[False  True False  True False]
print(result1[result1_bool]) #배열명[조건식]이면 조건식이 참인 것만 출력 

