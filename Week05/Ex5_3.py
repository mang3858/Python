#함수 연습
#3개의 정수를 매개변수로 전달받아 최대값을 구하여 반환하는 함수를 작성하시오

def get_max(a, b, c):
    max = a
    if max < b:
        max = b
    if max < c:
        max = c
    return max

n1 = int(input("정수1을 입력하시오:"))
n2 = int(input("정수2을 입력하시오:"))
n3 = int(input("정수3을 입력하시오:"))

print("세 수의 최대값=", get_max(n1, n2, n3))


