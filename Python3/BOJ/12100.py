#2048(easy) - 구현?(시뮬레이션)
n = int(input()) #보드의 크기
k = int(input()) #사과의 개수
board = [[0]*(n+1) for _ in range(n+1)] #보드 1~n까지
for _ in range(k):
    a, b = map(int, input().split())
    board[a][b] = 1 #사과가 있는 칸은 1로 지정
l = int(input()) #회전 횟수
info = [] #회전 정보 담을 리스트(초, 방향 같이 들어옴)
for _ in range(l):
    x, c = input().split() #정수x와 문자 c (각각 회전을 해야하는 시간과 회전할 방향)
    info.append((int(x), c))

# 0:동, 1: 남, 2: 서, 3:북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == 'L':
        direction = (direction-1)%4 #dx, dy의 길이 범위 안에서 돌고 돌아야 함
    elif c == 'D':
        direction = (direction+1)%4
    return direction

def simulate():
    x, y = 1,1 #뱀의 머리 위치(초기 위치)
    board[x][y]=2 #뱀이 존재하는 위치는 2로 지정
    direction = 0 #뱀이 바라보고 있는 방향 (처음 시작이 동쪽을 바라보고 있음)
    time = 0 #하나의 턴이 끝날때마다 시간 1씩 증가함
    index = 0 #다음에 회전할 정보(몇 번 회전하는지 카운트해서 l의 개수만큼 반복하도록 해야함)

    q = [(x,y)] #뱀이 차지하는 위치 정보(꼬리가 앞) => 꼬리 유지하거나 꼬리 자르기 위해 필요
    while True:
        nx = x+dx[direction]
        ny = y+dy[direction]

        #이동할 다음 위치가 맵의 범위 안에 있고, 몸통과 부딪히지 않는 위치라면
        if 1 <= nx <=n and 1 <= ny <= n and board[nx][ny]!=2:
            #사과가 없다면 한 칸 이동 후 꼬리 자름
            if board[nx][ny] == 0:
                board[nx][ny]=2 #해당 위치에 뱀이 자리하게 됨
                q.append((nx, ny)) #뱀이 차지하고 있음을 표시
                px, py = q.pop(0)
                board[px][py] = 0 #꼬리가 위치했던 칸을 비워줌
            #사과가 있다면 이동한 후 꼬리 유지
            elif board[nx][ny] == 1:
                board[nx][ny]=2
                q.append((nx, ny))
        else: #벽에 부딪히거나 몸통에 부딪히면
            time+=1
            break #종료
        x, y = nx, ny  # 다음 위치로 머리 이동
        time+=1
        #만약 회전할 시간이라면 회전
        if index < l and time == info[index][0]: #회전할 시간인 경우
            direction = turn(direction, info[index][1])
            index +=1
    return time #결국 구하는 것은 몇 초 후에 종료인지

print(simulate())
