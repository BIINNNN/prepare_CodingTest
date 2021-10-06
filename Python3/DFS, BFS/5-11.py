from collections import deque

#공백 구분해서 입력
n, m = map(int, input().split())
#2차원 리스트 맵 입력
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

#미로에서 이동할 방향 설정 위한 dx, dy => (-1,0),(1,0),(0,-1),(0,1)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    #큐가 빌때까지 반복
    while queue:
        #방문한 위치는 큐에서 없앰
        x, y = queue.popleft()
        #현재 위치에서 사방 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #미로를 벗어난 위치이면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            #괴물이 있는 부분이면 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]

#동빈이의 위치는 (1,1)이므로 queue 배열상에서는 (0,0)
print(bfs(0, 0))