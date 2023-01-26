#함수(): append(), extend(), insert(), remove(), del
scores = [] #공백 리스트
colors = list() #공백 리스트
nums=[None] * 5 #5개의 원소를 갖는 빈 리스트 만들기
print(scores)
print(colors)
print(nums)

#리스트의 길이 구하기
print(len(scores))
print(len(nums))

#리스트 클래스에서 제공하는 함수(메소드)
#append(), extend(), insert(), remove()
scores.append(100)
scores.append(200)
scores.append(300)
scores.append(400)
scores.append(500)
print(len(scores))
print(scores)
#append()는 끝자리에 붙여줌
#insert()는 원하는 위치를 정해서 그자리에 데이터 삽입

#인덱스번호 0번째 자리에 30을 삽입하시오.
scores.insert(0, 30)
print(scores)

#colors의 'black', 'white' 추가하기
colors.append('black')
colors.append('white')

#'red', 'green', 'blue'를 colors리스트에 추가하기
colors.extend(['red', 'green', 'blue'])
print(colors)

#colors 리스트에서 'white' 삭제하기
colors.remove('white')

#colors의 0번째 인덱스를 삭제하라
del colors[0]
print(colors)

# colors.remove('navy') -> 에러 발생
