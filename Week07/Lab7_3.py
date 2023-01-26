#가위바위보 게임
import random

#컴퓨터는 1~3 난수를 발생하여 이를 딕셔너리의 key로 저장하고, key에 대한 value으로 가위바위보 지정
rps_dic = {1:"가위", 2:"바위", 3:"보"}

#가위바위보가 이기는 경우에 대한 정보를 딕셔너리에 저장
match_table = {"가위":"보", "바위":"가위", "보":"바위"}

def match(c, m):
    if c== m:
        return "비김"
    elif match_table[c] == m:
        return "컴퓨터가 승리"
    else:
        return "사람이 승리"
    
computer = rps_dic[random.randint(1,3)]
mine = input("가위바위보 중 하나를 내시오: ")
result = match(computer, mine)
print("컴퓨터: ", computer)
print(result)
