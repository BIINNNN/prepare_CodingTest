#주사위 게임

import sys
sys.stdin = open("D:\input.txt","rt")

n = int(input())
moneys = []

for i in range(n):
    dice = input().split()
    dice.sort(reverse=True)
    a, b, c = map(int, dice)
    if a == b and b == c: #세 개 모두 같은 경우
        money = 10000+a*1000
        moneys.append(money)
    # 두 개만 같은 경우 (계산 편하기 위해 a와 어떤 한 숫자가 같은 경우와 그렇지 않은 경우 나눠서 계산)    
    elif a==b or a==c:
        money = 1000+a*100
        moneys.append(money)
    elif b==c:
        money = 1000+b*100
        moneys.append(money)
    #셋 다 다른 경우
    else:
        money = a*100
        moneys.append(money)

print(max(moneys))