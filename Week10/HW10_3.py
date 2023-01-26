'''
◼ 텍스트 파일 “data.txt”에 실수들이 저장되어 있다고 가정하고, 한 줄에 하나의 실수
만 저장되어 있다. 이 파일을 읽어서 합계와 평균을 계산한 후 이를 output.txt 파일
에 저장하는 프로그램을 작성하시오.
'''
infile = open("data.txt", "r")
outfile = open("ouput.txt", "w")

total = 0
count = 0
for line in infile :
    num = float(line.rstrip( ))
    total += num
    count+= 1
outfile.write("합계:"+str(total) +"\n")
outfile.write("평균:"+str(total/count))

infile.close( )
outfile.close( )
