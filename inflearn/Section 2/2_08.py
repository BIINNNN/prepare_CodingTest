#뒤집은 소수

import sys
sys.stdin = open("D:\input.txt","rt")

n = int(input())
nums = list(map(int, input().split())) #n개의 자연수

#각 자연수를 뒤집는 함수
def reverse(x):
    rev_num = 0
    while x>0:
        t = x % 10
        rev_num = rev_num*10 + t
        x = x // 10
    return rev_num

#소수 판별 함수
def isPrime(x):
    if x == 1:
        return False
    # ex) 만약 16이 들어온 경우, 16의 약수는 1x16, 2x8, 4x4 이다.
    # 이때, 절반만 돌면 16의 절반인 8까지만 돌면 나머지 부분(8과 짝인 2, 16과 짝인 1) 은 이미 앞에서 계산한 숫자가 된다. 
    # 따라서 주어진 숫자의 절반만큼만 확인하면 소수인지 아닌지를 판변할 수 있다.
    for i in range(2, x//2+1):
        if x%i == 0:
            return False
    # 반복문이 종료되지 않도록 끝까지 정상적으로 수행된 숫자는 소수인 것
    else:
        return True

for num in nums:
    rev_num = reverse(num)
    if isPrime(rev_num):
        print(rev_num, end=' ')