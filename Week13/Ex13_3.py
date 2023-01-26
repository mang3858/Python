#4명의 학생이 3과목 시험을 봤을 때 합계, 평균
import numpy as np

scores = np.array([[99, 93, 60], [98, 82, 93], [93, 65, 81], [78, 82, 81]])
total = scores.sum(axis=1)
avg = scores.mean(axis=1)
print(total.shape)
print(scores.shape)
last_row = total.shape[0]#배열의 행의 크기

print(last_row)

for i in range(last_row):
    print("학생", (i + 1), total[i], avg[i])

'''
row_cnt = total.shape[0]#배열의 행의 크기
row_cnt, col_cnt = scores.shape

print(row_cnt)
for i in range(row_cnt):
    print("학생", (i + 1), total[i], avg[i])'''
