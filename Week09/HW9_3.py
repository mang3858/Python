#questions리스트와 answers리스트를 zip()함수를 이용하여 다음과 같은 결과가 나오도록 프로그램하시오.

questions = ['name', 'dream', 'color']
answers = ['홍길동', '행복', '노랑']

for q, a in zip(questions, answers):
    print("what is your %s? It is %s" %(q, a))
