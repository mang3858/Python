import datetime

print(dir(datetime))
print(datetime.MAXYEAR)
print(datetime.MINYEAR)
today = datetime.date(2022, 12, 25)
print(today)
now = datetime.datetime(2022, 12, 25, 11, 22, 33)
print(now)

#앞에꺼는 패키지 두번째가 모듈
#->datetime패키지 안을 봤더니 datetime 모듈이 있고 그 모듈 안에 now()함수가 있는거
todat = datetime.datetime.now()

