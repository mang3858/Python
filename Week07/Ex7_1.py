#dictionary 사용법
#비어있는 딕셔너리 생성
blankDict1 = dict()
blankDict2 = {}

#초기값이 있는 딕션너리
county_code = {"America":1, "Korea":82, "China":86, "Japan":81}

#딕셔너리에 원소 추가
county_code["German"] = 49

#blankDict1에 이름과 나이를 쌍으로 추가한다
blankDict1["전지현"] = 22
blankDict1["송은지"] = 23
blankDict1["박연하"] = 25

#딕셔너리 값 출력하기
print(county_code["Korea"])
print(county_code)
print(county_code.keys())
print(county_code.values())
print(county_code.items())
print(blankDict1)

#key를 한줄에 개별로 하나씩 출력하고 싶음(단체로 묶어서가 아니라)
for key in county_code.keys(): #county_code.keys(): county_code에서 key만 뽑아 리스트로 가지고 있는거
    print(key)

#value를 한줄에 개별로 하나씩 출력하고 싶음
#방법1
for value in county_code.values():
    print(value)
#방법2
for key in county_code.keys():
    print(county_code[key]) #특정 key에 해당하는 value를 찾아줘

#딕셔너리의 키와 값을 한 줄에 1개씩할 때 튜플 단위로 출력
for item in county_code.items():
    print(item) #튜플형태로 묶어서 한 줄에 한개씩 나옴

#튜플로 출력되는거 싫다 -> 언패킹하기
#딕셔너리의 키와 값을 한 줄에 1개씩할 때 개별 데이터로 출력
for k, v in county_code.items():
    print(k, "는", v)

#키가 딕셔너리에 있는지 확인 후 값 출력
for key in county_code.keys():
    if "Gana" == key:
        print(county_code["Gana"])
    else:
        print("없는 나라입니다")
    
#get()함수로 값 가져오기 -> return 값이 있음
print(county_code.get("China"))
print(county_code.get("Gana", "찾는 나라가 없음")) #-> 에러뜨지 않고 None으로 나옴

if "Gana" in county_code:
    print("참일 때")
else:
    print("거짓일 때")

if "Korea" in county_code:
    print("참일 때")
else:
    print("거짓일 때")

#딕셔너리 원소 삭제 : del 딕셔너리 명[키]
del county_code["Korea"]
print(county_code)
