import sys
sys.stdin=open("D:\input.txt", "rt")

T = int(input())

for t in range(T): #테스트 케이스 개수만큼 반복하면서 각 케이스별로 테스트
    n, s, e, k = map(int, input().split())
    
    a = list(map(int, input().split()))
    a = a[s-1:e]
    a.sort()
    print("#{} {}".format(t+1, a[k-1]))