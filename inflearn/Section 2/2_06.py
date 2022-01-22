#자릿수의 합 

import sys
sys.stdin = open("D:\input.txt","rt")

n = int(input()) #자연수 개수
a = list(map(int, input().split())) #각 자연수

#각 자연수의 자릿수의 합을 구하는 함수
def digit_sum(x):
    sum = 0
    # Sol 1) 10으로 나눠서 일의 자리부터 잘라내는 방법
    while x>0:
        sum += x%10
        x = x//10
    # Sol 2) str() 함수를 사용해서 각 자리를 먼저 나눠서 한 번에 계산
    # for i in str(x):
    #     sum += int(i)     
    return sum

max = -2147000000

for i in a: #각각의 자연수에서 각 자리수의 합 계산
    sum = digit_sum(i)
    if sum > max:
        max = sum
        result = i

print(result)