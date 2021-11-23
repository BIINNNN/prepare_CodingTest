n = int(input())
conference = []

for _ in range(n):
    start, end = map(int, input().split())
    conference.append([start, end])

# 끝나는 시간 기준으로 오름차순 정렬을 먼저 해준 후, 
# 끝나는 시간이 같은 경우 시작 시간을 기준으로 정렬하도록 함
conference.sort(key=lambda x: (x[1],x[0])) 

last = 0 #마지막 회의 시간 저장 
count = 0 #회의 개수 카운트

for i, j in conference:
    #회의 시작 시간이 마지막 시간보다 크거나 같은 경우 더 늦게 시작하는 회의가 존재한다는 것
    if i >= last: 
        count += 1
        last = j #해당 타임의 회의 종료 시간을 마지막 시간으로 갱신
        
print(count)    