import numpy as np

A = np.array([1, 5, 3, 4, 2])
B = np.array([10, 50, 30, 40, 20])
C = A + B #일대일로 대응해서 더해짐 
print(C) #[11 22 33 44 55]

#40이 넘는 값만 출력 
result = C > 40
print(C[result])
