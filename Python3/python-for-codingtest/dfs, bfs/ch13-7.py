# 인구 이동
# PyPy3로 실행해야 시간초과 안 뜸.. Python으로 실행하니까 80~81% 쯤 시간초과로 실패
from collections import deque

n, l, r = map(int, input().split())

# 전체 나라 정보 입력
world = []
for _ in range(n):
    world.append(list(map(int, input().split())))
    
# 상, 하, 좌, 우 연합 가능 여부 확인 위한 x, y 이동 리스트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0 # 이동 횟수 저장 

# 특정 국가에서 출발해서 주변국과 국경선 개방 가능한지(연합 가능한지) 확인
def moves(x, y, idx):
    # 현재 위치의 나라와 연결된 연합국 정보(위치) 담을 리스트
    united = []
    united.append((x, y))
    
    q = deque()
    q.append((x, y))
    
    # 현재 연합의 번호를 할당하도록 함.
    union[x][y] = idx
    summary = world[x][y] # 현재 연합의 전체 인구 수
    cnt = 1 # 현재 연합 국가 수
    
    # BFS
    while q:
        x, y = q.popleft()
        # 상하좌우 연합 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                # 문제에서 주어진 조건 만족할 때 국경선 개방
                if l <= abs(world[nx][ny]- world[x][y]) <= r:
                    q.append((nx, ny))
                    # 연합 추가
                    union[nx][ny] = idx
                    summary += world[nx][ny]
                    cnt += 1
                    united.append((nx, ny))
    # 인구 분배
    for i, j in united:
        world[i][j] = summary // cnt
    

# 더 이상 이동 불가한 순간까지 이동 반복
while True:
    union = [[-1]*n for _ in range(n)] 
    idx = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1: # 아직 처리 전이라면
                moves(i, j, idx)
                idx += 1
    if idx == n*n: # 모든 이동 끝난 후,
        break
    result += 1
    
print(result)