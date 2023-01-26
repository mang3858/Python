#파일 쓰기
f = open("output1.txt", "w")
for i in range(10):
    f.write("안녕하세요\n")#f.write("안녕하세요" + \n")
f.close()

f = open("output1.txt", "r")
for line in f: #파일 읽기 가능
    print(line)
f.close()
