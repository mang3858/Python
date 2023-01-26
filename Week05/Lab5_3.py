#한화를 입력 받아 환전하는 프로그램 작성
#환전계산을 위한 국가, 화폐단위, 환율은 아래 표를 참조하여 리스트에 저장한 후 이용
#환율에 따른 환전 계산을 위한 함수: exchange()
#공식: 환전금액 = 한국돈 / 매매기준율
#입력 값: 한국돈, 환전 금액, 나라명
def exchange(m, rate):
    exchange_money = m / rate
    print("환전된 금액은 %.2f입니다" %exchange_money)

Exchange_Rate = [["미국", 1270.50], ["일본", 975.36], ["유럽", 1345.21], ["중국", 189.44], ["영국",1571.67]]
money = int(input("환전 금액을 입력하시오: "))
country =  input("나라명을 입력하시오: ")

for i in Exchange_Rate:
    if country == i[0]:
        exchange(money, i[1])

