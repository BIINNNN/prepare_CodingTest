# 감시 피하기
from itertools import combinations

n = int(input()) # 복도의 크기
board = [] # 복도(N x N)
teachers = [] # 선생님 위치 정보
empty = [] # 장애물 설치할 조합 구하기 위해 필요한 빈 공간 정보

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        # 선생님 위치 저장
        if board[i][j] == 'T':
            teachers.append((i, j)) 
        # 장애물 설치가 가능한 빈 공간 위치 저장
        if board[i][j] == 'X':
            empty.append((i, j))

# 학생 감시를 진행하는 함수. (학생이 보이면 True, 안보이면 False)        
def watch(x, y, direction):
    # 상
    if direction == 0: 
        # 위쪽 벽에 부딪히기 전까지 반복
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1
        
    # 하
    if direction == 1:
        # 아래쪽 벽에 부딪히기 전까지 반복
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x += 1
            
    # 좌
    if direction == 2:
        # 왼쪽 벽에 부딪히기 전까지 반복
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y -= 1
             
    # 우
    if direction == 3:
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1
    return False


# 학생이 감지되는지 확인        
def show():
    for x, y in teachers:
        for i in range(4): # 상하좌우 확인
            if watch(x, y, i):
                return True
    return False    
            
find = False 

for comb in combinations(empty, 3): # 빈 공간 중 3개씩 조합 만들어 가면서 확인
    for x, y in comb:
        board[x][y] = 'O' # 장애물 설치
        
    # 학생 보이지 않으면
    if not show():
        find = True
        break
    # 다른 경우 확인을 위해 설치한 장애물 없애고 리셋
    for x, y in comb:
        board[x][y] = 'X'
        
if find:
    print('YES')
else:
    print('NO')