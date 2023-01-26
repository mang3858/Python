#모둘명 fath_converter를 fah로 줄여 쓰고 싶을때 as 사용
#fath_converter부터 display를 가져와
#from fath_converter import display as fah
from fath_converter import display, convert_to_f
#from: 모듈명 생략가능 -> 직접 가져왔으니까

#print(fah.__name__)
print("Enter a celsius value: ", end="")
celsius = float(input())
#fahrenheit = fah.convert_to_f(celsius)
print(f"That's {fahrenheit} degrees Fahrenheit.")
#print("That's {} degrees Fahrenheit.".format(fahrenheit)))

#fath_converter모듈에 어떤 것이 있는지 확인
print(dir(fah))
#fath_converter모듈의 다른 함수 사용 
print(fah.base)
print(fah.display())
print(fah.display())
