#str1= "aBcDe"일 때 대문자 B, D를 출력하는 프로그램을 enumerate()함수를 이용하여 작성하시오

str1 = "aBcEd"
result = [v for i, v in enumerate(str1) if i % 2 == 1]
print(result)
