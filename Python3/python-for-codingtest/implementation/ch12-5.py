# 뱀
n = int(input()) # 보드 크기
k = int(input()) # 사과 개수
board = [[0]*(n+1) for _ in range(n+1)] # 맵 정보를 입력 받을 2차원 리스트 (1행 1열부터 시작하기 때문에 1부터 시작해서 N까지의 맵을 만들기 위해 n+1의 리스트 만들어 줌)

for _ in range(k): #사과의 위치 표시
    a, b = map(int, input().split())
    board[a][b] = 1
    
l = int(input()) # 방향 변환 횟수
info = [] # 방향 회전 정보
for _ in range(l):
    x, c = input().split() # x는 숫자(방향 변환되는 시기), c는 전환 방향
    info.append((int(x), c)) # ㅌㅠ플 형태로 리스트에 회전 방향 정보 저장

# 초기엔 동쪽(오른쪽) 보고 있음 = 초기는 오른쪽으로 증가
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == 'L':
        direction = (direction-1) % 4
    else:
        direction = (direction+1) % 4
    return direction
        
def simulate():
    x, y = 1, 1 # 뱀의 처음 위치
    board[x][y] = 2 #사과 위치가 이미 1로 되어있기때문에 뱀의 위치는 2로 표시
    time = 0 # 초 카운트
    direction = 0 # 처음은 동쪽
    q = [(x, y)] # 뱀이 차지하고 있는 위치 정보(이동하면서 머리 위치가 새롭게 붙으므로 꼬리가 앞, 머리가 뒤)
    
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치
        if 1 <= nx and nx <= n and 1<= ny and ny <= n and board[nx][ny] != 2:
            # 사과 없으면 이동 후 꼬리 제거(길이 유지)
            if board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                board[px][py] = 0
            
            # 사과 있으면 이동 후 꼬리는 원래 있던 위치에 두기 (길이 늘어남)
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                q.append((nx, ny))
            
        # 맵을 벗어나거나 몸통이 있는 위치에 부딪히면
        else:
            time += 1
            break
        
        time += 1
        x, y = nx, ny # 다음 위치로 머리 이동
        
        index = 0
        if index < l and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1
        
    return time

print(simulate())