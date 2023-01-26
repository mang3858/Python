case_1 = ['A', 'B', 'C']
case_2 = ['D', 'E', 'A']

'''
list1 = []
for a in case_1:
    for b in case_2:
        if a!= b:
            list1.append(a + b)
print(list1)

'''

'''
list1 = [a + b for a in case_1 for b in case_2 if not (a == b)] #a != b
print(list1)
'''
list1 = [a + b if not (a == b) else "짝" for a in case_1 for b in case_2 ] 
print(list1)

list1 = [[a + b if not (a == b) else "짝"] for a in case_1 for b in case_2 ] 
print(list1)

list1 = [[a + b if not (a == b) else "짝" for a in case_1] for b in case_2 ] 
print(list1)
