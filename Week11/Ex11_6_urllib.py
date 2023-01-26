import urllib.request

url = "https://www.google.com"

response = urllib.request.urlopen(url)
print(response.status) #200이면 정상응답
encoding = response.info().get_content_charset(failobj="utf-8")
#contents = response.read()
contents = response.read().decode(encoding)
print(contents)

f = open("output1.html", "w")
f.write(str(contents))
f.close()


'''
f = open("output1.html", "w") #깨짐 
f.write(str(contents))
f.close()
'''
