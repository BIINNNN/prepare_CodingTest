import math

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))
    
    # 두 원의 중심 사이의 거리
    distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    
    if distance == 0:    # 두 원의 중심이 같을 때
        if r1 == r2: # 두 원의 크기가 같다면
            print(-1)
        else:                  
            print(0)
    else:            # 두 원의 중심이 다를 때
        if (r1 + r2) == distance or abs(r2 - r1) == distance:
            print(1)
        elif ((abs(r1 - r2) < distance) and (distance < r1 + r2)):
            print(2)
        else:
            print(0)