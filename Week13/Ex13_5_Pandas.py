#pandas 데이터 생성
import pandas as pd

datas = [50, 80, 90, 30, 60]
ser = pd.Series(datas, name = "score") #nmae은 생략가능
print(ser)
print(ser[4])

ser2 = pd.Series(["김봄", "이가을", "이겨울"], index = ["이름1", "이름2", "이름3"])
print(ser2)
print(ser2[0])
