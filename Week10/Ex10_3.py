#파일 입출력
#열기 - 읽기 - 쓰기 - 닫기
#예1) 읽기 : read()
import os

'''
if os.path.isfile("dream.txt") :#파일 유무 체크
    f = open("dream.txt", "r")
    contents = f.read() #전체를 읽어서 문자열로 반환
    print(contents)
    f.close()#안쓸거면 꼭 닫아줘야 함!'''
'''
#예2) 읽기 : readlines()
if os.path.isfile("dream.txt") :
    f = open("dream.txt", "r")
    contents = f.readlines() #파일을 읽어 리스트에 저장하기
    print(contents)
    print()
    
    for str1 in contents:
        str1 = str1.rstrip()#오른쪽에 있는 공백(줄바꿈 포함) 제거하기
        #str1 = str1.replace('\n', '') #줄바꿈을 공백으로 대체하라
        print(str1)
    f.close()
'''
'''
#예3) 읽기 : readline()
if os.path.isfile("dream.txt") :
    with open("dream.txt", "r") as f: #with문 쓰면 close()함수 쓰지 않아도 됨 
        i = 0
        while True:
            contents = f.readline() #한 줄씩 읽어서 문자열로 반환 
            if not contents: #데이터가 없으면 break로 빠져나가기
                break
           #contents = contents.rstrip()#오른쪽에 있는 엔터키를 제거하라
            contents = contents.replace('\n', '')#줄 바꿈 제거 
            print(i, "==", contents)
            i += 1
'''
#예4) dream.txt의 글자 수와 단어수, 줄 수 구하기
if os.path.isfile("dream.txt") :
    f = open("dream.txt", "r")
    contents = f.read()
    print(contents)

    #글자수
    print("글자 수 :", len(contents))

    #줄 수
    line_list = contents.split("\n")
    #print(line_list)
    print("줄 수 :", len(line_list))
    
    #단어수
    contents_1 = contents.replace("\n", " ") 
    word_list = contents_1.split(" ")
    print("단어 수: ", len(word_list))

    f.close()
    f = open("output.txt", "w", encoding="utf8")#메모장에서 한글 깨질 때 #encoding="cp949"
    f.write("글자 수 :" + str(len(contents)) + "\n")#write는 자동 줄바꿈 안됨
    f.write("줄 수 :" + str(len(line_list)) + "\n")
    f.write("단어 수: " + str(len(word_list)) + "\n")
    f.close()
