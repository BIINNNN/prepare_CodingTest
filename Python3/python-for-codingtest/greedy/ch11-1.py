n = int(input())
fear = list(map(int, input().split()))
fear.sort()

result = 0 #총 그룹 수
cnt = 0 #현 그룹에 포함된 모험가 수

for i in fear:
    cnt += 1
    if cnt >= i:
        result += 1
        cnt = 0 #초기화
        
print(result)   