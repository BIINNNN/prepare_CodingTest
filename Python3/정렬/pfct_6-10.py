#위에서 아래로
import sys
sys.stdin = open("D:\input.txt", "rt")

n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))
    
arr = sorted(arr, reverse=True)
for x in arr:
    print(x, end=' ')