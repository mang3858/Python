'''
두 수를 입력 받고, 사칙연산 중 하나를 입력 받아 결과를 출력하는 프로그램을 작성하시오.'''

num1 = int(input("첫 번째 수 입력:"))
num2 = int(input("두 번째 수 입력:"))
op = input("원하는 연산 기호 하나 입력:(+ - * /):")

if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
elif op == '/':
    result = num1 / num2

print("%d %s %d = %d" %(num1, op, num2, result))
    
