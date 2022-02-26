# 왕실의 나이트
location = input() #str
row = int(location[1])
col = int(ord(location[0])-int(ord('a')))+1

moves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

count = 0

for move in moves:
    next_row = row+move[0]
    nex_col = col+move[1]
    
    if next_row >= 1 and next_row <= 9 and nex_col >= 1 and nex_col <= 8:
        count += 1
        
print(count)