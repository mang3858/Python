'''
주사위를 1000번 던져서 나오는 값들의 빈도수를 계산하는 프로그램을 작성하시오.
✓난수 발생 함수와 리스트 사용
'''

import random

counters = [0] * 6
for i in range(1000):
    value = random.randint(0, 5)
    counters[value] = counters[value] + 1
for j in range(6):
    print("주사위가 %d인 경우는 빈도수는 %d"%(j+1, counters[j]))
