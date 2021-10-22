#import sys
#sys.stdin = open("sample/input_14502.txt", "r")

#python3로는 시간초과되고, pypy3으로 실행해야 성공 (나중에 python3로 통과되도록다시 해봐야갰다...)

n, m = map(int, input().split()) #n: 세로 m: 가로
place = [list(map(int, input().split())) for _ in range(n)]

place_after = [[0]*m for _ in range(n)] #벽 3개 설치하고 나서의 연구실

#상하좌우 이동을 위한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0
#바이러스 사방에 퍼지도록
def virus(x, y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<= nx < n and 0<=ny<m:
            if place_after[nx][ny] ==0:
                place_after[nx][ny]=2
                virus(nx, ny)

#안전영역 크기 계산
def get_safezone():
    count = 0 #안전영역의 개수
    for i in range(n):
        for j in range(m):
            if place_after[i][j]==0:
                count+=1 #바이러스가 퍼지지 않은 곳 = 빈 곳 = 0인곳이면 안전 영역
    return count

def dfs(wall):
    global result
    if wall ==3:
        for i in range(n):
            for j in range(m):
                place_after[i][j] = place[i][j]
        #각 위치에서 바이러스의 전파 진행(바이러스 전파는 벽 세운 후)
        for i in range(n):
            for j in range(m):
                if place_after[i][j]==2: #바이러스가 있는 위치면
                    virus(i, j) #전파
        #안전 영역의 최댓값 계산
        result = max(result, get_safezone())
        return result

    #벽 개수 3개 아니면 빈 공간에 벽 설치
    for i in range(n):
        for j in range(m):
            if place[i][j] ==0:
                place[i][j] = 1
                wall += 1
                dfs(wall)
                place[i][j] = 0
                wall -= 1
dfs(0)
print(result)
