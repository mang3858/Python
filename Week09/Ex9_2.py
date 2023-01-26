list1 = []
for i in range(10):
    if i % 2 == 0:
        list1.append(i)
print(list1)

l = list(range(0, 10, 2))
print(l)

list2 = [i for i in range(0, 10, 2)]
print(list2)

list3 = [i for i in range(0, 10, 2) if i % 2 == 0]
print(list3)
