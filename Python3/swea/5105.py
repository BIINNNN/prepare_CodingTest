from collections import deque

import sys
sys.stdin = open("sample/input_5105.txt", "r")

T = int(input())



def bfs(start_x, start_y, end_x, end_y):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    queue = deque() #현재 방문중인 큐 삽입
    queue.append((start_x,start_y))

    #큐에 자료가 없을때까지 반복
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True  #방문 처리

        for i in range(0, 4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if maze[nx][ny] == 0:
                    queue.append((nx, ny))
                    distance[nx][ny] = distance[x][y] + 1  # 다음 위치의 시작점으로부터의 거리는 현재보다 1 큼
                elif maze[nx][ny] == 3:
                    distance[nx][ny] = distance[x][y]

    return distance[end_x][end_y]

for test_case in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)] #미로
    visited = [[False]*N for _ in range(N)] #방문 여부 확인 리스트
    distance = [[0]*N for _ in range(N)] #거리 저장 리스트

    start_x = start_y = end_x = end_y = 0

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_x, start_y = i, j
            elif maze[i][j] == 3:
                end_x, end_y = i, j

    result = bfs(start_x, start_y, end_x, end_y)
    print("#{} {}".format(test_case,result))