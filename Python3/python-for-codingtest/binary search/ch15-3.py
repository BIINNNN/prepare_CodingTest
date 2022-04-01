import sys

n, c =  list(map(int, input().split(' ')))

arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
arr.sort()

start = 1 # 가능한 최소 거리(min gap)
end = arr[-1]-arr[0] # 가능한 최대 거리(max gap)

result = 0

while (start <= end):
    mid = (start+end)//2
    install = arr[0] # 첫 공유기 설치는 첫 번째 좌표 위치의 집에 설치
    count = 1
    
    # 현재 mid 값 이용해서 공유기 설치
    for i in range(1, n):
        if arr[i] >= install+mid:
            install = arr[i]
            count += 1
            
    if count >= c: # C개 이상의 공유기가 설치 가능한 경우
        start = mid+1
        result = mid # 현재 mid 값이 해당 루프의 최적의 경우
    else:
        end = mid - 1
                 
print(result)