n = int(input())

candies = [list(input()) for _ in range(n)]
max_eat = 1

# 먹을 수 있는 최대 사탕 개수 구하는 함수
def count():
    global max_eat
    # 가로 탐색
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if candies[i][j] == candies[i][j+1]:
                cnt += 1
                if cnt >= max_eat:
                    max_eat = cnt
            else:
                cnt = 1
    
    # 세로 탐색
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if candies[j][i] == candies[j+1][i]:
                cnt += 1
                if cnt >= max_eat:
                    max_eat = cnt
            else:
                cnt = 1

# 가로 뒤집기
for i in range(n):
    for j in range(n-1):
        candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]
        count()
        candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]
        
#세로 뒤집기
for i in range(n):
    for j in range(n-1):
        candies[j][i], candies[j+1][i] = candies[j+1][i], candies[j][i]
        count()
        candies[j][i], candies[j+1][i] = candies[j+1][i], candies[j][i]
        
print(max_eat)