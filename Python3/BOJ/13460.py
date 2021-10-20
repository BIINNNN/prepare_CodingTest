#구슬 탈출 2 => 최소 몇 번 => bfs
from collections import deque

import sys
sys.stdin = open("sample/input_13460.txt", "r")

#기울일 때
def move(x, y, dx, dy):
    count = 0
    # 한칸씩 움직이는 것이 아니라 벽에 부딪히기 전까지 이동해야 함
    # 구멍을 만나면 종료되어야 함
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1 #움직인 거리
    return x, y, count

def bfs(rx, ry, bx, by):
    queue = deque()
    queue.append((rx,ry, bx, by, 1))
    visited[rx][ry][bx][by] = True
    dxy = [(-1, 0),(1,0),(0,1),(0,-1)]

    while queue:
        rx, ry, bx, by, depth = queue.popleft()
        if depth > 10: #10번 이내 성공 못하면 -1 출력
            break
        for dx, dy in dxy:
            nrx, nry, red_count = move(rx, ry, dx, dy)
            nbx, nby, blue_count = move(bx, by, dx, dy)

            if board[nbx][nby] != 'O': #파란공이 구멍에 빠지지 않을 때
                if board[nrx][nry] == 'O': #빨간공이 구멍에 빠지는 경우
                    return depth #이동한 횟수 리턴
                if nrx == nbx and nry == nby: #빨간공과 파란공이 같은 위치에 가게 되는 경우
                    if red_count > blue_count:
                        nrx -= dx
                        nry -= dy
                    else:
                        nbx -= dx
                        nby -= dy
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    queue.append((nrx, nry, nbx, nby, depth+1))
    return -1 #빠져나오지 못할 경우


N, M = map(int, input().split()) #N : 보드의 가로 크기 / M : 보드의 세로 크기
board = [list(input().strip()) for _ in range(N)] #입력 보드
visited = [[[[False]*M for _ in range(N)]for _ in range(M)]for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R': #빨간공이 있는 위치는 공이 지나다닐 수 있는 루트임
            board[i][j] = '.'
            rx, ry = i, j #빨간공 위치 저장
        elif board[i][j] == 'B':
            board[i][j] = '.'
            bx, by = i, j #파란공 위치 저장

result = bfs(rx, ry, bx, by)

print(result)




