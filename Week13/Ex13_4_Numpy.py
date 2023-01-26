import numpy as np
import matplotlib.pyplot as plt

X = np.arange(0, 10) #range(10)
Y1 = np.ones(10) #1로 구성
Y2 = X
Y3 = X ** 2
Y4 = np.zeros(10) #0으로 구성 

print(X)
print(Y1)
print(Y2)
print(Y3)
print(Y4)
plt.plot(X, Y1, X, Y2, X, Y3)
plt.show()

X1 = np.linspace(-2 * np.pi, 2 * np.pi, 100) #-2 * np.pi부터 2 * np.pi까지 데이터 100개
Y5 = np.sin(X1)
Y6 = 3 * np.sin(X1)
plt.plot(X1, Y5, X1, Y6)
plt.show()
