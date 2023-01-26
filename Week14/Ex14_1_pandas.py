import pandas as pd
scores = pd.read_csv("scores.csv")
print(scores)

#행 추출
print("-"*10)
print(scores.head(2)) #위에서 두 줄
print("-"*10)
print(scores.tail(1)) #밑에서 한 줄
print("-"*10)
#line1 = scores.loc[0:2]
#print(line1)
line1 = scores.loc[0:2, ["이름", "나이"]]#열의 이름
print(line1)
print("-"*10)
line2 = scores.iloc[2, 3]#열 번호 
print(line2)
print("-"*10)

#조건 적용
print(scores["나이"] > 20)
print("-"*10)
print(scores[scores["나이"] > 20]) #조건이 참인 데이터만 추출
print("-"*10)
print(scores[scores["평점"] < 4.0]) #행을 고르는 조건
print("-"*10)
print(scores.loc[scores["평점"] < 4.0, ["이름", "평점"]]) #ㅣoc속성을 이용하여 열을 고르는 조

#isin() 함수 사용
print("-"*10)
print(scores[scores["이름"] == "김봄"])
print("-"*10)
print(scores["이름"].isin(["나가을"]))
print("-"*10)
print(scores[scores["이름"].isin(["나가을"])])
print("-"*10)

#정렬 - 인덱스 기준  내림차순 정렬 : sort_index(ascending=False)
scores.sort_index(ascending=False)
print(scores)
print("-"*10)
sorted1 = scores.sort_index(ascending=False, inplace = False)
print(scores)
print(sorted1)
print("-"*10)

#sorted1 데이터프레임을 대상으로 index를 이름으로 변경하기
sorted1.set_index("이름", inplace=True)
print(sorted1)
print("-"*10)

sorted1.sort_index(ascending=True, inplace=True)
print(sorted1)
print("-"*10)

print(sorted1.values)
print("-"*10)

#scores 데이터 프레임을 대상으로 값을 가지고 정렬 : sort_values()
sorted2 = scores.sort_values(by=["나이"])
print(sorted2)
print("-"*10)
print(sorted2.loc[:, ["나이", "이름"]])
print("-"*10)

sorted2 = scores.sort_values(by=["성별", "나이"], ascending=[True, False])
print(sorted2.loc[:, ["성별", "나이"]])
print("-"*10)

# 추가 : 열추가 *변경도 가능 
scores["학번"] = ["A001", "A002", "A003", "A004"]
print(scores)
print("-"*10)
scores["학번"] = ["A001", "B002", "A003", "B004"]
print(scores)
print("-"*10)

scores["세대"] = scores["나이"] // 10
print(scores)
print("-"*10)

#행추가: pandas.concat([df1, df2], ingnore_index = True)
new_df = pd.DataFrame({"이름":["홍길동", "신짱구"], "나이": [100, 5]})
scores2 = pd.concat([scores, new_df], ignore_index = True)
print(scores2)
print("-"*10)

#행 삭제 :df.drop()
if 4 in scores2.index:
    scores2.drop(index=4, inplace = True)
    print(scores2)
else:
    print("없다 삭제 못 함")
print("-"*10)

#열 삭제 : df.drop("열이름")
scores2.drop("세대", axis=1, inplace=True)
print(scores2)
print("-"*10)
scores2.dropna(axis=0, inplace=True)
print(scores2)
print("-"*10)

#그룹핑해보기: df.groupby()
print(scores.groupby("성별").mean())
print("-"*10)
print(scores[["성별", "평점"]].groupby("성별").mean())
print("-"*10)

print(scores["성별"].value_counts())
print("-"*10)

#pandas에서 차트 그리기
scores.plot(kind="line", x="이름", y="나이", color="red")
import matplotlib.pyplot as plt
plt.show()
