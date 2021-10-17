import sys
sys.stdin = open("input_4871.txt", "r")

T = int(input())

#dfs 적용
def search_path(S, G): #경로존재 확인할 함수
    stack = [] #방문중인 노드 저장할 스택
    visited = [0]*(V+1) #방문 여부 표시할 리스트(노드 번호와 일치하는 인덱스 번호에 기록)

    stack.append(S) #출발노드 방문중이므로 스택에 집어넣음

    while stack: #스택에 남은 것이 없을 때까지 반복
        now = stack.pop() #현재 스택의 탑에 있는 것을 꺼내서 현재 방문중인 노드로 할당
        visited[now] = 1 #방문 표시
        for next in range(1, V+1):
            if not visited[next] and graph[now][next]: #다음 노드에 방문한 적이 없고, 현재 노드에 연결된 노드라면
                stack.append(next) # 방문노드로 저장
                visited[next] = 1 #방문 표시

    if visited[G]: #만약 마지막 도착 노드에 방문한 적이 있다면
        return 1
    else:
        return 0


for test_case in range(1, T+1):
    V, E = map(int, input().split()) # V: 노드의 개수, E: 간선의 개수
    # V+1을 해주는 이유 - 노드는 1번부터 시작하기 때문에 리스트의 인덱스 번호와 맞추기 위해(혼동 방지)
    graph = [[0 for _ in range(V+1)]for _ in range(V+1)] #해당 노드 번호와 연결된 노드번호를 저장하는 리스트

    for _ in range(0, E): #간선 개수만큼 정보 주어짐
        start, end = map(int, input().split()) # 출발, 노드 간선
        graph[start][end] = 1

    S, G = map(int, input().split()) # 경로 존재를 확인할 출발노드와 도착노드

    result = search_path(S, G)

    print("#{} {}".format(test_case, result))