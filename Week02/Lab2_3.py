x = 10
y = 20
print("교환 전: x =", x, "y =",y)

'''
temp = x
x = y
y = temp
'''

#파이썬은 맞교환이 가능함
x, y = y, x
print("교환 후: x =", x, "y =",y)
