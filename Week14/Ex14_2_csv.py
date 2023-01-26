import csv

with open("scores.csv", "r", encoding="utf-8") as infile:
    datas = csv.reader(infile)
    header = next(datas) #첫번째 줄 따로 읽기
    print(f'제목줄 : {header}')
    print()
    for line in datas:
        print(line)
with open("hello.csv", "w", encoding="utf-8") as outfile:
    w = csv.writer(outfile, delimiter="#")
    w.writerow("안녕하세요")
    w.writerow(["빅데이터처리 시험 내일"])
    w.writerow(["빅데이터", "처리", "시험", "내일"])
