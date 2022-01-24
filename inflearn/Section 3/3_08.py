# 곳감(모래시계)

import sys
sys.stdin = open("D:\input.txt","rt")

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

#회전
for _ in range(m):
    line, dir, num = map(int, input().split())
    if dir == 0:
        for _ in range(num):
            board[line-1].append(board[line-1].pop(0))
    else:
        for _ in range(num):
            board[line-1].insert(0, board[line-1].pop())

res = 0
s = 0
e = n-1

for i in range(n):
    for j in range(s, e+1):
        res += board[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(res)            