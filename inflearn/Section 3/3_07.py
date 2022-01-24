# 사과나무

import sys
sys.stdin = open("D:\input.txt","rt")

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

s = e = n//2
res = 0

for i in range(n):
    for j in range(s, e+1):
        res += board[i][j]
    if i < n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

print(res)