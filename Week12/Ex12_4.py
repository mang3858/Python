#원 그래프

import matplotlib.pyplot as plt

ratio = [20, 30, 10, 40]
labels = ['attendance', 'midterm', 'report' ,'final']
explode = [0.3, 0, 0, 0]

plt.pie(ratio, labels=labels, autopct='%.1f%%', explode=explode, shadow=True)
plt.title("Evaluation rate")
plt.show()
