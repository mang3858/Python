#요일별 기온 그래프 2개의 막대 그래프(겹쳐서 나옴)
'''
import matplotlib.pyplot as plt

X = [ "Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun" ] 
Y1 = [-8, -5, -3, -4, -1, -10, -7]
Y2 = [-6, -4, -1, -7, -6, -12, -5]

plt.title("temperature per week")
plt.bar(X, Y1, color='orange', width=0.3)
plt.bar(X, Y2, color='blue', width=0.2)
plt.xlabel("week")
plt.ylabel("temperature")
plt.legend(['1week', '2week'])
plt.show()
'''
#요일별 기온 그래프 2개의 막대 그래프(따로 나옴)
import matplotlib.pyplot as plt
import numpy as np

X = [ "Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun" ] 
Y1 = [-8, -5, -3, -4, -1, -10, -7]
Y2 = [-6, -4, -1, -7, -6, -12, -5]

plt.figure()#차트 전체 영역
plt.title("temperature per week")

idx = np.arange(len(X)) #스칼라 값

plt.bar(idx+0, Y1, color='orange', width=0.3)
plt.bar(idx+0.3, Y2, color='blue', width=0.2)

plt.xticks(idx, X) #축 
plt.xlabel("week")
plt.ylabel("temperature")
plt.legend(['1week', '2week'])
plt.show()
