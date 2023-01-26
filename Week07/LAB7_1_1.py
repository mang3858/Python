#사용자로부터 암호를 입력받고 프로그램에서 암호가 맞는지 체크하는 프로그램

userid = input("아이디를 입력하시오: ")
password = input("암호를 입력하시오: ")

while userid != "guest" or password != "pythonisfun":
    print()
    userid = input("아이디를 입력하시오: ")
    password = input("암호를 입력하시오: ")
print("로그인 성공")
