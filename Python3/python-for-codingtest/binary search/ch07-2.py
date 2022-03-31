# 떡볶이 떡 만들기
n, m = map(int, input().split())
length = list(map(int, input().split())) # 떡의 길이

start = 0
end = max(length)

result = 0
while start <= end:
    mid = (start+end)//2
    total = 0
    
    for x in length:
        if x > mid:
            total += x-mid
            
    if total < m:
        end = mid -1
    else:
        start = mid + 1
        result = mid
            
print(result)