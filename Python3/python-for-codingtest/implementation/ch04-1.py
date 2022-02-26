n = int(input())
moves = input().split()

x, y = 1, 1 # 시작 좌표는 항상 (1, 1)

# L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, -1, 0]
move_types = ['L', 'R', 'U', 'D']

for move in moves:
    for i in range(len(move_types)):
        if move == move_types[i]:
            nx = x+dx[i]
            ny = y+dy[i]
            
    if nx < 1 or ny < 1 or nx > n or ny >n:
        continue
    
    x, y = nx, ny
    
print(x, y)        