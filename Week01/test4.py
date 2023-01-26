import keyword
print(keyword.kwlist)

a = 10
b = '홍길동'
c = 3.14
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))

#누가나올까
#print(a+b)
print(a+c)
print(a+d)

print('이름' + b)

#a랑 b를 이어쓰고 싶다
print(a ,b)

#a랑 b를 띄어쓰기 말고 붙여쓰고 싶다
print(str(10)+b)

print(b*3)
print('안녕하세요' * 100)
print('안녕하세요 ' * 100)
