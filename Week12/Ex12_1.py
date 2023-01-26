#나이에 따른 연봉 그래프
'''
from matplotlib import pyplot as plt

x = [20, 30, 40, 50] 
y = [300, 400, 500, 350]
plt.plot(x, y, '*:r', ms=20, mec='r', mfc='y') 
plt.title("salary by age") 
plt.xlabel("Age") 
plt.ylabel("Pay") 
plt.legend(['Money'])
plt.show( )
'''

#plt.rcParams['font.family'] = 'Malgun Gothic' //한글 깨짐
'''
from matplotlib import pyplot as plt

x = [20, 30, 40, 50] 
y = [300, 400, 500, 350]
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.plot(x, y, '*:r', ms=20, mec='r', mfc='y') 
plt.title("나이에 따른 연봉 그래프") 
plt.xlabel("나이") 
plt.ylabel("연봉") 
plt.legend(['돈'])
plt.show( )'''

#2023, 2025 그래프 2개 
from matplotlib import pyplot as plt

x = [20, 30, 40, 50] 
y1 = [300, 400, 500, 350]
y2 = [330, 404, 550, 320]
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.plot(x, y1, 'o-b', mec='blue', mfc='blue')
plt.plot(x, y2, 'x:r', mec='red', mfc='red') 
plt.title("나이에 따른 연봉 그래프") 
plt.xlabel("나이") 
plt.ylabel("연봉") 
plt.legend(['2023', '2025'], loc="upper right")
plt.show( )
