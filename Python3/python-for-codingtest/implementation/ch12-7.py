from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    city = list(map(int, input().split()))
    for c in range(n):
        if city[c] == 2:
            chicken.append((r, c)) # 집
        if city[c] == 1:
            house.append((r, c)) # 치킨집

chooses = list(combinations(chicken, m))

def get_sum(choose):
    result = 0
    for hx, hy in house:
        temp = 100000
        for cx, cy in choose:
            temp = min(temp, abs(hx-cx)+abs(hy-cy))
            
        result += temp
        
    return result

result = 100000
for choose in chooses:
    result = min(result, get_sum(choose))
    
print(result)
            