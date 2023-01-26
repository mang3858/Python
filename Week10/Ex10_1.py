#Lambda 사용법 -> 짧은 조건식

f = lambda x, y: x + y
print(f(1, 7))

g = lambda x : "짝수" if x % 2 == 0 else "홀수"
print(g(4), g(13), g(7))

z = lambda x : "양수" if x > 0 else ("음수" if x < 0 else "0")
print(z(5), z(-5), z(0))

print((lambda x : x**2)(5))#(앞부분이 함수 이름에 해당)(뒷부분이 매개변수)

nums = [10, 2, 3, 7, 5]
f1 = lambda x : x ** 2
print(map(f1, nums)) #<map object at 0x000001657C0EAD40>
nums_list = list(map(f1, nums)) #map 객체 타입을 list타입으로 형 변환
print(nums_list)

#리스트의 요소가 짝수인지 홀수인지 판단하기
g = lambda x : "짝수" if x % 2 == 0 else "홀수"
print(list(map(g, nums)))

#리스트 결과를 딕셔너리로 표현하기
dict1= {}
for k, v in zip(nums, list(map(g, nums))):
    dict1[k] = v
print(dict1)

#리스트의 요소가 짝수인지 홀수인지 판단하기 - 리스트 컴프레인션
list1 = ["짝수" if i % 2 == 0 else "홀수" for i in nums]
print(list1)

#2개의 리스트에서 같은 인덱스 합 구하기
alist = [1, 2, 3, 4, 5]
blist = [5, 6, 7, 8, 9]
f1 = lambda x, y : x + y
print(list(map(f1, alist, blist)))

#2개의 리스트에서 같은 인덱스 합 구하기 - 리스트 컴프레인션
list1 = [x + y for x, y in zip(alist, blist)]
#두개의 리스트를 가져다가 zip으로 패킹해 그리고 x, y로 언패킹 해 그 언패킹한 값들을 더해
print(list1)

list2 = list(filter(lambda x : x % 2 == 0, alist)) #원데이터에서 고르는 것만 가능
print(list2)


