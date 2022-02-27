n, m = map(int, input().split())

d = [[0]*m for _ in range(n)]

x, y, dir = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문처리(방문: 1, 미방문:0)

arr = []
# 전체 맵 정보 입력
for _ in range(n):
    arr.append(list(map(int, input().split())))

# 북, 동, 남, 서 
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽 회전
def turn_left():
    global dir
    dir -= 1
    if dir == -1:
        dir = 3

# 시뮬레이션 시작        
cnt = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[dir]
    ny = y + dy[dir]
    # 회전 이후 정면으로 가보지 않은 칸이 있는 경우
    if d[nx][ny] ==0 and arr[nx][ny]==0:
        # 이동
        d[nx][ny] = 1
        # 현재 위치 갱신
        x = nx
        y = ny
        cnt += 1
        turn_time = 0
        continue
    
    # 회전 이후 정면으로 가보지 않은 칸이 없거나 바다라면
    else:
        turn_time += 1
    
    # 사방 모두 이동 불가인 경우
    if turn_time == 4:
        nx = x - dx[dir]
        ny = y - dy[dir]
        # 뒤로 이동 가능하다면
        if arr[nx][ny] == 0:
            # 이동 후 현재 위치 갱신
            x = nx
            y = ny
        
        # 뒤가 바다라 이동하지 못하는 경우
        else:
            break
        turn_time = 0
        
print(cnt)