#사용자로부터 신장과 
def BMI(height, weight):
    return weight / (height * height)

def result_print(result):
    print("당신의 체지방 지수는 %.2f입니다." %result)
    if result < 18.5:
        print("당신은 저체중입니다.")
    elif result <= 22.9:
        print("당신은 정상입니다.")
    elif result <= 24.9:
        print("당신은 과체중입니다.")
    elif result >= 25 and result <= 29.9: #이미 위조건에서 안맞으니까 내려옴 따라서 elif result <= 29.9:만 써도 가
        print("당신은 정상입니다.")
    else:
        print("당신은 고도비만입니다.")
    

h = float(input("키를 m단위로 입력: ")) 
w = float(input("키를 kg단위로 입력: "))

result = BMI(h, w)
result_print(result)
