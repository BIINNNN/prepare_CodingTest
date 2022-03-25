# 블록 이동하기

from collections import deque

def get_next_loc(loc, board):
    next_loc = [] # 반환해줄 이동 가능한 위치에 대한 정보
    loc = list(loc) # 튜플 형태의 현재 위치 정보를 리스트 형태로 바꿈
    loc1_x, loc1_y, loc2_x, loc2_y = loc[0][0], loc[0][1], loc[1][0], loc[1][1]
    
    # 상, 하, 좌, 우 
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(4):
        loc1_next_x, loc1_next_y, loc2_next_x, loc2_next_y = loc1_x + dx[i], loc1_y + dy[i], loc2_x + dx[i], loc2_y + dy[i]
        # 이동하려는 두 칸이 모두 이동 가능한 칸이라면 (벽이 아니라면)
        if board[loc1_next_x][loc1_next_y] == 0 and board[loc2_next_x][loc2_next_y] == 0:
            next_loc.append({(loc1_next_x, loc1_next_y),(loc2_next_x, loc2_next_y)})
        
    # 로봇이 가로로 놓여진 경우
    if loc1_x == loc2_x:
        #위, 아래로 회전 가능
        for i in [-1, 1]:
            # 위 혹은 아래쪽 두 칸이 모두 비어있다면
            if board[loc1_x+i][loc1_y] == 0 and board[loc2_x+i][loc2_y] == 0:
                next_loc.append({(loc1_x, loc1_y),(loc1_x+i, loc1_y)})
                next_loc.append({(loc2_x, loc2_y),(loc2_x+i, loc2_y)})
    # 로봇이 세로로 놓여진 경우
    elif loc1_y == loc2_y:
       # 좌우로 회전 가능
        for i in [-1, 1]:
            # 위 혹은 아래쪽 두 칸이 모두 비어있다면
            if board[loc1_x][loc1_y+i] == 0 and board[loc2_x][loc2_y+i] == 0:
                next_loc.append({(loc1_x, loc1_y),(loc1_x, loc1_y+i)})
                next_loc.append({(loc2_x, loc2_y),(loc2_x, loc2_y+i)}) 
                
    return next_loc

def solution(board):
    n = len(board)
    # 맵의 외곽에 벽을 두어서 맵을 벗어나지 않는지 간단히 확인
    new_board = [[1]*(n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]
            
    q = deque()
    visited = []
    loc = {(1,1), (1,2)} # 시작 위치
    q.append((loc, 0)) 
    visited.append(loc) # 방문처리
    
    # 큐 빌 때까지 반복
    while q:
        loc, dis = q.popleft()
        #(n,n)에 도달하면 반환
        if (n,n) in loc:
            return dis
        # 현재 위치에서 이동 가능한 위치 확인
        for next_loc in get_next_loc(loc, new_board):
            if next_loc not in visited:
                q.append((next_loc, dis+1))
                visited.append(next_loc)

    return 0