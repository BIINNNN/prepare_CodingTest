from collections import deque

n, m, v = map(int, input().split()) #각각 정점의 개수, 간선의 개수, 탐색을 시작할 정점번호

graph = [[0]*(n+1) for _ in range(n+1)] #정점 개수만큼 인접그래프 생성
visited = [False for _ in range(n+1)] #방문 확인

for _ in range(m):
    a, b = map(int, input().split()) # 간선이 연결하는 두 정점번호 M세트
    graph[a][b] = 1
    graph[b][a] = 1

#print(graph)

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in range(1, n+1):
        if not visited[i] and graph[v][i] == 1: #방문하지 않은 노드이고, 인접한 노드라면
            dfs(i)

def bfs(v):
    queue = deque()
    queue.append(v)
    # dfs를 실행한 뒤에 bfs를 실행하기 떄문에
    # 방문처리가 이미 되어 있으므로 여기서는 visited가 True인 경우를 사용해야 함
    visited[v] = False
    while queue: #큐가 빌때까지 반복
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if visited[i] and graph[v][i]==1:
                queue.append(i)
                visited[i] = False

dfs(v)
print()
bfs(v)