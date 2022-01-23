#카드 역배치(정올 기출)
import sys
sys.stdin = open("D:\input.txt", "rt")

arr = [i for i in range(21)]

for _ in range(10): #10개의 구간이 주어진다고 문제아 나와 있음
    ai, bi = map(int, input().split())
    for i in range((bi-ai+1)//2):
        arr[ai+i], arr[bi-i] = arr[bi-i], arr[ai+i]
arr.pop(0)

for x in arr:
    print(x, end=' ')