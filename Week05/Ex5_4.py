#5개의 양의 정수를 가지고 있는 리스트를 매개변수로 전달받아,
#리스트의 원소 중 짝수의 수를 세어서 출력하시오.

def get_even(nums):
    even_cnt = 0
    odd_cnt = 0
    for i in nums:
        if i % 2 == 0:
            even_cnt +=1
        else:
            odd_cnt += 1
    return even_cnt, odd_cnt
    
nums = [4, 30, 15, 28, 5]
cnt1, cnt2 = get_even(nums)
print("짝수의 개수는 %d이다" %cnt1)
print("홀수의 개수는 %d이다" %cnt2)
