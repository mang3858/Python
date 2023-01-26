#산점도 그래프

import matplotlib.pyplot as plt
plt.rc('xtick', labelsize=9) # x축 눈금 폰트 크기
plt.rc('ytick', labelsize=8) # y축 눈금 폰트 크기

#1일, 자동차 연식에 따른 속도
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
plt.scatter(x, y)

#2일, 자동차 연식에 따른 속도
x = [2,2,8,1,15,8,12,9,7,3,11,4,7]
y = [100,105,84,105,90,99,90,95,94,100,79,112,91]
plt.scatter(x, y)

plt.show()
