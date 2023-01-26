def convert_to_f(celcius_value):
    return celcius_value *9.0 / 5 + 32

def display():
    print(convert_to_f(40))
    print(convert_to_f(0))
    print(convert_to_f(-53))    

base = 24
if __name__ == '__main__':#어떤 모듈로부터 호출된거면 쓰지마
    print(__name__)#현재 main인지 아닌지를 보여줌

