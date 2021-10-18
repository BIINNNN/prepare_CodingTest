import sys
sys.stdin = open("sample/input_4875.txt","r")

T = int(input())

def find(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

def dfs(x, y):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    global result

    for i in range(0, 4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] : #미로의 벽을 벗어나지 않음
            visited[nx][ny] = True #방문 여부 갱신
            if maze[nx][ny] == 3:
                result = True
            elif maze[nx][ny] == 0:
                dfs(nx, ny)


for test_case in range(1, T+1):
    N = int(input())

    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[False for _ in range(N)]for _ in range(N)]
    result = False
    start_x, start_y = find(N)

    dfs(start_x, start_y)
    if result:
        print("#{} 1".format(test_case))
    else:
        print("#{} 0".format(test_case))
