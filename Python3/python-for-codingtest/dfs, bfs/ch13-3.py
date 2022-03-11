# 경쟁적 전염
from collections import deque

n, k = map(int, input().split())

board = [] # 시험관 정보
virus_inform = [] # 바이러스에 대한 정보 저장

for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(n):
        if board[i][j] != 0: # 해당 위치에 바이러스가 있다면
            # 바이러스 종류, 0초(증식 시작 전이므로), 바이러스가 존재하는 x축 위치, 바이러스가 존재하는 y축 위치
            virus_inform.append((board[i][j], 0, i, j)) # 하나의 바이러스에 대해 튜플 형식으로 묶어서 저장

# 낮은 번호부터 증식하도록 하기 위해 정렬해서 큐로 옮기기
virus_inform.sort()
q = deque(virus_inform)

target_s, target_x, target_y = map(int, input().split())

# 상, 하, 좌, 우 증식
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 수행 (퍼져나가는 것은 가까운 곳부터 -> 너비우선 탐색)
while q:
    virus, s, x, y = q.popleft()
    
    if s == target_s:
        break # 주어진 시간이 지나면 종료
    
    # 증식
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            if board[nx][ny] == 0:
                board[nx][ny] = virus
                q.append((virus, s+1, nx, ny))

print(board[target_x-1][target_y-1]) # 입력되는 목표 위치는 시험관 x, y 번호가 (1,1)부터 시작된다고 가정하지만, 실제 코드에서는 리스트를 사용해서 (0,0) 부터 시작됨. (ex. 입력받은 x, y 위치가 (2, 3)이라면 리스트 상 위치는 (1, 2))