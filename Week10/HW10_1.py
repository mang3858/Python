#람다식을 이용하여 화씨 온도를 섭씨온도로 변환하는 프로그램을 작성하시오.
f_temp = [0, 30, 50, 70, 100]
c_temp = list(map(lambda x: round((5.0/9.0)*(x-32.0), 2), f_temp))
print(c_temp)
