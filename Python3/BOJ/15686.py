from itertools import combinations
#import sys
#sys.stdin = open("sample/input_15686.txt", "r")

n, m = map(int, input().split()) #도시의 크기 n, 선택할 치킨집 개수
city = [list(map(int, input().split())) for _ in range(n)]
house, chicken = [], [] #집과 치킨집이 위치한 곳의 r, c 인덱스를 저장할 리스트

for r in range(n):
    for c in range(n):
        if city[r][c] == 1:
            house.append((r,c)) #집 위치
        elif city[r][c] == 2:
            chicken.append((r,c)) #치킨집 위치

#모든 치킨집 중에서 m개의 치킨집을 뽑는 조합을 계산
candidates = list(combinations(chicken, m)) #치킨집개수Cm

#치킨 거리를 계산
def get_sum(candidates):
    result = 0
    #모든 집에 대해 계산함
    for hr, hc in house:
        #가장 가까운 집을 찾음
        temp = 100
        for cr, cc in candidates:
            temp = min(temp, abs(hr-cr)+abs(hc-cc))
        #가장 가까운 치킨집 까지의 거리를 더함
        result += temp

    return result

#치킨거리의 최소값을 찾아서 출력하게 됨
result = 10000
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)