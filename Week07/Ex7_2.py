money_rate = {"미국":1256, "중국":125, "일본":200, "영국":246}

money = int(input("환전할 금액을 입력하시오: "))
contry = input("원하는 나라를 입력하시오: ")
if contry in money_rate:
    print(money / money_rate[contry])


