'''
-1이 입력되기 전까지 정수를 하나씩 입력 받아 리스트에 저장한다.
찾고자 하는 키값(정수)를 입력하여 그 정수의 위치가 찾아주는 프로그램을 작성하시오.
'''
nums = []

while True:
    num = int(input("수를 입력하시오(-1이면 입력끝): "))
    if num == -1:
        break
    nums.append(num)

key = int(input("찾고 싶은 값을 입력하시오: "))

print("찾는 값의 위치 : ", nums.index(key))

