#문자열을 입력받아 축약어의 뜻을 풀이하여 출력하는 프로그램
abbreviation = {"CS":"Computer Sience", "IT":"Infomation Technology", "loT":"Internet of Things", "HAND":"Have a nice day", "thx":"Thanks", "BBL":"Be Back Later"}

abbr = input("축약어를 입력하시오: ")
words = abbr.split()
result = ""

for word in words:
    if word in abbreviation:
        result += abbreviation[word] + " "
    else:
        result += word
print(result)
