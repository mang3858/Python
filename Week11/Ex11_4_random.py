import random

datas = ['red', 'green', 'blue', 'black', 'navy', 'yellow']
print(datas)

#섞기
random.shuffle(datas)
print(datas)

#샘플링(데이터 중에 무작위로 고름) 
for i in range(4):
    print(random.sample(datas, 4))
