#랜선자르기(결정 알고리즘)
import sys
#sys.stdin = open("C:/Users/seobi/Desktop/input.txt","rt")

k, n = map(int, input().split())
line = []
res = 0

def Count(len):
    cnt = 0
    for x in line:
        cnt += (x//len) # 가능한 토막의 개수
    return cnt

for i in range(k):
    tmp = int(input())
    line.append(tmp)
    
lt = 1
rt = max(line)

while lt<=rt:
    mid = (lt+rt)//2
    if Count(mid) >= n:
        res = mid
        lt = mid + 1 # 더 나은 경우가 있는지 최적의 경우 찾아감
    else: #개수가 부족한 경우 해당 길이가 너무 긴 것. 따라서 해당 경우보다 짧은 길이 필요(-1)
        rt = mid - 1

print(res)