import sys
from collections import deque
sys.stdin = open("sample/input_5247.txt", "r")

T = int(input())

def bfs():
    global result
    while Q: #큐가 비는 순간 종료
        #node = N (계산 결과로 나온 값이 다음 노드가 됨), count = 0
        node, count = Q.popleft() #먼저 들어온 큐의 원소부터 확인
        if node == M: #목표했던 결과값이 나오면
            result = count
            return #함수 종료

        for i in range(4):
            if i == 0:
                if 1 <= node + 1 <= 1000000 and visited[node + 1] == False:
                    Q.append((node + 1, count + 1))
                    visited[node + 1] = True
            elif i == 1:
                if 1 <= node - 1 <= 1000000 and visited[node - 1] == False:
                    Q.append((node - 1, count + 1))
                    visited[node - 1] = True
            elif i == 2:
                if 1 <= node * 2 <= 1000000 and visited[node * 2] == False:
                    Q.append((node * 2, count + 1))
                    visited[node * 2] = True
            elif i == 3:
                if 1 <= node - 10 <= 1000000 and visited[node - 10] == False:
                    Q.append((node - 10, count + 1))
                    visited[node - 10] = True

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    result = 0
    # 계산한 결과값을 인덱스로 방문여부 확인하도록 해서 같은 계산 결과가 나온 경우는 가지치도록 함
    visited = [False]*1000001 #최대 백만까지이므로
    Q = deque()
    Q.append((N, 0)) #처음 시작 숫자, 카운트 횟수(최소 횟수가 나와야 하므로)
    bfs()

    print("#{} {}".format(test_case, result))