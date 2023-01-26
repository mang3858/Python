'''
▪ 학교 포털 사이트에 로그인하려고 할 때 일어날 수 있는 경우에 적합한 메시지를 출력하는 프
로그램을 작성하시오.
▪ <조건> 로그인 아이디: admin, 비밀번호: pw1234'''

rogin = input("아이디 입력:")
pwd = input("비밀번호 입력:")

if rogin == 'admin' and pwd == 'pw1234':
    print("로그인 성공")
else:
    print("로그인 실패")
