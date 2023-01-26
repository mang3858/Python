#“no”가 입력될 때까지 정수를 입력받아 그 수들의 합을 구하는 프로그램을 작성하시오

num = int(input("숫자를 입력하시오: "))
answer = input("계속?(yes/no): ")
total = 0

while answer != "no":
    print()
    total += num
    num = int(input("숫자를 입력하시오: "))
    answer = input("계속?(yes/no): ")

print("\n합계는 %d입니다." %(total + num))

'''
total = 0
answer = "yes"

while answer == "yes":
    num = int(input("숫자를 입력하시오: "))
    total += num
    answer = input("계속?(yes/no): ")
    print()

print("합계는",total,"입니다.")
'''
