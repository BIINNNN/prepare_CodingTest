import sys
sys.stdin = open("sample/input_5188.txt", "r")

T = int(input())

def search_sum(x, y, sum):
    dx = [1,0]
    dy = [0,1]
    global min_sum

    sum = sum + field[x][y]
    if y == N-1 and x == N-1: #오른쪽 마지막 칸에 도달했다면
        if min_sum > sum:
            min_sum = sum
        return
    elif min_sum < sum:
        return

    for i in range(0,2):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < N and ny < N:
            search_sum(nx, ny, sum)

for test_case in range(1, T+1):
    N = int(input()) #맵의 크기
    field = [list(map(int, input().split())) for _ in range(N)] #N의 행을 갖는 맵 생성

    min_sum = 260

    search_sum(0, 0, 0) #x, y 위치, 합계

    print("#{} {}".format(test_case, min_sum))