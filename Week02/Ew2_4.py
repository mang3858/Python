#리스트 실습
datas = [10, 20, 30, 'red', 'green', 'blue', 3.14, True]
print(datas)

#인덱싱으로 0번, 3번 데이터 추출
print(datas[0])
print(datas[3])

#빛의 삼원색 추츨하기: 슬라이싱 -> 리스트 형태로 출력
print(datas[3 : 6])

#숫자만 출력해서 리스트 변수에 저
nums = datas[:3]
print(nums)
print(type(nums))
print(datas[::-1])
#print(datas[3: 6: -1]) -> 3부터 -1씩 6까지 갈 수 없음
print(datas[5:2:-1]) #'blue', 'green', 'red']
print(datas[::3]) #[10, 'red', 3.14]

