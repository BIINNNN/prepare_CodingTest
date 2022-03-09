n, m = map(int, input().split())

room = [] # 초기 입력받은 맵
room_after = [[0]*m for _ in range(n)] # 벽 설치 후 맵

for _ in range(n):
    room.append(list(map(int, input().split())))
    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

EMPTY = 0
WALL = 1
VIRUS = 2

# 바이러스 전파 함수
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 바이러스 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if room_after[nx][ny] == EMPTY:
                room_after[nx][ny] = VIRUS
                virus(nx, ny) # 재귀적으로 사용해서 퍼질 수 있을 때까지 퍼지도록.
        
# 안전 영역 계산 함수          
def safe_zone():
    safe = 0
    for i in range(n):
        for j in range(m):
            if room_after[i][j] == EMPTY:
                safe += 1
    return safe

result = 0

# 메인
def dfs(wall):
    global result
    
    if wall == 3:
        for i in range(n):
            for j in range(m):
                room_after[i][j] = room[i][j]
                
        for i in range(n):
            for j in range(m):
                if room_after[i][j] == VIRUS:
                    virus(i, j) 
        
        result = max(result, safe_zone())
        return
    
    # 벽 설치
    for i in range(n):
        for j in range(m):
            if room[i][j] == EMPTY:
                room[i][j] = WALL
                wall += 1
                dfs(wall)
                room[i][j] = EMPTY
                wall -= 1
                
dfs(0)
print(result)