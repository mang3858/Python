#4행 5열의 2차원 리스트를 만들고, 0부터 3의 배수를 출력하는 프로그램을 작성하시오

list1 = []
list2 = []

value = 0
for i in range(4):
    for j in range(5):
        list1.append(value)
        value += 3
    list2.append(list1)
    list1 = []
print(list2)
