import sys
sys.stdin=open("D:\input.txt", "rt")

n, k = map(int, input().split())
cnt = 0

for i in range(1, n+1):
    if n%i == 0:
        cnt+=1
    if cnt == k: #k번째 약수가 카운트되면 == 발견되면
        print(i)
        break #k번째 약수가 발견되면 for문 종료해도 됨
else: #약수 발견하지 못해서 break문에 걸리지 못한 경우
    print(-1)
        