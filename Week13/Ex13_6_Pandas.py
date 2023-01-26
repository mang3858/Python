import pandas as pd

#리스트로 DataFrame만들기
score = [[50, 80], [90, 90], [78, 90]]
df = pd.DataFrame(score, columns=["kor", "eng"], index=["학생1", "학생2", "학생3"])
print(df)

#딕셔너리 DataFrame만들기
score = {"이름":["신짱구", "최자두", "코난"], "국어":[50, 90, 90], "영어":[80, 90, 90]}
df2 = pd.DataFrame(score)
print(df2)

#csv파일에서 불러오기
scores = pd.read_csv("scores.csv")
print(scores)

#scores 데이터 프레임을 대상으로 인덱스, 컬럼, 값 출력
print(scores.index)
print(scores.columns)
print(scores.values)

#데이터 프레임의 헹과 열 수 출력
row, col = scores.shape
print(f'행: {row}, 열: {col}')

#데이터 프레임을 csv형식으로 저장하기
scores.to_csv("score2.csv")

#인덱스 변경
scores2 = scores.set_index("이름")


scores.set_index("이름", inplace=True)
print(scores)
print(scores.index)
scores.reset_index(inplace=True)
print(scores)

col_name = ["name", "age", "sex", "grade"]
scores.columns = col_name
print(scores)

scores.rename(columns={"name":"이름", "age":"나이","sex":"성별", "grade":"평점"}, inplace=True)#원본이 바뀌길 원하면 inplace
print(scores)

#열 단위 데이터 추출 - 시리즈 단위로 출력
print(scores["이름"])

#서브 데이터 프레임 추출
out = ["이름", "나이"]
print(scores[out]) #print(scores[ ["이름", "나이"] ])
