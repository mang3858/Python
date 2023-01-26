#정수를 입력받아 각 자리수의 합을 구하는 프로그램 작성
#ex) 입력이 54321이면  5+4+3+2+1 = 15

num = int(input("정수를 입력받으시오:"))#54321

total = 0
for i in str(num): #str(54321) ==> "54321"
    total += int(i) #int("5")

print(total)
