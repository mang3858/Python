'''편의점에서 판매하는 물건의 재고를 딕셔너리에 저장하고 물건이 팔릴 때마다
물건들의 재고를 출력하는 프로그램 작성
- 5개의 물건에 대한 딕셔너리를 생성한다 '''

items = {"커피":15, "펜":3, "종이컵":20, "우유":5, "콜라":7, "라면":20}
print("판매 전 재고:", items)
print()
sell = input("판매할 물건을 입력하시오: ")

for sell in items:
    items[sell] -= 1
else:
    print("판매할 재고가 아닙니다")

print("판매 후 재고:", items)
