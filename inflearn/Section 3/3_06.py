#격자판 최대합
import sys
sys.stdin = open("D:\input.txt","rt")

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

max = -2147000000

# 각 행/열의 합
for i in range(n):
    sum1 = sum2=0
    for j in range(n):
        sum1 += arr[i][j]
        sum2 += arr[j][i]
    if sum1 > max:
        max = sum1
    if sum2 > max:
        max = sum2

sum1 = sum2 = 0          
# 두 대각선
for i in range(n):    
    sum1 += arr[i][i]
    sum2 += arr[i][n-i-1]
    if sum1 > max:
        max = sum1
    if sum2 > max:
        max = sum2
            
print(max)