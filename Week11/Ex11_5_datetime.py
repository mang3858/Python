#함수관련 시험문제 
import datetime as d

#print(dir(d.time))
t_day = d.date.today()
print(t_day)

print(t_day.year)
print(t_day.month)
print(t_day.day)
print(t_day.weekday()) #0-월요일
print(t_day.isoweekday()) #0-일요일

t_day = d.datetime.today()#datetime안에  datetime이 있는 것
print(t_day)

a_day = d.date(2004, 12, 25)
b_day = d.date(2023, 12, 25)
print(b_day - a_day) #지난 날짜 + 시간과 함께 나옴
print((b_day - a_day).days) #날짜만 구해줌(시간은 나오지 않음)

import time
print(time.localtime())
print(time.strftime("%Y-%m-%d", time.localtime()))
print(time.strftime("%c", time.localtime()))

#시간을 초단위로 구해줌
print(time.time()) #초단위로 1970-1-1
print("start")
time.sleep(3)
print("stop")
